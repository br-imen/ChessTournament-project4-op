from controllers.player_contoller import PlayerController
from views.helpers import print_table


class MatchView:
    def __init__(self, match=None) -> None:
        """Match view
            class that serves as view for the match model
        Args:
            match (Match): Defaults to None.
        """
        self.match = match

    def get_score_player(self):
        """Input players scores

        Returns:
            tuple: players scores
        """
        # match view diplay match
        self.display_match()

        while True:
            response = input(
                f"\n\n-------- Update score for player ** {self.match.player1_id} ** ---------\n\n"
                f"   Type (1) if won  \n"
                f"   Type (2) if lost \n"
                f"   Type (3) if a tie \n\n"
                f"   Your response: "
            )
            if response == "1":
                point_player1 = 1
                point_player2 = 0
                break
            if response == "2":
                point_player1 = 0
                point_player2 = 1
                break
            if response == "3":
                point_player1 = 0.5
                point_player2 = 0.5
                break
        return point_player1, point_player2

    def display_match(self, total_score=None, updated=False):
        """display match as displaying one match score if self.match exist
            or all matchs scores at the end of the tournament

        Args:
            total_score (list[tuple]): Defaults to None.
            updated (bool): if true display updated match . Defaults to False.
        """
        player_controller = PlayerController()
        if self.match:
            title = self.match.name
            columns = [
                "player1_id",
                "player1_name",
                "score_player1",
                "player2_id",
                "player2_name",
                "score_player2",
            ]
            rows = [
                [
                    self.match.player1_id,
                    str(player_controller.search_player(self.match.player1_id)),
                    str(self.match.score_player1),
                    self.match.player2_id,
                    str(player_controller.search_player(self.match.player2_id)),
                    str(self.match.score_player2),
                ]
            ]
            if updated:
                title = f"{self.match.name} scores updated"

            print_table(title=title, columns=columns, rows=rows)
        if total_score:
            print("\n\n\n\n************* End of tournament ***************** \n")
            title = "End of tournament scores"
            columns = ["Player", "Player Name", "Score"]
            rows = []
            for player_score in total_score:
                rows.append(
                    [
                        player_score[0],
                        str(player_controller.search_player(player_score[0])),
                        str(player_score[1]),
                    ]
                )
            print_table(title=title, columns=columns, rows=rows)
