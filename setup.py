from setuptools import setup, find_packages
setup(name='census-income',   
      version='0.1',
      description='Census Income Prediction Pipeline',
      author='Your Name',  maintainer_email='fsdf',
      packages=find_packages(),
      install_requires=[
            'pandas',
            'numpy',
            'flask'
        ]
      )