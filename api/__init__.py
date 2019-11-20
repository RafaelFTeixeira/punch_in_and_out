from flask import Flask
from infrastructure import migrate
from api import routes


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app = migrate(app)
    app.register_blueprint(routes.bp)
    return app
