from settings import ABSOLUTE_PATH
import uuid
import json



class Match:

    def __init__(self, name, tournament_id, round_id, player1_id, player2_id, score_player1=0, score_player2=0) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.tournament_id = tournament_id
        self.round_id = round_id
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.score_player1 = score_player1
        self.score_player2 = score_player2

    def __str__(self) -> str:
        return f"name : {self.name} "
    
    def save(self):
        match_dict = {
            "id": self.id,
            "name": self.name,
            "tournament_id" : self.tournament_id,
            "round_id": self.round_id,
            "player1_id": self.player1_id,
            "player2_id": self.player2_id,
            "score_player1": self.score_player1,
            "score_player2": self.score_player2
        }
        try:
            with open(f"{ABSOLUTE_PATH}/data/matchs/matchs.json", "r") as match_file:
                list_matchs = json.load(match_file)
        except FileNotFoundError:
            list_matchs = []
        list_matchs.append(match_dict)
        with open(f"{ABSOLUTE_PATH}/data/matchs/matchs.json", "w") as match_file:
            json.dump(list_matchs, match_file)
