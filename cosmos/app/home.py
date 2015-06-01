from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from blueprints import default_blueprint

@default_blueprint.route('/', defaults={'page': 'index'})
@default_blueprint.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)