# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

install_requires = (
    'lxml',
    'rhaptos.cnxmlutils',
    )
tests_require = (
    'cnx-archive',
    )
description = "Transforms cnxml to html and vice versa."

setup(
    name='cnx-cnxml-transforms',
    version='0.0.1',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/cnx-archive",
    license='LGPL, See also LICENSE.txt',
    description=description,
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        'cnxmltransforms': ['xsl/*.xsl', 'xsl/content2presentation-files/*'],
        },
    tests_require=tests_require,
    include_package_data=True,
    test_suite='cnxmltransforms.tests'
    )
