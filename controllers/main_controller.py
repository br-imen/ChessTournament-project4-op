from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.player_view import PlayerView
from views.menu import Menu
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
        # match_path = f"{data_path}/matchs"
        # round_path = f"{data_path}/rounds"
        self.tournament_path = f"{data_path}/tournaments"
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        if not os.path.exists(self.player_path):
            os.makedirs(self.player_path)
        # if not os.path.exists(match_path):
        #     os.makedirs(match_path)
        # if not os.path.exists(round_path):
        #     os.makedirs(round_path)
        if not os.path.exists(self.tournament_path):
            os.makedirs(self.tournament_path)

    # To create tournament
    def create_tournament(self):
        # Get inputs to create trounament
        tournament_dict = TournamentView.get_inputs()

        tournament = Tournament(**tournament_dict)
        print(
            f"\n *********'''{tournament.name}''' Tournament created ********* \n"
            f"* Place = {tournament.place} \n"
            f"* Start date = {tournament.start_datetime} \n"
            f"* Number of rounds = {tournament.number_rounds} \n"
            f"* Description = {tournament.description} \n"
        )
        self.tournament = tournament

    # Register Player:
    def register_player(self):
        # View: print out for player inputs
        player_dict = PlayerView.get_inputs()
        player = Player(**player_dict)
        player.save()

    # Add player to tournament
    def add_player_tournament(self):
        len_list_players = 1
        while len_list_players % 2 != 0:
            # Get id player
            id = PlayerView.get_id()

            # search id player:
            player_object= self.search_player(id)

            if not player_object:
                print("\nERROR: Player's id not found \n")
                continue

            # Get list of ids already registred in tournament.list_players
            list_ids = []
            for element in self.tournament.list_players:
                list_ids.append(element.id_player)

            # If there is, He cannot be added
            if id in list_ids:
                print("\nError:Player already registred in tournament \n")
                continue
            # Add player to player_list in Tournament object "tournament":
            self.tournament.add_player(player=player_object)
            self.save()
            print(
                "\n--------------- Names of players registred in this tournament --------------\n"
            )
            for player in self.tournament.list_players:
                print(
                    f"Player {player.first_name} {player.id_player}\n"
                )
            print(
                f"\n--------------- Total players in tournament : {len(self.tournament.list_players)} ---------------- \n"
            )
            len_list_players = len(self.tournament.list_players)
            if len_list_players % 2 != 0:
                print("\nYou must add another player\n")

    # Start round
    def start_round(self):
        if self.tournament.list_rounds is None:
            number_rounds = 0
        else:
            number_rounds = len(self.tournament.list_rounds)

        if number_rounds < self.tournament.number_rounds:
            # print(f"number list rounds : {number_list_rounds}")
            # print(len(tournament.list_rounds))

            # To create a round
            round = self.create_round()

            # Add it to list_round in tournament object
            self.tournament.add_round(round)

            # Printing the round and its matchs
            print(
                f"\n--------------------------------------------------------\n ******* {round.name} ******* \n ------------------------------------------------------"
            )
            for match in round.list_matchs:
                print(
                    f"\n   ** {match.name} ** \n   Player 1 : {match.player1_id}  Score: {match.score_player1} \n   Player 2 : {match.player2_id}  Score: {match.score_player2} \n"
                )

            return round

    # To create round
    def create_round(self):
        list_matchs = []
        list_players = self.tournament.list_players
        r = len(self.tournament.list_rounds)
        number_match = 1
        # print(f"r: {r}")

        # r : len(tournament.list_round), There is previous rounds
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
            # DISPLAY score
            print("\n************* End of tournament ***************** \n")
            print(f"\nResults : {self.tournament.total_score} \n")
            return

        # There is more rounds to be done, we end only the round
        else:
            round.end_round()
            self.save()
            return

    # Show list_players of tournament
    def show_list_players_tournament(self):
        # display list players with argument sorted in tournament view
        list_players = []
        for player in self.tournament.list_players:
            list_players.append(player)
        sorted_list_players: list[dict] = sorted(
            list_players, key=lambda x: x.first_name
        )
        print(
            "\n--------------- Names of players registred in this tournament --------------\n"
        )
        for player in sorted_list_players:
            print(player)
        print(
            "\n-----------------------------------------------------------------------------\n"
        )

    # Return all players data:
    def get_all_players_data(self):
        dict_players = {}
        try:
            with open(f"{self.player_path}/players.json", "r") as players_file:
                dict_players = json.load(players_file)           
        except FileNotFoundError:
            print("\n Error: No players \n")
        dict_all_players_objects = Player.deserialize_all_players(dict_players)
        return dict_all_players_objects

    # Show all list players
    def show_all_players(self):
        print(
            "\n----------------------- List all players -----------------------\n"
        )
        dict_players_objects = self.get_all_players_data()
        if dict_players_objects:
            for id,value in dict_players_objects.items():
                print(
                    f"{id} \n   First name: {value.first_name} | Last name: {value.last_name} | Date of birth: {value.date_birth}\n\n"
                )
        else:
            print("\nError : No players found\n")
        print("-------------------------------------------------------\n")

    # Show match and rounds
    # round view dispay round
    def show_rounds_matchs(self):
        print(
            f"\n--------------- Rounds and its matchs of '''{self.tournament.name}''' tournament --------------\n"
        )
        list_rounds = self.tournament.list_rounds
        for round in list_rounds:
            print(
                f"\n\n*************{round.name}*************\n"
                f"start date : {round.start_datetime}\n"
                f"End date : {round.end_datetime}\n"
            )
            i = 1
            for match in round.list_matchs:
                print(
                    f"---- match{i} ----\n"
                    f"Player {match.player1_id} scores: {match.score_player1}\n"
                    f"Player {match.player2_id} scores: {match.score_player2}\n"
                )
                i += 1
        print(
            "\n-----------------------------------------------------------------------------\n"
        )

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

    # display tournament  intournament view for one trourmanent
    # Show all tournaments:
    def show_all_tournaments(self):
        print(
            "\n----------------------- List tournaments -----------------------\n"
        )
        dict_tournaments_objects = self.get_all_tournaments_data()
        for id, tournament_object in dict_tournaments_objects.items():
            print(
                f"{id} \n   Name: {tournament_object.name} | Place: {tournament_object.place} | Date: {tournament_object.start_datetime} - {tournament_object.end_datetime} \n\n"
            )
        print("\n-------------------------------------------------------\n")

    # Get dict_tournaments:
    def get_all_tournaments_data(self):
        dict_tournaments_objects = {}
        try:
            with open(
                f"{self.tournament_path}/tournaments.json", "r"
            ) as tournament_file:
                dict_tournaments = json.load(tournament_file)
                dict_tournaments_objects = Tournament.deserialize_all_tournaments(dict_tournaments)
        except FileNotFoundError:
            # tournaments view no ournament fouind error
            print("\nError: no tournament found\n")
        return dict_tournaments_objects

    # search for id tournament:
    def search_tournament(self, id):
        dict_tournaments_objects = self.get_all_tournaments_data()
        if id in dict_tournaments_objects:
            return dict_tournaments_objects[id]

    # search for id player:
    def search_player(self, id):
        dict_players_object = self.get_all_players_data()
        if id in dict_players_object:
            return dict_players_object[id]

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
            print(
                "\nYou can't start round there is no players registred in the tournament \n"
            )
            pass
        elif len(self.tournament.list_players) % 2 != 0:
            # roundview info
            print("\nAdd another player. \n")
        else:
            round = self.start_round()
            for match in round.list_matchs:
                # match view diplay match
                print(
                    f"\n\n*******-- {match.name} --*******\n"
                    f"Player 1: [{match.player1_id}] ==> {match.score_player1} \n"
                    f"Player 2: [{match.player2_id}] ==> {match.score_player2} \n"
                )

                # Get points of two players
                points_players: tuple(str) = MatchView.get_score_player()

                # update the score in match:
                match.score_player1 = points_players[0]
                match.score_player2 = points_players[1]
                # match view diplay match
                print(
                    f"\n\n******* Results ******* \n"
                    f"Player 1: [{match.player1_id}] ==> {match.score_player1} \n"
                    f"Player 2: [{match.player2_id}] ==> {match.score_player2} \n"
                )

            self.end_round(round)

            if (
                len(self.tournament.list_rounds)
                == self.tournament.number_rounds
            ):
                return

    # Start program
    def start(self):
        self.create_data_folder()

        while True:
            # View : Menu to choose
            menu = Menu()
            choice = menu.menu_principal()

            # To register player
            if choice == "1":
                player = self.register_player()
                #display player in Player view
                print("\nplayer registred\n")

            # To create tournament
            if choice == "2":
                self.create_tournament()

                while not (len(self.tournament.list_rounds)== self.tournament.number_rounds):
                    # Choice from menu_tournament after creating a tournament to add player or start round:
                    # If the first round to start : printing add player or start round
                    if len(self.tournament.list_rounds) == 0:
                        choice = menu.menu_start_round()

                    # If there is a round, continue another round.
                    else:
                        choice = menu.menu_another_round()

                    # To add player
                    if choice == "1":
                        self.add_player_tournament()

                    # To start a round:
                    if choice == "2":
                        self.run_round()

                    if choice == "0":
                        self.save()
                        break


            # To show reports
            if choice == "3":
                # Show all tournaments
                self.show_all_tournaments()
                while True:
                    report_choice = ReportsView.choose_report()

                    # See reports of a tournament
                    if report_choice == "2":
                        id_tournament = ReportsView.report_tournament()
                        tournament_object = self.search_tournament(id_tournament)
                        if tournament_object:
                            # tournament view display 
                            print(f"\n\n ********* Tournament {tournament_object.id}*********\n")
                            print(f"\n\n {tournament_object.name}  from {tournament_object.start_datetime} to {tournament_object.end_datetime}\n\n")
                            self.tournament = tournament_object
                            while True:
                                choice_report = ReportsView.get_reports()

                                # Show list players in tournament
                                if choice_report == "1":
                                    self.show_list_players_tournament()

                                # Show list of rounds and its matchs of one tournament
                                if choice_report == "2":
                                    self.show_rounds_matchs()

                                if choice_report == "3":
                                    break
                        else:
                            print("\nError: no tournament found\n")
                            pass

                    # Show all players
                    elif report_choice == "1":
                        self.show_all_players()

                    # Go back
                    elif report_choice == "3":
                        break

            # To continue a tournament:
            if choice == "4":
                last_tournament = self.get_last_tournament()
                if last_tournament == None:
                    # tournament view no tournament to resume
                    print("There is no Tournament to resume")
                    continue
                self.tournament = last_tournament
                while not (len(self.tournament.list_rounds)== self.tournament.number_rounds):
                    # Choice from menu_tournament after creating a tournament to add player or start round:
                    # If the first round to start : printing add player or start round
                    if len(self.tournament.list_rounds) == 0:
                        choice = menu.menu_start_round()

                    # If there is a round, continue another round.
                    else:
                        choice = menu.menu_another_round()

                    # To add player
                    if choice == "1":
                        self.add_player_tournament()

                    # To start a round:
                    if choice == "2":
                        self.run_round()

                    if choice == "0":
                        self.save()
                        break
                        
                        

            else:
                continue
