# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src', 'sphinx_antsibull_ext': 'src/sphinx_antsibull_ext'}

packages = \
['antsibull_docs',
 'antsibull_docs.cli',
 'antsibull_docs.cli.doc_commands',
 'antsibull_docs.data',
 'antsibull_docs.data.docsite',
 'antsibull_docs.docs_parsing',
 'antsibull_docs.jinja2',
 'antsibull_docs.schemas',
 'antsibull_docs.schemas.docs',
 'antsibull_docs.utils',
 'antsibull_docs.vendored',
 'sphinx_antsibull_ext']

package_data = \
{'': ['*'],
 'antsibull_docs.data': ['sphinx_init/*'],
 'antsibull_docs.data.docsite': ['macros/*'],
 'sphinx_antsibull_ext': ['css/*']}

install_requires = \
['ansible-pygments',
 'antsibull-core>=1.2.0,<2.0.0',
 'asyncio-pool',
 'docutils',
 'jinja2',
 'packaging',
 'rstcheck>=3.0.0,<7.0.0',
 'sphinx']

entry_points = \
{'console_scripts': ['antsibull-docs = antsibull_docs.cli.antsibull_docs:main']}

setup_kwargs = {
    'name': 'antsibull-docs',
    'version': '1.7.2',
    'description': 'Tools for building Ansible documentation',
    'author': 'Toshio Kuratomi',
    'author_email': 'a.badger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ansible-community/antsibull-docs',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
