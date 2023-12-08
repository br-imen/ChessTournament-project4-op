# from settings import ABSOLUTE_PATH
from datetime import datetime
from .match import Match

# import uuid
# import json


class Round:
    def __init__(
        self, name: str, list_matchs: list[Match],
        start_datetime = None, 
        end_datetime: datetime = None
    ) -> None:
        # self.id = str(uuid.uuid4())
        self.name: str = name
        # self.tournament_id = tournament_id
        self.start_datetime = datetime.now().isoformat(timespec="minutes") if start_datetime is None else start_datetime
        self.end_datetime = end_datetime
        self.list_matchs: list[Match] = list_matchs

    def __str__(self) -> str:
        return f"{self.serialize()}"

    def serialize(self) -> dict:
        import pdb; pdb.set_trace()
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime.isoformat(timespec="minutes"),
            "matchs": [m.serialize() for m in self.list_matchs],
        }

    @classmethod
    def deserialize(cls, dict_round):
        list_matchs = []
        i=1
        for tuple_match in dict_round['matchs']:
            list_matchs.append(Match(name=f'match{i}', 
                                        player1_id=tuple_match[0][0],
                                        player2_id=tuple_match[1][0],
                                        score_player1=tuple_match[0][1],
                                        score_player2=tuple_match[1][1]))
            i+=1
        round = cls(name=dict_round['name'],
                    start_datetime=datetime.fromisoformat(dict_round['start_datetime']),
                    end_datetime=datetime.fromisoformat(dict_round['end_datetime']) if dict_round['end_datetime'] else dict_round['end_datetime'] ,
                    list_matchs=list_matchs)
        return round





    def add_match(self, match: Match):
        self.list_matchs.append(match)

    def end_round(self):
        import pdb; pdb.set_trace()
        self.end_datetime = datetime.now()


#    def save(self,round_dict: dict):
#        try:
#            with open(f"{ABSOLUTE_PATH}/data/rounds/rounds.json", "r") as round_file:
#                list_rounds = json.load(round_file)
#        except FileNotFoundError:
#            list_rounds = []
#        list_rounds.append(round_dict)
#        with open(f"{ABSOLUTE_PATH}/data/rounds/rounds.json", "w") as round_file:
#            json.dump(list_rounds, round_file)
