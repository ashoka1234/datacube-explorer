#!/usr/bin/env python3

from setuptools import setup, find_packages
import versioneer

tests_require = [
    'pylint',
    'digitalearthau',
    'requests-html'
]

extras_require = {
    'test': tests_require,
    # These are all optional but nice to have on a real deployment
    'deployment': [
        # Performance
        'ciso8601',
        'bottleneck',
        # The default run.sh and docs use gunicorn+meinheld
        'gunicorn',
        'setproctitle',
        'meinheld',
    ],
}

setup(
    name='dea-dashboard',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    python_requires='>=3.6',

    url='https://github.com/opendatacube/datacube-explorer',
    author='Geoscience Australia',

    packages=find_packages(),
    install_requires=[
        'cachetools',
        'click',
        'dataclasses',
        'datacube>=1.6',
        'flask',
        'flask_themes @ git+https://git@github.com/maxcountryman/flask-themes@master',
        'fiona',
        'pyorbital',
        'geographiclib',
        'geoalchemy2',
        'python-rapidjson',
        'simplekml',
        'structlog',
        'Flask-Caching',
        'jinja2',
        'python-dateutil',
        'shapely',
        'gdal>=1.9'
        'pyproj',
        'pycrs',
    ],
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'cubedash-gen = cubedash.generate:cli',
        ],
    }
)
