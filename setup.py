# Copyright 2023 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup for pip package."""

from setuptools import find_namespace_packages
from setuptools import setup


def _get_version():
  with open('synjax/__init__.py') as fp:
    for line in fp:
      if line.startswith('__version__'):
        g = {}
        exec(line, g)  # pylint: disable=exec-used
        return g['__version__']
    raise ValueError('`__version__` not defined in `synjax/__init__.py`')


def _parse_requirements(requirements_txt_path):
  with open(requirements_txt_path) as fp:
    return fp.read().splitlines()


_VERSION = _get_version()

setup(
    name='synjax',
    version=_VERSION,
    url='https://github.com/deepmind/synjax',
    license='Apache 2.0',
    author='DeepMind',
    description='SynJax: structured probability distributions for JAX.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email='stanojevic@google.com',
    # Contained modules and scripts.
    packages=find_namespace_packages(exclude=['*_test.py', 'examples']),
    install_requires=_parse_requirements('requirements.txt'),
    extras_require={'jax': _parse_requirements('requirements-jax.txt')},
    tests_require=_parse_requirements('requirements-test.txt'),
    requires_python='>=3.8',
    include_package_data=True,
    zip_safe=False,
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
)
