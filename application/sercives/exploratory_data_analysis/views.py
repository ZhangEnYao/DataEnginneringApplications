from flask import redirect
from flask_login import login_required

from . import UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME, exploratory_data_analysis


@exploratory_data_analysis.route("/")
@login_required
def index():
    return redirect(UNIFORM_RESOURCE_LOCATOR_BASE_PATHNAME)
