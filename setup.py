from distutils.core import setup

version = __import__('owned_models').__version__

setup(
    name = 'django-owned-models',
    version = version,
    description = 'A package providing conveniences around the ownership of models by users.',
    long_description = open('README.rst').read(),
    author = 'Gavin Ballard',
    author_email = 'gavin@discolabs.com',
    url = 'https://github.com/discolabs/django-owned-models',
    license = 'MIT',

    packages = [
        'owned_models'
    ],

    package_dir = {
        'owned_models': 'owned_models',
    },

    requires = [
        'django',
        'tastypie',
    ],

    install_requires = [
        'django',
    ],

    zip_safe = True,
    classifiers = [],
)