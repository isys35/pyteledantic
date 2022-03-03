from os import path

import setuptools
from setuptools import setup

BASE_PATH = path.abspath(path.dirname(__file__))

with open(path.join(BASE_PATH, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(BASE_PATH, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

with open('requirements.txt', encoding='utf-8') as f:
    required_packages = f.read().splitlines()

setup(
    name='pyteledantic',
    version=version,
    description='Pydantic models for Telegram Bot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/isys35/pyteledantic',
    author='isys35',
    author_email='isysbas@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='pydantic telegram api bot',
    python_requires='>=3.9, <4',
    install_requires=required_packages,
    packages=setuptools.find_packages(),
    project_urls={
        'Source': 'https://github.com/isys35/pyteledantic',
    },
)