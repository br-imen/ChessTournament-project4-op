class MatchView:
    @classmethod
    def get_match(cls):
        match = input("\nType the name of match to update: \n")
        return match

    @classmethod
    def get_score_player(cls):
        response = input(
            "\n-------- Update the score of ** Player 1 ** ---------\n\n     Type (1) if won  \n     Type (2) if lost \n     Type (3) if a tie \nYour response: "
        )
        if response == "1":
            point_player1 = 1
            point_player2 = 0
        if response == "2":
            point_player1 = 0
            point_player2 = 1
        if response == "3":
            point_player1 = 0.5
            point_player2 = 0.5
        return point_player1, point_player2
