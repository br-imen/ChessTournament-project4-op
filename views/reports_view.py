class ReportsView:
    @classmethod
    def get_reports(cls):
        response = input(
            "\nChoose an option to do\n"
            # "Type (1) -----> To show all players \n"
            "Type (1) -----> List of all players of tournament \n"
            "Type (2) -----> List of all rounds and matchs of tournament \n"
            "Type (3) -----> To go back \n"
            "Your response: "
        )
        return response

    @classmethod
    def choose_report(cls):
        response = input(
            "Type (1) ----> To see list of all players \nType (2) ----> To see reports for a tournament \nType (3) ----> To go back \n"
            "Your response: "
        )
        return response

    @classmethod
    def report_tournament(cls):
        response = input(
            "\n Type the (Id) of the tournament \n" "Your response: "
        )
        return response
