

class Board(object):
    num_players = 2
    rows = 6
    cols = 7

    def __init__(self, *args, **kwargs):
        pass

    def starting_state(self):
        return (0, 0, 1)

    def display(self, state, action):
        p1, p2, player = state

        piece = {0: " ", 1: u"\u25cb", 2: u"\u25cf"}
        header = "   {0}".format(
            " ".join(str(i) for i in xrange(self.cols)))
        bar = "  +{0}+".format("-"*(2*self.cols-1))
        msg = "Played: {0}\nPlayer {1} to move.".format(
            self.pack(action), player)

        board = u"\n".join(
            u"  |{0}|".format(
                u"|".join(piece[((p1 >> ((c+1) * self.rows - r - 1)) & 1) +
                                2*((p2 >> ((c+1) * self.rows - r - 1)) & 1)]
                          for c in xrange(self.cols)))
            for r in xrange(self.rows))

        board = u"\n".join((header, bar, board, bar, header, msg))
        return board

    def parse(self, action):
        return int(action)

    def pack(self, action):
        return str(action)

    def is_legal(self, history, action):
        p1, p2, player = history[-1]
        occupied = p1 | p2
        column = (occupied >> (self.rows * action)) & 0b111111
        return column <= 0b11111

    def legal_actions(self, history):
        p1, p2, player = history[-1]
        occupied = p1 | p2
        return [c for c in xrange(self.cols)
                if (occupied >> (self.rows * c)) & 0b111111 <= 0b11111]

    def next_state(self, state, action):
        p1, p2, player = state
        occupied = p1 | p2
        column = (occupied >> (self.rows * action)) & 0b111111
        column += 1
        column <<= self.rows * action
        if player == 1:
            p1 |= column
        else:
            p2 |= column
        return (p1, p2, 3 - player)

    def previous_player(self, state):
        return 3 - state[-1]

    def current_player(self, state):
        return state[-1]

    def winner(self, history):
        state = history[-1]
        p1, p2, player = state
        occupied = p1 | p2

        top_row_mask = 0x1f7df7df7df
        bottom_row_mask = 0x3efbefbefbe

        for p_num, p_val in ((1, p1), (2, p2)):
            # W
            g = p_val
            g &= (g >> 6) & p_val
            g &= (g >> 6) & p_val
            g &= (g >> 6) & p_val
            if g:
                return p_num

            # E
            g = p_val
            g &= (g << 6) & p_val
            g &= (g << 6) & p_val
            g &= (g << 6) & p_val
            if g:
                return p_num

            # N
            g = p_val
            g &= (g << 1) & p_val & bottom_row_mask
            g &= (g << 1) & p_val & bottom_row_mask
            g &= (g << 1) & p_val & bottom_row_mask
            if g:
                return p_num

            # S
            g = p_val
            g &= (g >> 1) & p_val & top_row_mask
            g &= (g >> 1) & p_val & top_row_mask
            g &= (g >> 1) & p_val & top_row_mask
            if g:
                return p_num

            # NW
            g = p_val
            g &= (g >> 5) & p_val & bottom_row_mask
            g &= (g >> 5) & p_val & bottom_row_mask
            g &= (g >> 5) & p_val & bottom_row_mask
            if g:
                return p_num

            # NE
            g = p_val
            g &= (g << 7) & p_val & bottom_row_mask
            g &= (g << 7) & p_val & bottom_row_mask
            g &= (g << 7) & p_val & bottom_row_mask
            if g:
                return p_num

            # SW
            g = p_val
            g &= (g >> 7) & p_val & top_row_mask
            g &= (g >> 7) & p_val & top_row_mask
            g &= (g >> 7) & p_val & top_row_mask
            if g:
                return p_num

            # SE
            g = p_val
            g &= (g << 5) & p_val & top_row_mask
            g &= (g << 5) & p_val & top_row_mask
            g &= (g << 5) & p_val & top_row_mask
            if g:
                return p_num

        if occupied == 0x3ffffffffff:
            return 3

        return 0

    def is_ended(self, history):
        return bool(self.winner(history))

    def win_values(self, history):
        winner = self.winner(history)
        if not winner:
            return

        if winner == 3:
            return {1: 0.5, 2: 0.5}
        return {winner: 1, 3 - winner: 0}

    points_values = win_values

    def winner_message(self, winners):
        winners = sorted((v, k) for k, v in winners.iteritems())
        value, winner = winners[-1]
        if value == 0.5:
            return "Stalemate."
        return "Winner: Player {0}.".format(winner)
