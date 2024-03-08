#/* cSpell:disable */
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='burmesedate',
    version='0.0.1',
    author='Pho Thin Maung',
    author_email='phothinmg@gmail.com',
    description='Burmese Calendar API in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['burmesedate'],
    install_requires=['requests'],
    extras_require={
        'dev': ['pytest', 'pylint', 'coverage', 'black', 'genbadge'],
    },
    url="https://github.com/phothinmg/burmethon",

    project_urls={
        'Source Code': 'https://github.com/phothinmg/burmethon/tree/main/burmethon',
        'Bug Tracker': 'https://github.com/phothinmg/burmethon/issues',
    },
    license="Apache-2.0",
)
