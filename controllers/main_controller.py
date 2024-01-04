import sys
from controllers.player_contoller import PlayerController
from controllers.tournament_controller import TournamentController
from views.player_view import PlayerView
from views.main_menu import MainMenu
from views.tournament_view import TournamentView
from views.reports_view import ReportsView
import os
from settings import DATA_PATH


class MainController:
    def __init__(self):
        self.tournament = None
        self.tournament_path = f"{DATA_PATH}/tournaments"
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.report_view = ReportsView()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()

    # To create a data folder
    def create_data_folder(self):
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        if not os.path.exists(self.player_controller.player_path):
            os.makedirs(self.player_controller.player_path)
        if not os.path.exists(self.tournament_path):
            os.makedirs(self.tournament_path)

    # Start program
    def start(self):
        self.create_data_folder()
        MainMenu.welcome()
        while True:
            # MainMenu to choose
            menu = MainMenu()
            choice = menu.menu_principal()
            # To register player
            if choice == "1":
                self.player_view.display_register_player()
                self.player_controller.register_player()
            # To create tournament
            if choice == "2":
                self.tournament_view.display_create_tournament()
                tournament = self.tournament_controller.create_tournament()
                if tournament:
                    self.tournament = tournament
                    self.tournament_controller.control_tournament()
            # To show reports
            if choice == "3":
                self.report_view.display_title()
                while True:
                    report_choice = self.report_view.report_menu()

                    # See reports of a tournament
                    if report_choice == "2":
                        self.tournament_view.display_tournament_reports()
                        self.tournament_controller.tournament_report()
                    # Show all players
                    elif report_choice == "1":
                        self.player_view.display_all_players()
                        self.player_controller.show_all_players()
                    # Go back
                    elif report_choice == "0":
                        break
            # To continue a tournament:
            if choice == "4":
                """Get last tournament, if exist self.tournament gets the last tournament and
                resume the tournament"""
                last_tournament = self.tournament_controller.resume_last_tournament()
                if last_tournament:
                    self.tournament = last_tournament
                    self.tournament_controller.control_tournament()
            if choice == "0":
                sys.exit()
            else:
                continue
