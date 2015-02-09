from setuptools import setup, find_packages

setup(
  name='pyreil',
  description='REIL translation library.',
  author='Mark Brand',
  author_email='c01db33f@gmail.com',
  packages=find_packages(),
  install_requires=['capstone'],
)
