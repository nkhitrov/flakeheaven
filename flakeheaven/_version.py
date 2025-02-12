try:
    # built-in
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    # external
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version('flakeheaven')
