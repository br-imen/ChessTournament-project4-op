class ReportsView:
    @classmethod
    def get_reports(cls):
        print("\n")
        response = input(
            "\n  Choose an option to do\n"
            # "Type (1) -----> To show all players \n"
            "   Type (1) -----> List of all players of tournament \n"
            "   Type (2) -----> List of all rounds and matchs of tournament \n"
            "   Type (0) -----> To go back \n"
            "   Your response: "
        )
        return response

    @classmethod
    def report_menu(cls):
        print("\n\n")
        response = input(
            "Type (1) ----> To see list of all players \nType (2) ----> To see reports for a tournament \nType (0) ----> To go back \n"
            "Your response: "
        )
        return response

    @classmethod
    def report_tournament_menu(cls):
        response = input("\n Type the (Id) of the tournament \n" "Your response: ")
        return response
