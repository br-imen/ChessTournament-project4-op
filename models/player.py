import json
from settings import ABSOLUTE_PATH
      
class Player:

    def __init__(self, first_name, last_name, date_birth, id_player) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.id_player = id_player

    @classmethod
    def get_attributes(cls):
        return list(cls.__init__.__code__.co_varnames)[1:]

    def __str__(self) -> str:
        return f" First name : {self.first_name}, Last name : {self.last_name}, Date of birth : {self.date_birth}, id player: {self.id_player}"

    def save(self):
        player_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_birth": self.date_birth,
            "id_player": self.id_player
        }
        try:
            with open(f"{ABSOLUTE_PATH}/data/players/players.json", "r") as player_file:
                list_players = json.load(player_file)
        except FileNotFoundError:
            list_players = []
        list_players.append(player_dict)
        with open(f"{ABSOLUTE_PATH}/data/players/players.json", "w") as player_file:
            json.dump(list_players, player_file)


        # verify id does not exist !
        # tinydb 
