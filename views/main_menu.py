from views.helpers import title_1


class MainMenu:
    def menu_principal(self):
        title_1("Main Menu")
        option_menu = input(
            "\nChoose an option to do: \n"
            "Type (1) -----> Register a player \n"
            "Type (2) -----> Create a tournament \n"
            "Type (3) -----> Show reports \n"
            "Type (4) -----> Continue a tournament \n"
            "Type (0) -----> Quit \n"
            "Your response: "
        )
        return option_menu
