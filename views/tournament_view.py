from models.tournament import Tournament
from views.helpers import print_table, title_2, title_3


class TournamentView:
    # Get input to create tournament
    @classmethod
    def get_inputs(cls):
        dict_inputs = {}
        list_inputs = ["name", "place", "number_rounds", "description"]
        for element in list_inputs:
            data = input(f"\n{element} : ")
            if element == "number_rounds":
                data = int(data)
            dict_inputs[element] = data
        return dict_inputs

    # Print tournament that's created
    @classmethod
    def display_tournament_data(
        cls, tournament: Tournament = None, all_tournaments: dict = None
    ):
        if tournament:
            title = f" tournament : {tournament.id}"
            columns = ["id", "Name", "Place", "start_datetime", 
                       "end_datetime", "Number of rounds", "description"]
            tournament = tournament.serialize()
            rows = [[tournament["id"],
                     tournament["name"], 
                     tournament["place"], 
                     tournament["start_datetime"],
                     tournament["end_datetime"],
                     str(tournament["number_rounds"]),
                     tournament["description"]]]
            print_table(title=title,
                columns=columns,
                rows=rows)
        elif all_tournaments:
            title = "List tournaments"
            columns = ["id", "Name", "Place", "start_datetime", "end_datetime"]
            rows = []

            for id, tournament_object in all_tournaments.items():
                tournament = tournament_object.serialize()
                rows.append([id, tournament["name"], 
                             tournament["place"], 
                             tournament["start_datetime"],
                             tournament["end_datetime"]])
            print_table(title=title,
                columns=columns,
                rows=rows)
        else:
            cls.error("No tournament found")

    # Print error
    @classmethod
    def error(cls, message):
        print(f"\nError: {message} \n")

    # Print info
    @classmethod
    def info(cls, message):
        print(f"\nInfo: {message} \n")

    @classmethod
    def display_title_2(cls, message):
        title_2(message=message)
    
    @classmethod
    def display_title_3(cls, message):
        title_3(message=message)
