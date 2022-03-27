# 🐍 Python package template repository
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Repository for `cookiecutter` template used for setting up a minimal Python package

Repository for holding the cookiecutter template for creating a minimal Python
package.

## ✨ Features
- 📚 Sphinx documentation
    - Auto API documentation using `sphinx-apidoc`
    - Notebook support using `nbsphinx`
- 🧱 Makefile for automating steps e.g. building docs
- ✅ Example tests using `unittest` layout
- ⚠️ Pre-commit hooks setup
- 🗄 Custom `pylintrc` file based on [Google Python Style guide](https://google.github.io/styleguide/pyguide.html)
- 📜 `CHANGELOG.md` file
- 📋 `pyproject.toml` file for setting up tools and package
- 🚅 Modern `pip` [PEP517 setup installer](https://peps.python.org/pep-0517/)

## 🛠 Requirements
- Python 3.8 or newer
- `cookiecutter`
- Make
- [`cruft`](https://github.com/cruft/cruft) (Recommended)

## 🚀 Usage
### Cookiecutter approach
Initialise the template using the `cookiecutter` command:

```bash
$   cookiecutter https://www.github.com/ismailuddin/cookiecutter-python-package-template
```

### Cruft approach
[`cruft`](https://github.com/cruft/cruft) allows your projects to keep upto date with the template repository.

For new projects, run the following:

```bash
$   cruft create https://www.github.com/ismailuddin/cookiecutter-python-package-template
```

For existing projects initialised with `cookiecutter`, run the following:

```bash
$   cruft link https://www.github.com/ismailuddin/cookiecutter-python-package-template
```

To update your project to the latest version of it's parent template:

```bash
$   cruft update
```

