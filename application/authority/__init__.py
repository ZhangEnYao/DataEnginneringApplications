from flask import Blueprint
authority = Blueprint(
    'authority',
    __name__,
    url_prefix='/authority'
)

from . import views, errors