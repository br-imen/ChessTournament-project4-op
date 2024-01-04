# import json
from settings import ABSOLUTE_PATH
import json


class Player:
    def __init__(self, first_name, last_name, date_birth, id_player) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.id_player = id_player

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_birth": self.date_birth,
            "id_player": self.id_player,
        }

    @classmethod
    def deserialize(cls, dict_player):
        player = cls(**dict_player)
        return player

    @classmethod
    def deserialize_all_players(cls, dict_all_players):
        dict_all_players_object = {}
        for key, value in dict_all_players.items():
            player = cls.deserialize(value)
            dict_all_players_object[key] = player
        return dict_all_players_object

    def save(self):
        try:
            with open(f"{ABSOLUTE_PATH}/data/players/players.json", "r") as player_file:
                dict_players = json.load(player_file)
        except FileNotFoundError:
            dict_players = {}
        dict_players[self.id_player] = self.serialize()
        with open(f"{ABSOLUTE_PATH}/data/players/players.json", "w") as player_file:
            json.dump(dict_players, player_file)

        # Mentor note : verify id does not exist !
        # Mentor note : tinydb
