from setuptools import setup

setup(
    name='steemlogin',
    version='0.0.6',
    packages=['steemlogin'],
    url='https://github.com/digital-mine/steemlogin-python-client',
    license='MIT',
    author='digital-mine',
    author_email='digitalmine23@gmail.com',
    description='Python client library of SteemLogin',
    install_requires=["requests", "responses"]
)
