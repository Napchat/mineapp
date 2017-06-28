from flask import Blueprint, render_template, abort, g, redirect, url_for, session
from jinja2 import TemplateNotFound
from mineapp.forms import NameForm

blue1 = Blueprint('blue1', __name__, template_folder='templates', static_folder='static')

@blue1.before_request
def before_request():
    g.logged_in = False

@blue1.route('/login', methods=['GET', 'POST'])
def login():
    try:
        form = NameForm()
        if form.validate_on_submit():
            session['name'] = form.name.data
            g.logged_in = True
            return redirect(url_for('blue1.index'))
        return render_template('blue1/login.html', form=form, name=session.get('name'))
    except TemplateNotFound:
        abort(404)

@blue1.route('/')
@blue1.route('/index')
def index():
    try:
        if not g.logged_in:
            return redirect(url_for('blue1.login'))
        return render_template('blue1/index.html')
    except TemplateNotFound:
        abort(404)