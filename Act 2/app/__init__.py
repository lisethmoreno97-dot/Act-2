"""App package initializer.

Expose the FastAPI `app` for tests and imports, and keep package-level imports minimal.
"""

from .main import app  # re-export the FastAPI app

__all__ = ["app"]