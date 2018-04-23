from flask import Markup
from os import path, name as osName
from sys import version_info
if version_info.major == 2:
    FileNotFoundError = IOError

class colorpicker(object):
    def __init__(self, app=None, local=[]):
        """
        initiating extension with flask app instance
        @param: app Flask app instance (Default: None)
        @param: local to load .js .css source code locally (Default: [])
        """
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
        self.injectThem()  # injecting module into the template

    def init_app(self, app):
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        pass

    def injectThem(self):
        """ to inject the module into the template as colorpicker """
        @self.app.context_processor
        def inject_vars():
            return dict(colorpicker=self)

    def loader(self):
        """ to get html imports of colorpicker scripts and css """
        html = ""
        for i, n in enumerate(['js', 'css']):
            links = ['https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.css',
                     'https://cdnjs.cloudflare.com/ajax/libs/spectrum/1.8.0/spectrum.min.js'] if self.local == [] else self.local
            if self.local != []:
                def togglePath(rev=False, links=links):
                    """
                        Function to fix windows OS relative path issue
                        ISSUE 1 : windows os path
                        if windows used and windows path not used.
                    """
                    if osName == 'nt':
                        order = ['\\', '/'] if rev else ['/', '\\']
                        for linkIndex, link in enumerate(links):
                            links[linkIndex] = link.replace(order[0], order[1])
                togglePath(False)
                for sl in links:
                    if not path.isfile(sl):
                        raise(FileNotFoundError(
                            "colorpicker.loader() file not found " + sl))
                togglePath(True)
            tags = [
            '<script src="%s"></script>\n',
            '<link href="%s" rel="stylesheet">\n'
            ] if self.local == [] else [ 
            '<script src="/%s"></script>\n',
            '<link href="/%s" rel="stylesheet">\n'
            ] # to fix additional / due to looping !!
            html += tags[i] % [
                l for l in links if l.split(
                    '.')[len(l.split('.')) - 1] == n][0]
        return Markup(html)

    def picker(self, ids=[".colorpicker"],
               default_color='rgb(0,0,255)',
               color_format='rgb',
               showAlpha='true',
               showInput='false',
               showButtons='false',
               allowEmpty='true'):
        """
        to get html ready colorpicker initiation with the given options
        @param: ids list of identifiers of the html element to assign the color picker to
        (Default: '.colorpicker')
        @param: default_color for the colorpicker to start with (Default:
        'rgb(0,0,255)')
        @param: color_format color format to use (Default: 'rgb')
        @param: showAlpha to enable alpha (Default: 'true')
        @param: showInput to show or hide the color format (Default: 'false')
        @param: showButtons to show or hide buttons (Default: 'false')
        @param: allowEmpty to allow or disallow empty input (Default: 'true')
        """
        for h, a in {'showAlpha': showAlpha,
                     'showInput': showInput,
                     'showButtons': showButtons,
                     'allowEmpty': allowEmpty}.items():
            if not isinstance(a, str):
                raise(TypeError("colorpicker.picker(%s) takes string" % h))
            if h != 'id' and a != 'true' and a != 'false':
                raise(TypeError(
                    "colorpicker.picker(%s) only true or false string" % h))
            if not isinstance(ids, list):
                raise(TypeError("colorpicker.picker(ids) requires a list of strings"))
        html = ""
        for id in ids:
            html += " ".join([
                '<script> $(document).ready(function () {'
                '$("%s").spectrum({' % id,
                'showAlpha: %s,' % showAlpha,
                'showInput: %s,' % showInput,
                'showButtons: %s,' % showButtons,
                'allowEmpty: %s,' % allowEmpty,
                'color: $("%s").val() || "%s",' % (id, default_color),
                'preferredFormat: "%s",' % color_format,
                'move: function(color) {',
                '$(this).val(color.toRgbString())',
                '},', '})',
                '}) </script>'])
        return Markup(html) # html ready colorpicker