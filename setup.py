# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.1'

long_description = \
    read('docs', 'README.rst') + \
    read('docs', 'HISTORY.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='tutorial.todoapp',
    version=version,
    description="A simple ToDo app tutorial for Plone.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='Caipirinha Sprinters',
    author_email='plone-users@lists.sourceforge.net',
    url='http://githib.com/collective/tutorial.todoapp',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['tutorial'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'Pillow',
        'Plone',
        'plone.api',
        'plone.app.dexterity',
        'setuptools',
    ],
    extras_require={
        'develop': [
            'flake8',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zptlint',
        ],
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
