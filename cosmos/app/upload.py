from cosmos.blueprints import default_blueprint

@default_blueprint.route('/')
def index():
    return 'Index Page'

@default_blueprint.route('/upload')
def pic_upload():
    return 'Hello Phlower!'

class UploadPicView(MainDefaultView):

    def get_or_post(self):
        user_session = get_user_session()

        app_renderer = ApplicationTemplateRenderer()
        from predictit.framework.request import is_browser_MSIE
        media_picker_dict = {'browser_is_ie':is_browser_MSIE()}

        mconfig = construct_media_upload_config()
        self.ondomready_data_init('MediaUploadModule.init', mconfig, priority=90)

        return self.render_template(TemplateInfoHolder(app_renderer, 'pool/media/media_picker'), media_picker_dict)


