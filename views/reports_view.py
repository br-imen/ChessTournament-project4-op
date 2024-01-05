from views.helpers import title_2


class ReportsView:
    def __init__(self) -> None:
        """Report view"""
        pass

    def get_reports(self):
        print("\n")
        response = input(
            "\n  Choose an option to do\n"
            "   Type (1) -----> List of players of this tournament \n"
            "   Type (2) -----> List of rounds and matchs for this tournament \n"
            "   Type (0) -----> Go back \n"
            "   Your response: "
        )
        return response

    def report_menu(self):
        print("\n\n")
        response = input(
            "Type (1) ----> List of all players \n"
            "Type (2) ----> See reports for one tournament \n"
            "Type (0) ----> Go back \n"
            "Your response: "
        )
        return response

    def report_tournament_menu(self):
        response = input("\n Type the (Id) of the tournament \n" "Your response: ")
        return response

    def display_title(self):
        title_2("Show Reports")
