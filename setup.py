from setuptools import setup

requires = [
    'click==6.7',
    'dominate==2.3.1',
    'Flask==0.12.2',
    'Flask-Bootstrap==3.3.7.1',
    'Flask-WTF==0.14.2',
    'itsdangerous==0.24',
    'Jinja2==2.9.6',
    'MarkupSafe==1.0',
    'visitor==0.1.3',
    'Werkzeug==0.12.2',
    'WTForms==2.1'
]
setup(
    name='mineapp',
    version='1.0',
    packages=['mineapp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)