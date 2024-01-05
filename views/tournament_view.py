from models.tournament import Tournament
from views.helpers import print_table, title_2, title_3


class TournamentView:
    def __init__(self) -> None:
        """Tournament View
        class that serves as a view for tournament model
        """
        pass

    def get_inputs(self):
        dict_inputs = {}
        list_inputs = ["name", "place", "number_rounds", "description"]
        for element in list_inputs:
            while True:
                data = input(f"\n{element} : ")
                if self.validate_input(element, data):
                    break
            if element == "number_rounds":
                data = int(data)
            dict_inputs[element] = data
        return dict_inputs

    def validate_input(self, element, data):
        """validate input

        Args:
            element (str): the name of the attribute
            data : the data of the attribute

        Returns:
            bool: if is valide it return True else is return False
        """
        if data:
            if element == "number_rounds":
                if data.isdigit():
                    return True
                else:
                    self.error("Invalid number rounds")
                    return False
        else:
            self.error("Missing input")
            return False
        return True

    # Print tournament that's created
    def display_tournament_data(
        self, tournament: Tournament = None, all_tournaments: dict = None
    ):
        if tournament:
            title = f" tournament : {tournament.id}"
            columns = [
                "id",
                "Name",
                "Place",
                "start_datetime",
                "end_datetime",
                "Number of rounds",
                "description",
            ]
            tournament = tournament.serialize()
            rows = [
                [
                    tournament["id"],
                    tournament["name"],
                    tournament["place"],
                    tournament["start_datetime"],
                    tournament["end_datetime"],
                    str(tournament["number_rounds"]),
                    tournament["description"],
                ]
            ]
            print_table(title=title, columns=columns, rows=rows)
        elif all_tournaments:
            title = "List tournaments"
            columns = ["id", "Name", "Place", "start_datetime", "end_datetime"]
            rows = []

            for id, tournament_object in all_tournaments.items():
                tournament = tournament_object.serialize()
                rows.append(
                    [
                        id,
                        tournament["name"],
                        tournament["place"],
                        tournament["start_datetime"],
                        tournament["end_datetime"],
                    ]
                )
            print_table(title=title, columns=columns, rows=rows)
        else:
            self.error("No tournament found")

    # Print error
    def error(self, message):
        print(f"\nError: {message} \n")

    def error_finish_tournament(self):
        return self.error(
            "There still a tournament not completed, you can't create a new one."
        )

    def error_player_not_found(self):
        return self.error("Player's id not found")

    def error_no_tournament(self):
        return self.error("No tournament found")

    def error_no_tournament_resume(self):
        return self.error("No tournament to resume")

    def error_player_exist(self):
        return self.error("Player already registred in tournament")

    # Print info

    def info(self, message):
        print(f"\nInfo: {message} \n")

    def info_add_player(self):
        return self.info("You must add another player")

    def display_title_2(self, message):
        title_2(message=message)

    def display_title_3(self, message):
        title_3(message=message)

    def display_tournament_players(self):
        return self.display_title_3("Tournament Players")

    def display_tournament_rounds(self):
        return self.display_title_3("Tournament Rounds")

    def display_add_player(self):
        return self.display_title_3("Add Player")

    def display_start_round(self):
        return self.display_title_3("Start Round")

    def display_tournament_menu(self):
        return self.display_title_2("Tournament Menu")

    def display_create_tournament(self):
        return self.display_title_2("Create Tournament")

    def display_tournament_reports(self):
        return self.display_title_2("Tournament Reports")
