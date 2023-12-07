class TournamentView:
    @classmethod
    def get_inputs(cls):
        dict_inputs = {}
        list_inputs = ["name", "place", "number_rounds", "description"]
        for element in list_inputs:
            data = input(f"\n{element} : ")
            if element == "number_rounds":
                data = int(data)
            dict_inputs[element] = data
        return dict_inputs
