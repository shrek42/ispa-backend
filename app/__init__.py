"""Main application package."""
from .jwt import Jwt_Manager
from . import app # noqa

jwt = Jwt_Manager()
