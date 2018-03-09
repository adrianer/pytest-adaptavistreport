from setuptools import setup

setup(
    name='pytest-adaptavistreport',
    description='pytest plugin that aims to report test cases results to Jiras plugin Adaptavist Test Management.',
    long_description=open("README.md").read(),
    version='0.0.1',
    url='https://github.com/mabouelfadl/pytest-adaptavistreport',
    download_url='https://github.com/mabouelfadl/pytest-adaptavistreport/archive/0.1.tar.gz',
    license='proprietary',
    author='Mariam Abouelfadl',
    author_email='mabouelfadl@gmail.com',
    py_modules=['pytest_adaptavistreport'],
    entry_points={'pytest11': ['adaptavistreport = pytest_adaptavistreport']},
    platforms='any',
    install_requires=['pytest>=3.3.2'],
)
