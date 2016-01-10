from setuptools import setup

setup(
    name="JekyllUtils",
    version='1.0',
    py_modules=['generators'],
    install_requires=[
        'Click',
        'python-slugify'
    ],
    entry_points='''
        [console_scripts]
        new=generators:new
    '''

)
    