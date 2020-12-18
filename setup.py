#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='saam',
    version='0.1',
    author='Riadh Hamdi',
    author_email='rhamdi@redhat.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='https://github.com/riadhhamdi/AWX_Creds_Plugin.git',
    packages=['saam'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'saam_plugin = saam:saam_plugin',
        ]
    }
)
