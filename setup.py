try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup

try:
    lic = open('LICENSE').read()
except:
    lic = ''

try:
    readme = open('README.md').read()
except:
    readme = 'Extra Logging Functionality'

setup(
    name='loggingextras',
    version='0.3.2',
    packages= find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sharonlev/pyLoggingExtras',
    license=lic,
    author='Sharon Lev',
    author_email='sharon_lev@yahoo.com',
    description='Extra Logging Functionality',
    long_description=readme,
    test_suite='test',
    zip_safe=False,
)
