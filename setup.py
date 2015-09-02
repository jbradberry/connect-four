from distutils.core import setup

setup(
    name='ConnectFour',
    version='0.1dev',
    author='Jeff Bradberry',
    author_email='jeff.bradberry@gmail.com',
    packages=['connect_four'],
    entry_points={
        'jrb_board.games': 'connect_four.connectfour:Board',
    },
    license='LICENSE',
    description="An implementation of the game Connect Four.",
)
