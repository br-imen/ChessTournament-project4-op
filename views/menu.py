class Menu:
    def menu_principal(self):
        option_menu = input(
            "\nChoose an option to do: \nType (1) -----> to register a player \nType (2) -----> to create a tournament \nType (3) -----> show reports \nType (4) -----> To continue a tournament \nYour response: "
        )
        return option_menu

    def menu_start_round(self):
        option_start_round = input(
            "\nChoose an option to do : \nType (1) -----> to add a player in tournament \nType (2) -----> to start a round \nYour response: "
        )
        return option_start_round

    def menu_another_round(self):
        option_another_round = input(
            "\nType (2) to start another round \nYour response: "
        )
        return option_another_round
