from setuptools import setup

setup(
    name='ColorStealthGame',
    version='0.1',
    packages=['colorgame'],
    install_requires=[
        'pygame'
    ],
    entry_points={
        'console_scripts': ['colorgame=colorgame.app:main'],
    },
    url='https://www.github.com/neuroneuro15/ColorStealthGame',
    license='MIT',
    author='Nicholas A. Del Grosso and Anna Durbanova',
    author_email='delgrosso.nick@gmail.com',
    description='Abstract Pygame made for mini game jam around the theme "invisibilitity".  Two Players have to find themselves in a chaotic sea, then find each other!'
)
