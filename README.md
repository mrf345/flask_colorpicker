<h1 align='center'>flask_colorpicker</h1>
<h3 align='center'>
A Flask extension to add Spectrum jQuery color picker into the template, it makes adding and configuring multiple color pickers at a time much easier and less time consuming.
</h3>

## Install :
#### - With pip:
> - `pip install Flask-Colorpicker` <br />

#### - From the source:
> - `git clone https://github.com/mrf345/flask_colorpicker.git`<br />
> - `cd flask_colorpicker` <br />
> - `python setup.py install`

## Setup :
#### - Inside the Flask app:
```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
app = Flask(__name__)
Bootstrap(app)
colorpicker(app)
```
#### - inside the jinja template
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

## Settings:
#### - Customize:
>The accepted arguments to be passed to the `colorpicker.picker()` function are as follow:
```python
def picker(self, id=".colorpicker", # id of element to assign colorpicker to
            default_color='rgb(0,0,255,0.5)', # default color to start with
            color_format='rgb', # color format to use
            showAlpha='true', # enable or disable transparency
            showInput='false', # display or hide color picker
            showButtons='false', # display or hide buttons
            allowEmpty='true'): # allow empty input
```

#### - Local source:
> by default the extension will load spectrum plugin from [a remote CDN][25530337]. Although you can configure that to be locally through passing a list of two files .js and .css into the colorpicker module like such:
```python
colorpicker(app=app, local=['static/js/spectrum.js', 'static/css/spectrum.css'])
```
 _The order in-which the items of list are passed is not of importance, it will be auto detected via file extension_

  [25530337]: https://cdnjs.com/libraries/spectrum "Spectrum CDN"

## Credit:
> - [Spectrum][33c1000c]: jQuery color picker.

  [33c1000c]: https://github.com/bgrins/spectrum "Spectrum  website"
