from __future__ import absolute_import
from distutils.core import setup

setup(
    name='ConnectFour',
    version='0.1dev',
    author='Jeff Bradberry',
    author_email='jeff.bradberry@gmail.com',
    packages=['connect_four'],
    entry_points={
        'jrb_board.games': 'connect_four = connect_four.connectfour:Board',
    },
    install_requires=['six'],
    license='LICENSE',
    description="An implementation of the game Connect Four.",
)
