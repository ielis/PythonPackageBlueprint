from setuptools import setup, find_packages

from pypablue import __version__

# read requirements/dependencies
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# read description/README.md
with open("README.md", 'r') as fh:
    long_description = fh.read()


setup(name='pypablue',
      version=__version__,
      packages=find_packages(),
      install_requires=requirements,

      package_data={'': ['test_data/*']},
      long_description=long_description,
      long_description_content_type='text/markdown',

      author='Daniel Danis',
      author_email='daniel.danis@jax.com',
      url='https://github.com/ielis/PythonPackageBlueprint',
      description='Template for a Python package',
      license='GPLv3',
      keywords='python package template',

      entry_points={'console_scripts': [
          'pypablue = pypablue.main:main'
      ]})
