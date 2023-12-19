from models.round import Round
from views.helpers import print_table, title_4


class RoundView:
    @classmethod
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

    @classmethod
    def display_round(cls, round: Round):
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
        columns = ["name", "player1_id", "score_player1", "player2_id", "score_player2"]
        rows = []
        for match in round.list_matchs:
            rows.append(
                [
                    match.name,
                    match.player1_id,
                    str(match.score_player1),
                    match.player2_id,
                    str(match.score_player2),
                ]
            )
        print_table(title=title, columns=columns, rows=rows)

    @classmethod
    def error(cls, message):
        print(f"\nError: {message} \n")

    @classmethod
    def error_no_players_registred(cls):
        return cls.error(
            "You can't start round there is no players registred in the tournament"
        )

    @classmethod
    def info(cls, message):
        print(f"\nInfo: {message} \n")

    @classmethod
    def info_add_player(cls):
        return cls.info("Add another player.")

    @classmethod
    def display_all_rounds(cls, tournament=None):
        if tournament:
            list_rounds = tournament.list_rounds
            for round in list_rounds:
                cls.display_round(round)

    @classmethod
    def display_title_4(cls, message):
        title_4(message=message)

    @classmethod
    def display_update_match(cls, match):
        return cls.display_title_4(f"  Update {match.name}")
