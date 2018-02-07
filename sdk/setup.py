from setuptools import setup, find_packages


setup(
    name='sdk',
    version='1.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[line.strip() for line in open('requirements.txt') if len(line) > 0]
)
