
from setuptools import setup, find_packages
import os.path
import re


# reading package's version (same way sqlalchemy does)
with open(
    os.path.join(os.path.dirname(__file__), 'gitbadges', '__init__.py')
) as v_file:
    package_version = \
        re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read())\
        .group(1)


dependencies = [
]


setup(
    name='gitbadges',
    version=package_version,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important!
    install_requires=dependencies,
    packages=find_packages(exclude=['tests']),
    license='MIT',
)
