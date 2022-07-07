from setuptools import setup

setup(
    name='renote',
    version='0.1.0',
    py_modules=['renote','note'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'renote = renote:setNote',
            ],
        },
)
