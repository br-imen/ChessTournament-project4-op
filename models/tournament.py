# from settings import ABSOLUTE_PATH
from datetime import datetime
import uuid

# import json
from .player import Player
from .round import Round


class Tournament:
    def __init__(
        self,
        name: str,
        place: str,
        description: str,
        list_players: list[Player] = None,
        end_datetime: datetime = None,
        list_rounds: list[Round] = None,
        number_rounds: int = 4,
        start_datetime=None,
        id: str = None,
    ):
        if list_players is None:
            list_players = []
        if list_rounds is None:
            list_rounds = []
        self.id = str(uuid.uuid4()) if id is None else id
        self.name: str = name
        self.place: str = place
        self.start_datetime = (
            datetime.now() if start_datetime is None else start_datetime
        )
        self.end_datetime = end_datetime
        self.number_rounds: int = number_rounds
        self.list_rounds: list[Round] = list_rounds
        self.list_players: list[Player] = list_players
        self.description: str = description

    def __str__(self) -> str:
        return f"{self.serialize()}"

    # Add player object to list_players
    def add_player(self, player: Player):
        self.list_players.append(player)

    # Add round object to list_rounds
    def add_round(self, round: Round):
        self.list_rounds.append(round)

    @property
    def total_score(self):
        dict_total_score = {}
        for round in self.list_rounds:
            for match in round.list_matchs:
                if match.player1_id in dict_total_score:
                    dict_total_score[match.player1_id] += match.score_player1
                else:
                    dict_total_score[match.player1_id] = match.score_player1
                if match.player2_id in dict_total_score:
                    dict_total_score[match.player2_id] += match.score_player2
                else:
                    dict_total_score[match.player2_id] = match.score_player2
        return dict_total_score

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "start_datetime": self.start_datetime.isoformat(timespec="minutes"),
            "end_datetime": self.end_datetime.isoformat(timespec="minutes")
            if self.end_datetime
            else "",
            "number_rounds": self.number_rounds,
            "list_rounds": [r.serialize() for r in self.list_rounds],
            "list_players": [p.serialize() for p in self.list_players],
            "description": self.description,
        }

    @classmethod
    def deserialize(cls, dict_tournament):
        list_players = []
        for dict_player in dict_tournament["list_players"]:
            list_players.append(Player.deserialize(dict_player))

        list_rounds = []
        for dict_round in dict_tournament["list_rounds"]:
            list_rounds.append(Round.deserialize(dict_round))
        tournament = Tournament(
            id=dict_tournament["id"],
            name=dict_tournament["name"],
            place=dict_tournament["place"],
            start_datetime=datetime.fromisoformat(dict_tournament["start_datetime"]),
            end_datetime=datetime.fromisoformat(dict_tournament["end_datetime"])
            if dict_tournament["end_datetime"]
            else None,
            number_rounds=dict_tournament["number_rounds"],
            list_rounds=list_rounds,
            list_players=list_players,
            description=dict_tournament["description"],
        )
        return tournament

    @classmethod
    def deserialize_all_tournaments(cls, dict_all_tournaments):
        dict_all_tournaments_objects = {}
        for key, value in dict_all_tournaments.items():
            tournament_object = cls.deserialize(value)
            dict_all_tournaments_objects[key] = tournament_object
        return dict_all_tournaments_objects

    def end_tournament(self):
        self.end_datetime = datetime.now()
