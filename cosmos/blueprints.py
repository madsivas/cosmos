'''
Created on Nov 26, 2012

@author: madhu
'''
from flask import request
from flask import redirect
from flask import url_for
from flask import abort

from flask import Blueprint

from cosmos.framework.templates import ApplicationTemplateRenderer


default_blueprint = Blueprint('cosmos', __name__, template_folder='templates', static_folder='static')

def register_blueprints(app):
    app.register_blueprint(default_blueprint)

@default_blueprint.route('/')
def index():
    return 'Index Page'

@default_blueprint.route('/search')
def show_search(name=None):
    app_renderer = ApplicationTemplateRenderer()
    return app_renderer.render_template('search')

@default_blueprint.route('/upload', methods=['POST'])
def pic_upload(name=None):
    try:
        log.debug(request.json.get('media_id'))
        media_id = request.json.get('media_id')
        media_url = get_hyves_media(media_id)
        if media_id:
            PoolDomain.create_or_update_pool_avatar(pool_id, media_url)
    except UserValidationError as error:
        return dict(success=False, messages=error.messages)
    return dict(success=True, media_url=media_url)


