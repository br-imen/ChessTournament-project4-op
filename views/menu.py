class Menu:
    def menu_principal(self):
        print(
            "\n\n"
            f"{' '*10}"
            "********************************** \n"
            f"{' '*10}"
            "***          Main Menu         *** \n"
            f"{' '*10}"
            "********************************** \n"
        )
        option_menu = input(
            "\nChoose an option to do: \nType (1) -----> to register a player \nType (2) -----> to create a tournament \nType (3) -----> show reports \nType (4) -----> To continue a tournament \nYour response: "
        )
        return option_menu
