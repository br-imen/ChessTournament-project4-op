import json
from models.player import Player
from views.player_view import PlayerView
from settings import DATA_PATH


class PlayerController:
    def __init__(self) -> None:
        self.player_path = f"{DATA_PATH}/players"
        self.player_view = PlayerView()

    # Create new player
    def create_player(self):
        """player_verif: to ask again in case the id player input exist in database"""
        player_verif = True
        while player_verif:
            player_dict = self.player_view.get_inputs()
            player_verif = self.search_player(id=player_dict["id_player"])
            if player_verif:
                self.player_view.error_player_exist()
        player = Player(**player_dict)
        player.save()
        return player

    # Register player
    def register_player(self):
        player = self.create_player()
        self.player_view.display_player(player=player)
        self.player_view.info_player_registred()

    # Return all players data:
    def get_all_players_data(self, return_type=dict):
        dict_players = {}
        try:
            with open(f"{self.player_path}/players.json", "r") as players_file:
                dict_players = json.load(players_file)
        except FileNotFoundError:
            self.player_view.error_no_players()
        dict_all_players_objects = Player.deserialize_all_players(dict_players)
        return dict_all_players_objects

    # Search for id player:
    def search_player(self, id):
        dict_players_object = self.get_all_players_data()
        if id in dict_players_object:
            return dict_players_object[id]
        else:
            return {}

    # Show all players
    def show_all_players(self):
        dict_all_players_objects = self.get_all_players_data()
        self.player_view.display_player_list(all_players=dict_all_players_objects)
