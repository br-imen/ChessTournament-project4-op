import json
from models.player import Player
from views.player_view import PlayerView
from settings import DATA_PATH


class PlayerController:
    def __init__(self) -> None:
        self.player_path = f"{DATA_PATH}/players"

    def create_player(self):
        player_verif = True
        while player_verif:
            player_dict = PlayerView.get_inputs()
            player_verif = self.search_player(id=player_dict["id_player"])
            if player_verif:
                PlayerView.error("Player exist ! Please enter inputs again")
        player = Player(**player_dict)
        player.save()
        return player

    def register_player(self):
        player = self.create_player()
        PlayerView.display_player(player=player)
        PlayerView.info("Player registred\n")

    # Return all players data:
    def get_all_players_data(self, return_type=dict):
        dict_players = {}
        try:
            with open(f"{self.player_path}/players.json", "r") as players_file:
                dict_players = json.load(players_file)
        except FileNotFoundError:
            PlayerView.error("No players")
        dict_all_players_objects = Player.deserialize_all_players(dict_players)
        return dict_all_players_objects

    # search for id player:
    def search_player(self, id):
        dict_players_object = self.get_all_players_data()
        if id in dict_players_object:
            return dict_players_object[id]
        else:
            return {}
