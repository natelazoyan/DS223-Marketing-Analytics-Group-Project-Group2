from setuptools import setup, find_packages

setup(
    author='Group 2',
    description='ETL related content',
    name='etl',
    version='0.1.0',
    packages=find_packages(include=['etl','etl.*']),
    
)