from flask import redirect
from flask_login import login_required

from . import UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME, database_accessor


@database_accessor.route('/')
@login_required
def index():
    return redirect(UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME)
