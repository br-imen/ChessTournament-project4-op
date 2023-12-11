from models.round import Round
from views.match_view import MatchView


class RoundView:
    @classmethod
    def menu_start_round(self, list_rounds_length):
        if list_rounds_length == 0:
            option_start_round = input(
                "\nChoose an option to do : \nType (1) -----> to add a player in tournament \nType (2) -----> to start a round\nType (0) -----> to quit \nYour response: "
            )
        else:
            option_start_round = input(
            "\nChoose an option to do : \nType (2) -----> to start another round \nType (0) -----> to quit \nYour response: "
            )
        return option_start_round

    @classmethod
    def display_round(cls, round: Round):
        print(
            f"\n\n  ************* {round.name} *************\n"
            f"  start date : {round.start_datetime}\n"
        )
        if round.end_datetime:
            print(f"  End date : {round.end_datetime}\n")
        for match in round.list_matchs:
            MatchView.display_match(match)

    @classmethod
    def error(cls, message):
        print(f"\nError: {message} \n")

    @classmethod
    def info(cls, message):
        print(f"\nInfo: {message} \n")

    @classmethod
    def display_all_rounds(cls, tournament=None):
        if tournament:
            print(
                f"\n  --------------- List of Rounds for '{tournament.name}' tournament --------------\n"
            )
            list_rounds = tournament.list_rounds
            for round in list_rounds:
                cls.display_round(round=round)
            print(
                "\n  -----------------------------------------------------------------------------\n"
            )
