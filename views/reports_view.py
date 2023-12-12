from views.helpers import title_2


class ReportsView:
    @classmethod
    def get_reports(cls):
        print("\n")
        response = input(
            "\n  Choose an option to do\n"
            "   Type (1) -----> List of players of this tournament \n"
            "   Type (2) -----> List of rounds and matchs of this tournament \n"
            "   Type (0) -----> Go back \n"
            "   Your response: "
        )
        return response

    @classmethod
    def report_menu(cls):
        print("\n\n")
        response = input(
            "Type (1) ----> List of all players \n"
            "Type (2) ----> See reports for one tournament \n"
            "Type (0) ----> Go back \n"
            "Your response: "
        )
        return response

    @classmethod
    def report_tournament_menu(cls):
        response = input("\n Type the (Id) of the tournament \n" "Your response: ")
        return response
    
    @classmethod
    def display_title(cls):
        title_2("Show Reports")
