"""
Flask-Formspree
-------------

Flask extension to create and modify formspree.io static forms easily
and with less repetitiveness

"""
from setuptools import setup


setup(
    name='Flask-Formspree',
    version='0.2',
    url='https://github.com/mrf345/flask_formspree/',
    download_url='https://github.com/mrf345/flask_formspree/archive/0.2.tar.gz',
    license='MIT',
    author='Mohamed Feddad',
    author_email='mrf345@gmail.com',
    description='formspree flask extension',
    long_description=__doc__,
    py_modules=['flask_formspree'],
    packages=['flask_formspree'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    keywords=['flask', 'extension', 'formspree', 'static', 'forms'],
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
