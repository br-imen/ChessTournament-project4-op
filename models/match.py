# from settings import ABSOLUTE_PATH
# mport json


class Match:
    def __init__(
        self,
        name: str,
        player1_id: str,
        player2_id: str,
        score_player1=0,
        score_player2=0,
    ) -> None:
        self.name: str = name
        self.player1_id: str = player1_id
        self.player2_id: str = player2_id
        self.score_player1: float = score_player1
        self.score_player2: float = score_player2

    def __str__(self) -> str:
        return f"{self.serialize()} "

    def serialize(self) -> tuple:
        return (
            [self.player1_id, self.score_player1],
            [self.player2_id, self.score_player2],
        )


#    def save(self, match_dict: dict):
#        try:
#            with open(f"{ABSOLUTE_PATH}/data/matchs/matchs.json", "r") as match_file:
#                list_matchs = json.load(match_file)
#        except FileNotFoundError:
#            list_matchs = []
#        list_matchs.append(match_dict)
#        with open(f"{ABSOLUTE_PATH}/data/matchs/matchs.json", "w") as match_file:
#            json.dump(list_matchs, match_file)
