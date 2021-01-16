#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import find_packages
from setuptools import setup
import {{cookiecutter.package_name}}

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="{{cookiecutter.package_name}}",
    author="{{cookiecutter.author_name}}",
    version={{cookiecutter.package_name}}.__version__,
    author_email="{{cookiecutter.author_email}}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    description="{{cookiecutter.short_description}}",
    install_requires=[
        "pandas"
    ],
    license="MIT license",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="",
    packages=find_packages(exclude=("tests")),
    test_suite="tests",
    url="{{cookiecutter.project_url}}",
    zip_safe=False,
)
