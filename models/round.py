from settings import ABSOLUTE_PATH
from datetime import datetime
import uuid
import json


class Round:
    
    def __init__(self, name, tournament_id, end_datetime) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.tournament_id = tournament_id
        self.start_datetime = datetime.now().isoformat(timespec='minutes') 
        self.end_datetime = end_datetime


    def __str__(self) -> str:
        return f"name : {self.name}"
    

    def save(self):

        round_dict = {
            "id" : self.id,
            "name" : self.name,
            "tounament_id" : self.tournament_id,
            "start_datetime" : self.start_datetime,
            "end_datetime" : self.end_datetime,
            "matchs": [(["player1", 1], ["player2", 0]), (["player3", 0.5], ["player4", 0.5])]
        }

        try:
            with open(f"{ABSOLUTE_PATH}/data/rounds/rounds.json", "r") as round_file:
                list_rounds = json.load(round_file)
        except FileNotFoundError:
            list_rounds = []
        list_rounds.append(round_dict)
        with open(f"{ABSOLUTE_PATH}/data/rounds/rounds.json", "w") as round_file:
            json.dump(list_rounds, round_file)
