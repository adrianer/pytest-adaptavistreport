from setuptools import setup

setup(
    name='pytest-adaptivistreport',
    description='pytest plugin that aims to report test cases results to Jiras plugin Adaptivist Test Management.',
    long_description=open("README.md").read(),
    version='0.0.1',
    url='https://github.com/mabouelfadl/pytest-adaptivistreport',
    download_url='https://github.com/mabouelfadl/pytest-adaptivistreport/archive/0.1.tar.gz',
    license='proprietary',
    author='Mariam Abouelfadl',
    author_email='mabouelfadl@gmail.com',
    py_modules=['pytest_adaptivistreport'],
    entry_points={'pytest11': ['adaptivistreport = pytest_adaptivistreport']},
    platforms='any',
    install_requires=['pytest>=3.3.2'],
)
