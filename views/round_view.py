from models.round import Round
from views.helpers import print_table, title_4
from views.match_view import MatchView


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
        print("\n\n\n------------------------------------------------------------------------")
        title = round.name
        round_serialzed = round.serialize()
        columns = ["name", "start_datetime", "end_datetime"]
        rows = [[round_serialzed["name"],
                round_serialzed["start_datetime"],
                round_serialzed["end_datetime"]]]
        print_table(title=title,
            columns=columns,
            rows=rows)
        
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
            list_rounds = tournament.list_rounds
            for round in list_rounds:
                cls.display_round(round)

    
    @classmethod
    def display_title_4(cls, message):
        title_4(message=message)
