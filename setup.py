import os

from setuptools import setup

setup(
    name='template_store',
    version='0.1.0-pre-release',
    description='lumoz.ai brick templates store',
    url='',
    author='Attinad Software',
    author_email='attinad@attinadsoftware.com',
    license='MIT',
    install_requires=[
        'grpcio',
        'grpcio-tools',
    ],
    packages=['template_store'],
    zip_safe=False
)
