from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from mineapp.forms import NameForm

blue1 = Blueprint('blue1', __name__, template_folder='templates', static_folder='static')

@blue1.before_request
def before_request():
    pass

@blue1.route('/')
@blue1.route('/index')
def index():
    try:
        form = NameForm()
        return render_template('blue1/index.html', form=form)
    except TemplateNotFound:
        abort(404)