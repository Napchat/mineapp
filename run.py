from flask import Flask
from flask_bootstrap import Bootstrap

from mineapp.blueprints.blue1.blue1 import blue1
import config

app = Flask('mineapp')
app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(blue1)

bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run()