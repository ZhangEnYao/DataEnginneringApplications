from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

bootstrap = Bootstrap()
login_manager = LoginManager()


def create():
    server = Flask(__name__)
    server.secret_key = "Data Engineering Team"
    server.permanent_session_lifetime = 13 * 23

    bootstrap.init_app(server)

    login_manager.init_app(server)
    login_manager.login_view = "authority.login"

    from application.main import main as blueprint_main

    server.register_blueprint(blueprint_main)

    from application.authority import authority as blueprint_authority

    server.register_blueprint(blueprint_authority)

    from application.sercives.database_accessor import (
        database_accessor as blueprint_database_accessor,
    )
    from application.sercives.database_accessor import (
        register_dash_service as register_database_accessor,
    )

    register_database_accessor(server=server)
    server.register_blueprint(blueprint_database_accessor)

    from application.sercives.exploratory_data_analysis import (
        exploratory_data_analysis as blueprint_exploratory_data_analysis,
    )
    from application.sercives.exploratory_data_analysis import (
        register_dash_service as register_exploratory_data_analysis,
    )

    register_exploratory_data_analysis(server=server)
    server.register_blueprint(blueprint_exploratory_data_analysis)

    return server
