# from settings import ABSOLUTE_PATH
from datetime import datetime
from .match import Match


class Round:
    def __init__(
        self,
        name: str,
        list_matchs: list[Match],
        start_datetime=None,
        end_datetime: datetime = None,
    ) -> None:
        self.name: str = name
        self.start_datetime = (
            datetime.now() if start_datetime is None else start_datetime
        )
        self.end_datetime = end_datetime
        self.list_matchs: list[Match] = list_matchs

    def __str__(self) -> str:
        return f"{self.serialize()}"

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "start_datetime": self.start_datetime.isoformat(timespec="minutes"),
            "end_datetime": self.end_datetime.isoformat(timespec="minutes")
            if self.end_datetime
            else "",
            "matchs": [m.serialize() for m in self.list_matchs],
        }

    @classmethod
    def deserialize(cls, dict_round):
        list_matchs = []
        i = 1
        for tuple_match in dict_round["matchs"]:
            list_matchs.append(
                Match(
                    name=f"match{i}",
                    player1_id=tuple_match[0][0],
                    player2_id=tuple_match[1][0],
                    score_player1=tuple_match[0][1],
                    score_player2=tuple_match[1][1],
                )
            )
            i += 1
        round = cls(
            name=dict_round["name"],
            start_datetime=datetime.fromisoformat(dict_round["start_datetime"]),
            end_datetime=datetime.fromisoformat(dict_round["end_datetime"])
            if dict_round["end_datetime"]
            else dict_round["end_datetime"],
            list_matchs=list_matchs,
        )
        return round

    def add_match(self, match: Match):
        self.list_matchs.append(match)

    def end(self):
        self.end_datetime = datetime.now()
