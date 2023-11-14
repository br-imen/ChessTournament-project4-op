from models.player import Player



class PlayerController:

    def create_player(player_dict):
        player = Player(**player_dict)
        player.save()
