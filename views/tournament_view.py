from models.tournament import Tournament
from views.helpers import title_2, title_3


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
            print(
                f"\n----------------------- The tournament id : {tournament.id} ----------------------- \n"
                f"  Name = {tournament.name}"
            )
            if tournament.end_datetime:
                print(
                    f"  Date = {tournament.start_datetime} - {tournament.end_datetime}"
                )
            else:
                print(f"  Date = {tournament.start_datetime}")
            print(
                f"  Place = {tournament.place} \n"
                f"  Number of rounds = {tournament.number_rounds} \n"
                f"  Description = {tournament.description} \n"
            )
        elif all_tournaments:
            print(
                "\n----------------------- List tournaments -----------------------\n"
            )
            for id, tournament_object in all_tournaments.items():
                print(
                    f"{id} \n   Name: {tournament_object.name} |"
                    f" Place: {tournament_object.place} |"
                    f" Date: {tournament_object.start_datetime} -"
                    f" {tournament_object.end_datetime} \n\n"
                )
            print("\n-------------------------------------------------------\n")
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
