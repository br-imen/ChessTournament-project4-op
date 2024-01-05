from controllers.player_contoller import PlayerController
from models.round import Round
from views.helpers import print_table, title_4


class RoundView:
    def __init__(self) -> None:
        """Round view
        Class that serves as a view for the round
        """
        pass

    def menu_start_round(self, list_rounds_length):
        if list_rounds_length == 0:
            option_start_round = input(
                "\nChoose an option to do : \n"
                "Type (1) -----> Add a player in tournament \n"
                "Type (2) -----> Start a round\n"
                "Type (0) -----> Quit \n"
                "Your response: "
            )
        else:
            option_start_round = input(
                "\nChoose an option to do : \n"
                "Type (2) -----> Start another round \n"
                "Type (0) -----> Quit \n"
                "Your response: "
            )
        return option_start_round

    def display_round(self, round: Round):
        """Display a givin round

        Args:
            round (Round):
        """
        player_controller = PlayerController()
        print("\n")
        title = round.name
        round_serialized = round.serialize()
        columns = ["name", "start_datetime", "end_datetime"]
        rows = [
            [
                round_serialized["name"],
                round_serialized["start_datetime"],
                round_serialized["end_datetime"],
            ]
        ]
        print_table(title=title, columns=columns, rows=rows)

        title = "matchs list"
        columns = [
            "name",
            "player1_id",
            "player1_name",
            "score_player1",
            "player2_id",
            "player2_name",
            "score_player2",
        ]
        rows = []
        for match in round.list_matchs:
            player1 = player_controller.search_player(match.player1_id)
            player2 = player_controller.search_player(match.player2_id)
            rows.append(
                [
                    match.name,
                    match.player1_id,
                    str(player1),
                    str(match.score_player1),
                    match.player2_id,
                    str(player2),
                    str(match.score_player2),
                ]
            )
        print_table(title=title, columns=columns, rows=rows)

    def error(self, message):
        print(f"\nError: {message} \n")

    def error_no_players_registred(self):
        return self.error(
            "You can't start round there is no players registred in the tournament"
        )

    def info(self, message):
        print(f"\nInfo: {message} \n")

    def info_add_player(self):
        return self.info("Add another player.")

    def display_all_rounds(self, tournament=None):
        if tournament:
            list_rounds = tournament.list_rounds
            for round in list_rounds:
                self.display_round(round)

    def display_title_4(self, message):
        title_4(message=message)

    def display_update_match(self, match):
        return self.display_title_4(f"  Update {match.name}")
