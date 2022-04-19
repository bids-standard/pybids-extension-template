# PyBIDS extension template

This repository is intended to demonstrate the creation of PyBIDS extension packages.
Please select a unique name, and replace all instances of `EXTENSION` with that.

This uses a very bare-bones approach to single-location versioning (in `setup.cfg`)
that will work out of the box with Python 3.8+. A conditional dependency on the
[importlib-metadata](https://importlib-metadata.readthedocs.io/) package covers packages that
still support 3.7.
You may choose to set up something like
[Versioneer](https://github.com/python-versioneer/python-versioneer/),
[versioningit](https://versioningit.readthedocs.io/) or
[setuptools_scm](https://github.com/pypa/setuptools_scm).

Build distributions with (you may need to `pip install build` first):

```
python -m build
```

Install with:

```
pip install .
```

Editable installs should work with:

```
pip install -e .
```

Happy hacking!
