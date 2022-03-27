# {{cookiecutter.package_name}}
> {{cookiecutter.short_description}}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)



## Requirements
- Python 3.8 or newer

## 🛠 Installation
### Installation from source
To install the package, run the following command from a terminal:

```bash
$   python -m pip install --upgrade pip
$   pip install .
```

### Installation from `pip`
```bash
$   python -m pip install --upgrade pip
$   pip install {{cookiecutter.package_name}}
```

### Installation for development
Run the following:

```bash
$   python -m pip install --upgrade pip
$   pip install -e ".[test]"
```


### Troubleshooting installation
With `pip>=22.*.*`, you should be using PEP517, aka the `pyproject.toml` and `setup.cfg` file. This can be forced as follows:

```bash
$   python -m pip install --upgrade pip
$   pip install --use-pep517 .
```

For older `pip` versions, you may need to do the following:

```bash
$   python -m pip install --upgrade pip
$   pip install --no-use-pep517 .
```


## 🚀 Usage
Example usage of the packakge.

## 📚 Documentation
Documentation can be built using the command `make docs`, which uses the `Makefile` and the `make` binary.