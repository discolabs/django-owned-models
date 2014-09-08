from django.test import TransactionTestCase
from django.db import IntegrityError

from .recipes import UserRecipe
from .models import TestUserOwnedModel


class OwnedModelsTestCase(TransactionTestCase):
    """
    Test cases for user-owned models.

    Inherits from TransactionTestCase rather than TestCase because of the `test_different_users_can_use_same_name`
    test, which raises IntegrityErrors that cause transaction rollbacks.
    """

    def test_create_without_user_raises_typeerror(self):
        self.assertRaises(TypeError, TestUserOwnedModel.objects.create, name = 'instance')

    def test_create_with_user(self):
        user = UserRecipe.make()

        instance = TestUserOwnedModel.objects.create(user, name = 'instance')
        all_instances = TestUserOwnedModel.objects.all(user)

        self.assertEqual(len(all_instances), 1, "User has one instance created.")
        self.assertEqual(all_instances[0].id, instance.id, "ID set correctly on created instance.")
        self.assertEqual(all_instances[0].user_id, user.id, "User set correctly on created instance.")

    def test_get_or_create_with_user(self):
        user = UserRecipe.make()

        # First call to get_or_create() should create the object with the user object set on it.
        instance, created = TestUserOwnedModel.objects.get_or_create(user, defaults = {
            'name': 'instance',
        })

        self.assertTrue(created, "Instance was created with first call to get_or_create().")
        self.assertEqual(instance.user_id, user.id, "User set correctly on created instance.")

        # Second call to get_or_create() should fetch the object with the user object set on it.
        instance, created = TestUserOwnedModel.objects.get_or_create(user, defaults = {
            'name': 'instance',
        })

        self.assertFalse(created, "Instance was not created with second call to get_or_create().")
        self.assertEqual(instance.user_id, user.id, "User still set correctly on created instance.")

    def test_different_users_can_only_see_their_own_instances(self):
        user_a, user_b = UserRecipe.make(_quantity = 2)

        # Create model instances for both users.
        TestUserOwnedModel.objects.create(user_a, name = 'instance_a')
        TestUserOwnedModel.objects.create(user_b, name = 'instance_b')

        all_instances = TestUserOwnedModel.all_objects.all()
        user_a_instances = TestUserOwnedModel.objects.all(user_a)
        user_b_instances = TestUserOwnedModel.objects.all(user_b)

        self.assertEqual(len(all_instances), 2, "Total of two objects exists.")
        self.assertEqual(len(user_a_instances), 1, "User A can only see one object.")
        self.assertEqual(len(user_b_instances), 1, "User B can only see one object.")

    def test_users_can_not_fetch_other_users_instances(self):
        user_a, user_b = UserRecipe.make(_quantity = 2)

        # Create model instances for both users.
        instance_a = TestUserOwnedModel.objects.create(user_a, name = 'instance_a')
        instance_b = TestUserOwnedModel.objects.create(user_b, name = 'instance_b')

        # Assert user A can fetch their own instance with a .get() and the id of a model, but that user B can't.
        self.assertTrue(TestUserOwnedModel.objects.get(user_a, id = instance_a.id))
        self.assertRaises(TestUserOwnedModel.DoesNotExist, TestUserOwnedModel.objects.get, user_b, id = instance_a.id)

    def test_same_user_can_not_use_same_name(self):
        user = UserRecipe.make()

        self.assertTrue(TestUserOwnedModel.objects.create(user, name = 'instance'), "Instance with name 'instance' created on first call to create().")
        self.assertRaises(IntegrityError, TestUserOwnedModel.objects.create, user, name = 'instance')

    def test_different_users_can_use_same_name(self):
        user_a, user_b = UserRecipe.make(_quantity = 2)

        # First, check different users can create with same name.
        self.assertTrue(TestUserOwnedModel.objects.create(user_a, name = 'instance'), "Instance with name 'instance' created for user A.")
        self.assertTrue(TestUserOwnedModel.objects.create(user_b, name = 'instance'), "Instance with name 'instance' created for user B.")

        # Now, check neither can create again with same name.
        self.assertRaises(IntegrityError, TestUserOwnedModel.objects.create, user_a, name = 'instance')
        self.assertRaises(IntegrityError, TestUserOwnedModel.objects.create, user_b, name = 'instance')
