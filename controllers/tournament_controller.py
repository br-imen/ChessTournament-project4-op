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
        self.tournament_path = f"{DATA_PATH}/tournaments"
        self.tournament = tournament
        self.round_controller = RoundController()
        self.player_controller = PlayerController()

        # To create tournament

    def create_tournament(self):
        list_tournaments_not_completed = self.filter_tournaments(end_datetime=None)
        if list_tournaments_not_completed == []:
            tournament_dict = TournamentView.get_inputs()
            tournament = Tournament(**tournament_dict)
            self.tournament = tournament
            self.save()
            TournamentView.display_tournament_data(tournament=tournament)
            return tournament
        else:
            TournamentView.error_finish_tournament()
            return

    # Add player to tournament
    def add_player_tournament(self):
        len_list_players = 1
        while len_list_players % 2 != 0:
            id = PlayerView.get_id()
            player_object = self.player_controller.search_player(id)
            if not player_object:
                TournamentView.error_player_not_found()
                continue

            # Get list of ids already registred in tournament.list_players
            list_ids = []
            for element in self.tournament.list_players:
                list_ids.append(element.id_player)

            # If there is, the player cannot be added
            if id in list_ids:
                TournamentView.error_player_exist()
                continue

            # Add player to player_list in Tournament object "tournament":
            self.tournament.add_player(player=player_object)

            # Save tournament
            self.save()

            # Display numbers of players added
            PlayerView.display_player_list(tournament=self.tournament)

            # If number impair should add another player
            len_list_players = len(self.tournament.list_players)
            if len_list_players % 2 != 0:
                TournamentView.info_add_player()

    # Save tournament:
    def save(self):
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
            TournamentView.error_no_tournament()
        return dict_tournaments_objects

    # Search for id tournament:
    def search_tournament(self, id):
        dict_tournaments_objects = self.get_all_tournaments_data()
        if id in dict_tournaments_objects:
            return dict_tournaments_objects[id]

    # Find tournament by date and defined by None not ended:
    def filter_tournaments(self, end_datetime=None):
        dict_tournaments_objects = self.get_all_tournaments_data()
        list_tournaments_objects = []
        for id, tournament_object in dict_tournaments_objects.items():
            if tournament_object.end_datetime == end_datetime:
                list_tournaments_objects.append(tournament_object)
        return list_tournaments_objects

    # Find the last tournament
    def get_last_tournament(self):
        all_tournaments_objects = self.get_all_tournaments_data()
        for id, tournament_object in all_tournaments_objects.items():
            if not tournament_object.end_datetime:
                last_tournament_object = tournament_object
                return last_tournament_object

    # Assign the last tournament to self.tournament
    def resume_last_tournament(self):
        last_tournament = self.get_last_tournament()
        if last_tournament is None:
            TournamentView.error_no_tournament_resume()
            return
        self.tournament = last_tournament
        return last_tournament

    # Tournament reports
    def tournament_report(self):
        # Show all tournaments
        dict_tournaments_objects = self.get_all_tournaments_data()
        TournamentView.display_tournament_data(all_tournaments=dict_tournaments_objects)
        id_tournament = ReportsView.report_tournament_menu()
        tournament_object = self.search_tournament(id_tournament)
        if tournament_object:
            TournamentView.display_tournament_data(tournament=tournament_object)
            self.tournament = tournament_object
            while True:
                choice_report = ReportsView.get_reports()

                # Show list players in tournament
                if choice_report == "1":
                    TournamentView.display_tournament_players()
                    PlayerView.display_player_list(tournament=self.tournament)

                # Show list of rounds and its matchs of one tournament
                if choice_report == "2":
                    TournamentView.display_tournament_rounds()
                    RoundView.display_all_rounds(tournament=self.tournament)

                if choice_report == "0":
                    break
        else:
            TournamentView.error_no_tournament()
            pass

    def control_tournament(self):
        TournamentView.display_tournament_menu()
        while not (len(self.tournament.list_rounds) == self.tournament.number_rounds):
            choice = RoundView.menu_start_round(len(self.tournament.list_rounds))

            # To add player
            if choice == "1":
                TournamentView.display_add_player()
                self.player_controller.show_all_players()
                self.add_player_tournament()

            # To start a round:
            if choice == "2":
                TournamentView.display_start_round()
                self.round_controller.run_round(tournament=self.tournament)
                self.save()

            if choice == "0":
                self.save()
                break
