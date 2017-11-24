from flask import current_app
from os import path
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class colorpicker(object):
    def __init__(self, app=None, local=[]):
        self.app = app
        self.local = local
        if self.app is not None:
            self.init_app(app)
        else:
            raise(AttributeError("must pass app to colorpicker(app=)"))
        if self.local != []:
            if len(self.local) != 2:
                raise(
                    TypeError(
                        "colorpicker(local=) requires a list of" +
                        " two files spectrum.js and spectrum.css"))
        self.injectem()

    def init_app(self, app):
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        pass

    def injectem(self):
        @self.app.context_processor
        def inject_vars():
            return dict(colorpicker=self)

    def loader(self):
        html = ""
        for i, n in enumerate(['js', 'css']):
            if self.local == []:
                links = ['https://cdnjs.cloudflare.com/ajax/' +
                         'libs/spectrum/1.8.0/spectrum.min.css',
                         'https://cdnjs.cloudflare.com/ajax/' +
                         'libs/spectrum/1.8.0/spectrum.min.js']
            else:
                links = self.local
                if not path.isfile(links[0]) and not path.isfile(links[1]):
                    raise(FileNotFoundError(
                        "colorpicker.loader() file not found "))
            tags = ['<script src="%s"></script>\n',
                    '<link href="%s" rel="stylesheet">\n']
            html += tags[i] % [
                l for l in links if l.split(
                    '.')[len(l.split('.')) - 1] == n][0]
        return html

    def picker(self, id=".colorpicker",
               default_color='rgb(0,0,255,0.5)',
               color_format='rgb',
               showAlpha='true',
               showInput='false',
               showButtons='false',
               allowEmpty='true'):
        for h, a in {'id': id,
                     'showAlpha': showAlpha,
                     'showInput': showInput,
                     'showButtons': showButtons,
                     'allowEmpty': allowEmpty}.items():
            if not isinstance(a, str):
                raise(TypeError("colorpicker.picker(%s) takes string" % h))
            if h != 'id' and a != 'true' and a != 'false':
                raise(TypeError(
                    "colorpicker.picker(%s) only true or false string" % h))
        return " ".join(['<script>',
                         '$("%s").spectrum({' % id,
                         'showAlpha: %s,' % showAlpha,
                         'showInput: %s,' % showInput,
                         'showButtons: %s,' % showButtons,
                         'allowEmpty: %s,' % allowEmpty,
                         'color: "%s",' % default_color,
                         'preferredFormat: "%s",' % color_format,
                         'move: function(color) {',
                         '$("%s").val(color.toRgbString());' % id,
                         '},', '});',
                         '</script>'])
