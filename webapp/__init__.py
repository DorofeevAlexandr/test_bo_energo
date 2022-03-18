from flask import Flask
from webapp.db import db
from webapp.test_1.views import blueprint as test_1_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    app.register_blueprint(test_1_blueprint)

    return app
