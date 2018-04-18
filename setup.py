"""
Flask-Colorpicker
-------------

A Flask extension to add Spectrum javascript color picker into the template,
it makes adding and configuring multiple color pickers at a time much easier
and less time consuming

"""
from setuptools import setup


setup(
    name='Flask-Colorpicker',
    version='0.7',
    url='https://github.com/mrf345/flask_colorpicker/',
    download_url='https://github.com/mrf345/flask_colorpicker/archive/0.7.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='color picker flask extension',
    long_description=__doc__,
    py_modules=['colorpicker'],
    packages=['flask_colorpicker'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Bootstrap'
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
