# flask_colorpicker
### A [Flask][9c2c9277] extension to add [Spectrum][2e6e1a93] javascript color picker into the template, it makes adding and configuring multiple color pickers at a time much easier and less time consuming

  [9c2c9277]: http://flask.pocoo.org/ "Flask website"
  [2e6e1a93]: https://github.com/bgrins/spectrum "Spectrum repo"

## Install it :
#### - With pip
`pip install Flask-Colorpicker` <br />
#### - or from github
`git clone https://github.com/mrf345/flask_colorpicker.git`<br />
`python setup.py install`
## Run it :
`from flask import Flask` <br />
`from flask_colorpicker import colorpicker` <br />
`app = Flask(__name__)` <br />
`colorpicker(app)` <br />
#### inside the template
`{% extends 'bootstrap/base.html'}` <br />
`{% block scripts %}` <br />
`{{ super() }}` <br />
`{{ colorpicker.loader() }}` <br />
`{{ colorpicker.picker(id=".cp") }}` <br />
`{% endblock %}`<br />
`{% block content %}` <br />
`<form class="verticalform">`<br />
`<input type="text" class="form-control cp" />` <br />
`</form>`<br />
`{% endblock %}` <br />

#### _Result_
![Spectrum](https://raw.githubusercontent.com/usb-resetter/usb-resetter.github.io/master/images/colorpicker.png)
### Extra configuration:
#### - Local Spectrum
##### by default the extension will load spectrum plugin from [a remote CDN][25530337]. Although you can configure that to be locally through passing a list of two files .js and .css into the colorpicker module like such:
`colorpicker(app=app, local=['static/js/spectrum.js', 'static/css/spectrum.css'])`
##### _The order in-which the items of list are passed is not of importance, it will be auto detected via file extension_

  [25530337]: https://cdnjs.com/libraries/spectrum "Spectrum CDN"

#### - Customize Spectrum
##### The accepted arguments to be passed to the `colorpicker.picker()` function are as follow:
`def picker(self, id=".colorpicker",` <br />
`--------> default_color='rgb(0,0,255,0.5)',` <br />
`--------> color_format='rgb',`<br />
`--------> showAlpha='true',`<br />
`--------> showInput='false',`<br />
`--------> showButtons='false',`<br />
`--------> allowEmpty='true'):`<br />
