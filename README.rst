Connect Four
============

https://en.wikipedia.org/wiki/Connect_Four


Requirements
------------

* Python 3.10+; PyPy; PyPy3


Getting Started
---------------

To set up your local environment you should create a virtualenv and
install everything into it. ::

    $ mkvirtualenv connect_four

Pip install this repo, either from a local copy, ::

    $ pip install -e connect_four

or from github, ::

    $ pip install git+https://github.com/jbradberry/connect-four#egg=connect_four

and then install the requirements ::

    $ pip install -r requirements_server.txt
    $ pip install -r requirements_player.txt

To run the server with Connect Four ::

    $ board-serve connect_four

Optionally, the server ip address and port number can be added ::

    $ board-serve connect_four 0.0.0.0
    $ board-serve connect_four 0.0.0.0 8000

To connect a client as a human player ::

    $ board-play connect_four human
    $ board-play connect_four human 192.168.1.1 8000   # with ip addr and port

To connect a client using one of the compatible `Monte Carlo Tree
Search AI <https://github.com/jbradberry/mcts>`_ players ::

    $ board-play connect_four jrb.mcts.uct    # number of wins metric
    $ board-play connect_four jrb.mcts.uctv   # point value of the board metric
