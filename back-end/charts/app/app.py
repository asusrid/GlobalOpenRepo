from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'My_Top_Secret_Key'

    # Blueprint

    from app.blueprints.core import bp as bp_core
    bp_core.config(app)

    return app