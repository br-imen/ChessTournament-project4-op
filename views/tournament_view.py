
class TournamentView:
    
    @classmethod
    def get_inputs(cls):
        dict_inputs = {}
        list_inputs = ["name", "place", "description", "number_rounds"]
        for element in list_inputs:
                data = input(f"{element} : ")
                dict_inputs[element] = data      
        return dict_inputs
    