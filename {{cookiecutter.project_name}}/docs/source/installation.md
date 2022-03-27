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