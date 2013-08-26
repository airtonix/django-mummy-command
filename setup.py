from setuptools import setup
from setuptools import find_packages
import os

setup(
    name='django-mummy-command',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'model-mommy>=1.0',
        'Django>=1.4'
    ],
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='Simple django management command for model-mommy',
    license='MIT',
    keywords='django, fixtures, mockups, model-mommy',
    url='https://github.com/airtonix/django-mummy-command',
    include_package_data=True,
)
