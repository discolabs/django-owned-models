from setuptools import setup, find_packages

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

    packages = find_packages(),

    install_requires = [
        'django >=1.6.5, <1.7',
        'django-tastypie >=0.11.0',
    ],

    zip_safe = True,
    classifiers = [],
)