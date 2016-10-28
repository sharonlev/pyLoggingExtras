try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

setup(
    name='LoggingExtras',
    version='0.1',
    packages= find_packages('lib'),
    package_dir={'': 'lib'},
    url='https://github.com/sharonlev/pyLoggingExtras',
    license=open('LICENSE',).read(),
    author='Sharon Lev',
    author_email='sharon_lev@yahoo.com',
    description='Extra Logging Functionality',
    long_description=open('README.md',).read(),
    test_suite='test'
)
