from os import path
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))
long_description = ""

with open(path.join(basedir, "README.md")) as f:
    long_description += f.read()


setup(
    name='Flask-Colorpicker',
    version='0.11',
    url='https://github.com/mrf345/flask_colorpicker/',
    download_url='https://github.com/mrf345/flask_colorpicker/archive/0.11.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='color picker flask extension',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['colorpicker'],
    packages=['flask_colorpicker'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Bootstrap',
        'MarkupSafe',
    ],
    keywords=['flask', 'extension', 'color', 'picker', 'spectrum',
              'colorpicker'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
