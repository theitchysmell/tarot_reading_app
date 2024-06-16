from setuptools import setup, find_packages

setup(
    name='tarot_reading_app',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'tarot_reading_app = gui:main',
        ],
    },
)
