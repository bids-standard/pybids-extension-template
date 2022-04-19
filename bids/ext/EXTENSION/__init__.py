_extname = __package__.rsplit(".", 1)[-1]
__version__ = __import__('importlib.metadata').metadata.version('pybids-' + _extname)
