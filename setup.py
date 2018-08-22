from setuptools import setup

setup(
    name='flaskfolio',
    packages=['flaskfolio'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask_wtf', 'flask_mail'
    ],
)