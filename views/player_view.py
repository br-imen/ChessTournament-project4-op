import re

from models.player import Player
from views.helpers import print_table, title_2, title_3


class PlayerView:
    # Function: gets attributes of class and returns a dict of inputs of user.
    @classmethod
    def get_inputs(cls):
        dict_inputs = {}
        list_attributes = ["first_name", "last_name", "date_birth", "id_player"]
        print("\n")
        for element in list_attributes:
            while True:
                data = input(f"{element} : ")
                if cls.validate_input(element, data):
                    dict_inputs[element] = data
                    break
        return dict_inputs

    # Validate inputs user
    @classmethod
    def validate_input(cls, element, data):
        if data:
            if element == "id_player":
                match = re.search(r"[A-Z]{2}[0-9]{5}", data)
                if match:
                    return True
                else:
                    cls.error("Invalid id")
                    return False
            elif element == "date_birth":
                match = re.search(
                    r"(0[1-9]|[12][0-9]|3[01])(\/|-)(0[1-9]|1[1,2])(\/|-)(19|20)\d{2}",
                    data,
                )
                if match:
                    return True
                else:
                    cls.error("Invalid date")
                    return False
            else:
                return True
        else:
            cls.error("Missing input")
            return False

    @classmethod
    def get_id(cls):
        id = input("Type the id player = ")
        return id

    # Print error
    @classmethod
    def error(cls, message):
        print(f"\nError: {message} \n")

    @classmethod
    def info(cls, message):
        print(f"\nInfo: {message} \n")

    @classmethod
    def display_player_list(cls, all_players=None, tournament=None):
        if tournament:
            title = "Players registred  in this tournament"
            list_players = tournament.list_players
        elif all_players:
            title = "List all players"
            list_players = all_players.values()
        else:
            cls.error("No players found")
        sorted_list_players: list[Player] = sorted(
            list_players, key=lambda x: x.first_name.lower()
        )
        rows = []
        for player in sorted_list_players:
            rows.append([player.id_player, player.first_name, player.last_name, player.date_birth])
        print_table(title=title,
                    columns=["id", "first_name", "last_name", "date_birth"],
                    rows=rows)

    @classmethod
    def display_player(cls, player: Player):
        print("\n")
        print_table(title=player.id_player,
                    columns=["first_name", "last_name", "date_birth"],
                    rows=[[player.first_name, player.last_name, player.date_birth]])

    @classmethod
    def display_title_2(cls, message):
        title_2(message)
    
    @classmethod
    def display_title_3(cls, message):
        title_3(message)