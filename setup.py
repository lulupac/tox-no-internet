from setuptools import setup


setup(
    name='tox-no-internet',
    description="Workarounds for using tox with no internet connection",
    url='https://github.com/lulupac/tox-no-internet',
    version='0.1.0',
    author='lulupac',
    author_email='lulupac07@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    py_modules=['tox_no_internet'],
    install_requires=['tox>=2.7'],
    entry_points={
        'tox': ['no_internet = tox_no_internet'],
    },
)
