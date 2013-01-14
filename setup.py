from distutils.core import setup

setup(
    name='django-decorators',
    version='0.1.1',
    author='Julian Amaya',
    author_email='julian@monoku.com',
    packages=['django_decorators'],
    url='http://pypi.python.org/pypi/django-decorators/',
    license='LICENSE.md',
    description='A bunch of django extra decorators.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1.1",
    ],
)