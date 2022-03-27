.PHONY: docs mypy test check clean clean-build clean-pyc clean-test dist release
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open(os.path.abspath(sys.argv[1]))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

clean: clean-build clean-pyc clean-test

clean-build: # Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: # Remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: # Remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

mypy:
	mypy {{cookiecutter.package_name}}

test:
	pytest --cov={{cookiecutter.package_name}} --cov-report html
	
check:
	pylint src/{{cookiecutter.package_name}}
	bandit src/{{cookiecutter.package_name}} -r
	flake8 src
	isort src

docs: # Generate Sphinx HTML documentation, including API docs
	rm -rf docs/source/api
	sphinx-apidoc -f -o docs/source/api {{cookiecutter.package_name}}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html

dist: clean
	python -m build --sdist
	python -m build --wheel

release: dist # Package and upload a release
	twine upload dist/*