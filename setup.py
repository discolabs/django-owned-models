from distutils.core import setup

version=__import__('owned_models').__version__

setup(
    name='django-owned-models',
    version=version,
    description='A package providing conveniences around the ownership of models by users.',
    long_description=open('README.rst').read(),
    author='Gavin Ballard',
    author_email='gavin@gavinballard.com',
    url='https://github.com/gavinballard/django-owned-models',
    license='MIT',

    packages=['owned_models'],
    package_dir={
        'owned_models': 'owned_models',
    },

    requires=['Django (>=1.3)',],
    install_requires=['Django>=1.3',],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
