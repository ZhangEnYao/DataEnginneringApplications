from flask import render_template

from . import exploratory_data_analysis


@exploratory_data_analysis.app_errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("errors/404.html"), 404
