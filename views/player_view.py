import re

from models.player import Player
from views.helpers import print_table, title_2, title_3


class PlayerView:
    # Function: gets attributes of class and returns a dict of inputs of user.
    def get_inputs(self):
        dict_inputs = {}
        list_attributes = ["first_name", "last_name", "date_birth", "id_player"]
        print("\n")
        for element in list_attributes:
            while True:
                data = input(f"{element} : ")
                if self.validate_input(element, data):
                    dict_inputs[element] = data
                    break
        return dict_inputs

    # Validate inputs user
    def validate_input(self, element, data):
        if data:
            if element == "id_player":
                match = re.search(r"[A-Z]{2}[0-9]{5}", data)
                if match:
                    return True
                else:
                    self.error("Invalid id")
                    return False
            elif element == "date_birth":
                match = re.search(
                    r"^[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}$",
                    data,
                )
                if match:
                    return True
                else:
                    self.error("Invalid date")
                    return False
            else:
                return True
        else:
            self.error("Missing input")
            return False

    def get_id(self):
        id = input("\nType the id player = ")
        return id

    # Print error
    def error(self, message):
        print(f"\nError: {message} \n")

    def error_player_exist(self):
        return self.error("Player exist ! Please enter inputs again")

    def error_no_players(self):
        return self.error("No players")

    def info(self, message):
        print(f"\nInfo: {message} \n")

    def info_player_registred(self):
        return self.info("Player registred\n")

    def display_player_list(self, all_players=None, tournament=None):
        if tournament:
            title = "Players registred  in this tournament"
            list_players = tournament.list_players
        elif all_players:
            title = "List all players"
            list_players = all_players.values()
        else:
            self.error("No players found")
        sorted_list_players: list[Player] = sorted(
            list_players, key=lambda x: x.first_name.lower()
        )
        rows = []
        for player in sorted_list_players:
            rows.append(
                [
                    player.id_player,
                    player.first_name,
                    player.last_name,
                    player.date_birth,
                ]
            )
        print_table(
            title=title,
            columns=["id", "first_name", "last_name", "date_birth"],
            rows=rows,
        )

    def display_player(self, player: Player):
        print("\n")
        print_table(
            title=player.id_player,
            columns=["first_name", "last_name", "date_birth"],
            rows=[[player.first_name, player.last_name, player.date_birth]],
        )

    def display_title_2(self, message):
        title_2(message)

    def display_register_player(self):
        return self.display_title_2("Register Player")

    def display_title_3(self, message):
        title_3(message)

    def display_all_players(self):
        return self.display_title_3("All Players")
