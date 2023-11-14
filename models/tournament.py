from settings import ABSOLUTE_PATH
from datetime import datetime
import uuid
import json

class Tournament:

    def __init__(self, name, place, description, list_players = None, end_datetime = None, actual_round = None, list_rounds = None, number_rounds = 4):
        self.id = str(uuid.uuid4())
        self.name = name
        self.place = place
        self.start_datetime = datetime.now().isoformat(timespec='minutes')
        self.end_datetime = end_datetime
        self.number_rounds = number_rounds
        self.actual_round = actual_round
        self.list_rounds = list_rounds
        self.list_players = list_players
        self.description = description


    def __str__(self) -> str:
        return f"name = {self.name}"
    

    # Save tournament
    def save(self):
        tournament_dict = {
            "id" : self.id,
            "name" : self.name,
            "place" : self.place,
            "start_datetime" : self.start_datetime,
            "end_datetime" : self.end_datetime,
            "number_rounds" : self.number_rounds,
            "actual_round" : self.actual_round,
            "list_rounds" : self.list_rounds, 
            "list_players" : self.list_players,
            "description" : self.description
        }
        try:
            with open(f"{ABSOLUTE_PATH}/data/tournaments/tournaments.json", "r") as tournament_file:
                list_tournaments = json.load(tournament_file)
        except FileNotFoundError:
            list_tournaments = []
        list_tournaments.append(tournament_dict)
        with open(f"{ABSOLUTE_PATH}/data/tournaments/tournaments.json", "w") as tournament_file:
            json.dump(list_tournaments, tournament_file)


