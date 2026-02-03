from .hello_b import hello_b  # noqa: F401

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # Python < 3.8
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("toy-package-a")  # Use your actual package name
except PackageNotFoundError:
    # Package not installed, use fallback
    __version__ = "0.0.0+unknown"
