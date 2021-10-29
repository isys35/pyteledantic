from os import path

import setuptools
from setuptools import setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='pyteledantic',
    version='0.0.7',
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