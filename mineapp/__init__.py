from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from mineapp.blueprints.blue1.blue1 import blue1
    app.register_blueprint(blue1)

    from flask_bootstrap import Bootstrap
    bootstrap = Bootstrap(app)

    return app