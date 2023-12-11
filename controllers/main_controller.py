from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
from views.menu import Menu
from views.round_view import RoundView
from views.tournament_view import TournamentView
from views.match_view import MatchView
from views.reports_view import ReportsView
import os
from settings import ABSOLUTE_PATH
import json


class MainController:
    def __init__(self):
        self.tournament = None
        self.tournament_path = None
        self.player_path = None

    # To create a data folder
    def create_data_folder(self):
        data_path = f"{ABSOLUTE_PATH}/data"
        self.player_path = f"{data_path}/players"
        self.tournament_path = f"{data_path}/tournaments"
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        if not os.path.exists(self.player_path):
            os.makedirs(self.player_path)
        if not os.path.exists(self.tournament_path):
            os.makedirs(self.tournament_path)

    # To create tournament
    def create_tournament(self):
        list_tournaments_not_completed = self.filter_tournaments(end_datetime=None)
        if list_tournaments_not_completed == []:
            tournament_dict = TournamentView.get_inputs()
            tournament = Tournament(**tournament_dict)
            self.tournament = tournament
            self.save()
            TournamentView.display_tournament_data(tournament=tournament)
            return "sucess"
        else:
            TournamentView.error("There still a tournament not completed, you can't create a new one.")
            return "failed"

    # Register Player:
    def create_player(self):
        player_verif = True
        while player_verif:
            player_dict = PlayerView.get_inputs()
            player_verif = self.search_player(id=player_dict['id_player'])
            if player_verif:
                PlayerView.error("Player exist ! Please enter inputs again")
        player = Player(**player_dict)
        player.save()
        return player

    # Add player to tournament
    def add_player_tournament(self):
        len_list_players = 1
        while len_list_players % 2 != 0:
            id = PlayerView.get_id()
            player_object = self.search_player(id)
            if not player_object:
                TournamentView.error("Player's id not found")
                continue

            # Get list of ids already registred in tournament.list_players
            list_ids = []
            for element in self.tournament.list_players:
                list_ids.append(element.id_player)

            # If there is, the player cannot be added
            if id in list_ids:
                TournamentView.error("Player already registred in tournament")
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
                TournamentView.info("You must add another player")

    # Start round
    def start_round(self):
        if self.tournament.list_rounds is None:
            number_rounds = 0
        else:
            number_rounds = len(self.tournament.list_rounds)

        if number_rounds < self.tournament.number_rounds:
            # To create a round
            round = self.create_round()

            # Add it to list_round in tournament object
            self.tournament.add_round(round)

            RoundView.display_round(round)
            return round

    # To create round
    def create_round(self):
        list_matchs = []
        list_players = self.tournament.list_players
        r = len(self.tournament.list_rounds)
        number_match = 1

        # There is previous rounds
        if r >= 1:
            # Create a list player filtered by score:
            sorted_list_total_scores: list[tuple()] = sorted(
                self.tournament.total_score.items(),
                key=lambda x: x[1],
                reverse=True,
            )

            # Create a list of Matchs
            for i in range(0, len(sorted_list_total_scores), 2):
                match = Match(
                    name=f"match{number_match}",
                    player1_id=sorted_list_total_scores[i][0],
                    player2_id=sorted_list_total_scores[i + 1][0],
                )
                list_matchs.append(match)
                number_match += 1

        # The first round
        else:
            # Create a list of Matchs
            for i in range(0, len(list_players), 2):
                match = Match(
                    name=f"match{number_match}",
                    player1_id=list_players[i].id_player,
                    player2_id=list_players[i + 1].id_player,
                )
                list_matchs.append(match)
                number_match += 1

        # Create a round
        round = Round(name=f"round{r+1}", list_matchs=list_matchs)

        return round

    # To end round:
    def end_round(self, round: Round):
        # Get number of rounds have been done
        number_rounds = len(self.tournament.list_rounds)

        # If number of rounds have been done is equal or exceed the number of total rounds in tournament object, we end the round and the tournamment.
        if number_rounds >= self.tournament.number_rounds:
            round.end_round()
            self.tournament.end_tournament()
            self.save()
            MatchView.display_match(total_score=self.tournament.total_score)
            return

        # There is more rounds to finish, we end only the round
        else:
            round.end_round()
            self.save()
            return

    # Show list_players of tournament
    def show_list_players_tournament(self):
        PlayerView.display_player_list(tournament=self.tournament)

    # Return all players data:
    def get_all_players_data(self, return_type=dict):
        dict_players = {}
        try:
            with open(f"{self.player_path}/players.json", "r") as players_file:
                dict_players = json.load(players_file)
        except FileNotFoundError:
            TournamentView.error("No players")
        dict_all_players_objects = Player.deserialize_all_players(dict_players)
        return dict_all_players_objects

    # Show all list players
    def show_all_players(self):
        dict_all_players_objects = self.get_all_players_data()
        PlayerView.display_player_list(all_players=dict_all_players_objects)

    # Show match and rounds
    def show_rounds_matchs(self):
        RoundView.display_all_rounds(tournament=self.tournament)

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

    # Show all tournaments:
    def show_all_tournaments(self):
        dict_tournaments_objects = self.get_all_tournaments_data()
        TournamentView.display_tournament_data(all_tournaments=dict_tournaments_objects)

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
            TournamentView.error("No tournament found")
        return dict_tournaments_objects

    # search for id tournament:
    def search_tournament(self, id):
        dict_tournaments_objects = self.get_all_tournaments_data()
        if id in dict_tournaments_objects:
            return dict_tournaments_objects[id]
    
    def filter_tournaments(self, end_datetime=None):
        dict_tournaments_objects = self.get_all_tournaments_data()
        list_tournaments_objects = []
        for id, tournament_object in dict_tournaments_objects.items():
            if tournament_object.end_datetime == end_datetime:
                list_tournaments_objects.append(tournament_object)
        return list_tournaments_objects

    # search for id player:
    def search_player(self, id):
        dict_players_object = self.get_all_players_data()
        if id in dict_players_object:
            return dict_players_object[id]
        else:
            return {}

    # Get the last tournament
    def get_last_tournament(self):
        all_tournaments_objects = self.get_all_tournaments_data()
        for id, tournament_object in all_tournaments_objects.items():
            if not tournament_object.end_datetime:
                last_tournament_object = tournament_object
                return last_tournament_object

    # Start and end a round
    def run_round(self):
        if not self.tournament.list_players:
            # Round view error missing players error
            RoundView.error(
                "You can't start round there is no players registred in the tournament"
            )
            pass
        elif len(self.tournament.list_players) % 2 != 0:
            # roundview info
            RoundView.info("Add another player.")
        else:
            round = self.start_round()
            for match in round.list_matchs:

                # Get points of two players
                points_players: tuple(str) = MatchView.get_score_player(match)

                # Update the score in match:
                match.score_player1 = points_players[0]
                match.score_player2 = points_players[1]
                MatchView.display_match(match=match, updated=True)

            self.end_round(round)

            if len(self.tournament.list_rounds) == self.tournament.number_rounds:
                return

    # Start program
    def start(self):
        self.create_data_folder()

        while True:
            # Menu to choose
            menu = Menu()
            choice = menu.menu_principal()

            # To register player
            if choice == "1":
                self.register_player()

            # To create tournament
            if choice == "2":
                result = self.create_tournament()
                if result == "sucess":
                    self.control_tournament()

            # To show reports
            if choice == "3":
                # Show all tournaments
                self.show_all_tournaments()
                while True:
                    report_choice = ReportsView.report_menu()

                    # See reports of a tournament
                    if report_choice == "2":
                        self.tournament_report()

                    # Show all players
                    elif report_choice == "1":
                        self.show_all_players()

                    # Go back
                    elif report_choice == "0":
                        break

            # To continue a tournament:
            if choice == "4":
                self.resume_last_tournament()
                self.control_tournament()
            else:
                continue
    
    def resume_last_tournament(self):
        last_tournament = self.get_last_tournament()
        if last_tournament == None:
            TournamentView.error("No tournament to resume")
            return
        self.tournament = last_tournament

    def register_player(self):
        player = self.create_player()
        PlayerView.display_player(player=player)
        PlayerView.info("Player registred\n")
    
    def tournament_report(self):
        id_tournament = ReportsView.report_tournament_menu()
        tournament_object = self.search_tournament(id_tournament)
        if tournament_object:
            TournamentView.display_tournament_data(
                tournament=tournament_object
            )
            self.tournament = tournament_object
            while True:
                choice_report = ReportsView.get_reports()

                # Show list players in tournament
                if choice_report == "1":
                    self.show_list_players_tournament()

                # Show list of rounds and its matchs of one tournament
                if choice_report == "2":
                    self.show_rounds_matchs()

                if choice_report == "0":
                    break
        else:
            TournamentView.error("No tournament found")
            pass
    
    def control_tournament(self):
        while not (
            len(self.tournament.list_rounds) == self.tournament.number_rounds
        ):
            choice = RoundView.menu_start_round(len(self.tournament.list_rounds))

            # To add player
            if choice == "1":
                self.add_player_tournament()

            # To start a round:
            if choice == "2":
                self.run_round()

            if choice == "0":
                self.save()
                break