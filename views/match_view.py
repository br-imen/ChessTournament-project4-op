class MatchView:
    @classmethod
    def get_match(cls):
        match = input("\nType the name of match to update: \n")
        return match

    @classmethod
    def get_score_player(cls, match):
        print(f"\n\n**** Update {match.name} scores ****\n")

        # match view diplay match
        MatchView.display_match(match=match)

        response = input(
            f"\n\n-------- Update score for player ** {match.player1_id} ** ---------\n\n"
            f"   Type (1) if won  \n"
            f"   Type (2) if lost \n"
            f"   Type (3) if a tie \n\n"
            f"   Your response: "
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

    @classmethod
    def display_match(cls, match=None, total_score=None, updated=False):
        if match:
            if updated:
                print(f"\n  °°° scores updated °°° \n")
            else:
                print(f"\n  ---- {match.name} ----\n")
            print(
                f"  Player {match.player1_id} scores: {match.score_player1}\n"
                f"  Player {match.player2_id} scores: {match.score_player2}\n"
            )
        if total_score:
            print("\n************* End of tournament ***************** \n")
            for id, value in total_score.items():
                print(f"Player {id} scores: {value}\n")
