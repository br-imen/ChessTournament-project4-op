import json
from controllers.player_contoller import PlayerController
from controllers.round_controller import RoundController
from models.tournament import Tournament
from settings import DATA_PATH
from views.player_view import PlayerView
from views.reports_view import ReportsView
from views.round_view import RoundView
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self, tournament=None) -> None:
        """Tournament Controller
            Controller that orchestrate all the tournament's processes

        Args:
            tournament (Tournament): Defaults to None.
        """
        self.tournament_path = f"{DATA_PATH}/tournaments"
        self.tournament = tournament
        self.round_controller = RoundController()
        self.player_controller = PlayerController()
        self.report_view = ReportsView()
        self.round_view = RoundView()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()

        # To create tournament

    def create_tournament(self):
        """Create and return a tournament

        Returns:
            Tournament:
        """
        list_tournaments_not_completed = self.filter_tournaments(end_datetime=None)
        if list_tournaments_not_completed == []:
            tournament_dict = self.tournament_view.get_inputs()
            tournament = Tournament(**tournament_dict)
            self.tournament = tournament
            self.save()
            self.tournament_view.display_tournament_data(tournament=tournament)
            return tournament
        else:
            self.tournament_view.error_finish_tournament()
            return

    # Add player to tournament
    def add_player_tournament(self):
        """Add a player to tournament"""
        len_list_players = 1
        while len_list_players % 2 != 0:
            id = self.player_view.get_id()
            player_object = self.player_controller.search_player(id)
            if not player_object:
                self.tournament_view.error_player_not_found()
                continue

            # Get list of ids already registred in tournament.list_players
            list_ids = []
            for element in self.tournament.list_players:
                list_ids.append(element.id_player)

            # If there is, the player cannot be added
            if id in list_ids:
                self.tournament_view.error_player_exist()
                continue

            # Add player to player_list in Tournament object "tournament":
            self.tournament.add_player(player=player_object)

            # Save tournament
            self.save()

            # Display numbers of players added
            self.player_view.display_player_list(tournament=self.tournament)

            # If number impair should add another player
            len_list_players = len(self.tournament.list_players)
            if len_list_players % 2 != 0:
                self.tournament_view.info_add_player()

    # Save tournament:
    def save(self):
        """Save tournament to json file
        raise and exception for a json decoding error
        """
        dict_tournaments = {}
        try:
            with open(
                f"{self.tournament_path}/tournaments.json", "r"
            ) as tournament_file:
                dict_tournaments = json.load(tournament_file)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError as e:
            raise e
        dict_tournaments[self.tournament.id] = self.tournament.serialize()
        with open(f"{self.tournament_path}/tournaments.json", "w") as file:
            json.dump(dict_tournaments, file)

    # Get dict_tournaments:
    def get_all_tournaments_data(self):
        """Get all tournaments data from json file

        Returns:
            dict: dict for all tournaments data
        """
        dict_tournaments_objects = {}
        try:
            with open(
                f"{self.tournament_path}/tournaments.json", "r"
            ) as tournament_file:
                dict_tournaments = json.load(tournament_file)
                dict_tournaments_objects = Tournament.deserialize_all_tournaments(
                    dict_tournaments
                )
        except FileNotFoundError:
            self.tournament_view.error_no_tournament()
        return dict_tournaments_objects

    # Search for id tournament:
    def search_tournament(self, id):
        """Search tournament by id

        Args:
            id (str):

        Returns:
            Tournament: tournament object
        """
        dict_tournaments_objects = self.get_all_tournaments_data()
        if id in dict_tournaments_objects:
            return dict_tournaments_objects[id]

    # Find tournament by date and defined by None not ended:
    def filter_tournaments(self, end_datetime=None):
        """Filter tournaments by end_datetime

        Args:
            end_datetime (datetime): Defaults to None.

        Returns:
            list[Tournament]:
        """
        dict_tournaments_objects = self.get_all_tournaments_data()
        list_tournaments_objects = []
        for id, tournament_object in dict_tournaments_objects.items():
            if tournament_object.end_datetime == end_datetime:
                list_tournaments_objects.append(tournament_object)
        return list_tournaments_objects

    # Find the last tournament
    def get_last_tournament(self):
        """Get the last tournament

        Returns:
            Tournament:
        """
        all_tournaments_objects = self.get_all_tournaments_data()
        for id, tournament_object in all_tournaments_objects.items():
            if not tournament_object.end_datetime:
                last_tournament_object = tournament_object
                return last_tournament_object

    # Assign the last tournament to self.tournament
    def resume_last_tournament(self):
        """Resume the last tournament if exist
            and initialize self.tournament

        Returns:
            Tournament:
        """
        last_tournament = self.get_last_tournament()
        if last_tournament is None:
            self.tournament_view.error_no_tournament_resume()
            return
        self.tournament = last_tournament
        return last_tournament

    # Tournament reports
    def tournament_report(self):
        """Tournament Report
        display all tournament report
        """
        # Show all tournaments
        dict_tournaments_objects = self.get_all_tournaments_data()
        self.tournament_view.display_tournament_data(
            all_tournaments=dict_tournaments_objects
        )
        id_tournament = self.report_view.report_tournament_menu()
        tournament_object = self.search_tournament(id_tournament)
        if tournament_object:
            self.tournament_view.display_tournament_data(tournament=tournament_object)
            self.tournament = tournament_object
            while True:
                choice_report = self.report_view.get_reports()

                # Show list players in tournament
                if choice_report == "1":
                    self.tournament_view.display_tournament_players()
                    self.player_view.display_player_list(tournament=self.tournament)

                # Show list of rounds and its matchs of one tournament
                if choice_report == "2":
                    self.tournament_view.display_tournament_rounds()
                    self.round_view.display_all_rounds(tournament=self.tournament)

                if choice_report == "0":
                    break
        else:
            self.tournament_view.error_no_tournament()
            pass

    def control_tournament(self):
        """Control tournament
        control all the tournament's processes
        """
        self.tournament_view.display_tournament_menu()
        while not (len(self.tournament.list_rounds) == self.tournament.number_rounds):
            choice = self.round_view.menu_start_round(len(self.tournament.list_rounds))
            # To add player
            if choice == "1" and len(self.tournament.list_rounds) == 0:
                self.tournament_view.display_add_player()
                self.player_controller.show_all_players()
                self.add_player_tournament()

            # To start a round:
            elif choice == "2":
                self.tournament_view.display_start_round()
                self.round_controller.run_round(tournament=self.tournament)
                self.save()

            elif choice == "0":
                self.save()
                break
