# flask_colorpicker
### A [Flask][9c2c9277] extension to add [Spectrum][2e6e1a93] javascript color picker into the template, it makes adding and configuring multiple color pickers at a time much easier and less time consuming

  [9c2c9277]: http://flask.pocoo.org/ "Flask website"
  [2e6e1a93]: https://github.com/bgrins/spectrum "Spectrum repo"

## Install it :
#### - With pip
`pip install Flask-Colorpicker` <br />
#### - or from github
`git clone https://github.com/mrf345/flask_colorpicker.git`<br />
`cd flask_colorpicker` <br />
`python setup.py install`
## Run it :
```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
app = Flask(__name__)
Bootstrap(app)
colorpicker(app)
```
#### inside the template
```jinja
{% extends 'bootstrap/base.html'}
{% block scripts %}
  {{ super() }}
  {{ colorpicker.loader() }}
  {{ colorpicker.picker(id=".cp") }}
{% endblock %}
{% block content %}
  <form class="verticalform">
    <input type="text" class="form-control cp" />
  </form>
{% endblock %}
```

#### _Result_
![Spectrum](https://raw.githubusercontent.com/usb-resetter/usb-resetter.github.io/master/images/colorpicker.png)

## Settings:
#### - Local Spectrum
##### by default the extension will load spectrum plugin from [a remote CDN][25530337]. Although you can configure that to be locally through passing a list of two files .js and .css into the colorpicker module like such:

```python
colorpicker(app=app, local=['static/js/spectrum.js', 'static/css/spectrum.css'])
```
##### _The order in-which the items of list are passed is not of importance, it will be auto detected via file extension_

  [25530337]: https://cdnjs.com/libraries/spectrum "Spectrum CDN"

#### - Customize Spectrum
##### The accepted arguments to be passed to the `colorpicker.picker()` function are as follow:
```python
def picker(self, id=".colorpicker", # id of element to assign colorpicker to
            default_color='rgb(0,0,255,0.5)', # default color to start with
            color_format='rgb', # color format to use
            showAlpha='true', # enable or disable transparency
            showInput='false', # display or hide color picker
            showButtons='false', # display or hide buttons
            allowEmpty='true'): # allow empty input
```
