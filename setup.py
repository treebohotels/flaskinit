from setuptools import setup, find_packages

setup(
    name='flaskinit',
    version='0.1.0',
    description='A skeleton project structure for flask apps',
    url='https://github.com/treebohotels/flaskinit.git',
    packages=find_packages(),
    author='Sohit kumar',
    author_email='sumitk002@gmail.com',
    license='UNLICENSE',
    keywords='cli',
    install_requires=['argparse'],
    entry_points={
        'console_scripts': [
            'flaskinit = flaskinit.initalize:create_app'
        ]
    })
