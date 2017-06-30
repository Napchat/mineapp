from flask import Flask
import click

import config
from mineapp import create_app

app = create_app(config.DevelopmentConfig)

@app.cli.command()
def initdb():
    click.echo('init the db')