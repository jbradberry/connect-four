import connectfour
from boardserver import server

board = connectfour.Board()
api = server.Server(board)
api.run()
