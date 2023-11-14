from models.player import Player
from models.tournament import Tournament
from views.player_view import PlayerView
from views.options import Options
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
import os
from settings import ABSOLUTE_PATH



# To create a data folder
def create_data_folder():
    data_path = f"{ABSOLUTE_PATH}/data"
    player_path = f"{data_path}/players"
    match_path = f"{data_path}/matchs"
    round_path = f"{data_path}/rounds"
    tournament_path = f"{data_path}/tournaments"
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    if not os.path.exists(player_path):
        os.makedirs(player_path)
    if not os.path.exists(match_path):
        os.makedirs(match_path)
    if not os.path.exists(round_path):
        os.makedirs(round_path)
    if not os.path.exists(tournament_path):
        os.makedirs(tournament_path)



def main():
    MainController().start()
    create_data_folder()
    while True:
        # View : Options to choose 
        option = Options.choose()

        # To register player
        if option == "1":

            # Model : Get list of attributes from class Player
            list_inputs = Player.get_attributes()

            # View: print out for player inputs
            player_dict = PlayerView.get_inputs(list_inputs)

            # Controller: create player and save in json file
            PlayerController.create_player(player_dict)

            print("Player successfully registred !")
            pass

        # To create tournament
        if option == "2":

            # Get inputs of trounament
            tournament_dict = TournamentView.get_inputs()

            # instantiate a tournament 
            tournament = Tournament(**tournament_dict)

            # save it in json file
            tournament.save()

            print("Tournament successfully created !")
             
            



        



if __name__ == "__main__":
    main()
