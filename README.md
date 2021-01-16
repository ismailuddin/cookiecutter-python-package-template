# 🐍 Python package template repository
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Repository for `cookiecutter` template for setting up a minimal Python package

Repository for holding the cookiecutter template for creating a minimal Python
package.

## ✨ Features
- 📚 Sphinx documentation
    - Auto API documentation using `sphinx-apidoc`
    - Notebook support using `nbsphinx`
- 🧱 Makefile for automating steps e.g. building docs
- ✅ Example tests using `unittest` layout
- Custom `.pylintrc` file
- `CHANGELOG.md` file
- `pyproject.toml` file for setting Black formatter line length to 79    

## 🛠 Requirements
- Python 3.6 or newer
- cookiecutter
- Make

## 🚀 Usage
Initialise the template using the `cookiecutter` command:

```shell
$   cookiecutter https://www.github.com/ismailuddin/cookiecutter-python-package-template
```