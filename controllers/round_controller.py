

from models.match import Match
from models.round import Round
from models.tournament import Tournament
from views.match_view import MatchView
from views.round_view import RoundView


class RoundController:

    def __init__(self) -> None:
        pass

    # Start round
    def start_round(self, tournament: Tournament):
        if tournament.list_rounds is None:
            number_rounds = 0
        else:
            number_rounds = len(tournament.list_rounds)

        if number_rounds < tournament.number_rounds:
            # To create a round
            round = self.create_round(tournament=tournament)

            # Add it to list_round in tournament object
            tournament.add_round(round)

            RoundView.display_round(round)
            return round  

    # To create round
    def create_round(self, tournament):
        list_matchs = []
        list_players = tournament.list_players
        r = len(tournament.list_rounds)
        number_match = 1

        # There is previous rounds
        if r >= 1:
            # Create a list player filtered by score:
            sorted_list_total_scores: list[tuple()] = sorted(
                tournament.total_score.items(),
                key=lambda x: x[1],
                reverse=True,
            )

            # Create a list of Matchs
            for i in range(0, len(sorted_list_total_scores), 2):
                match = Match(
                    name=f"match{number_match}",
                    player1_id=sorted_list_total_scores[i][0],
                    player2_id=sorted_list_total_scores[i + 1][0],
                )
                list_matchs.append(match)
                number_match += 1

        # The first round
        else:
            # Create a list of Matchs
            for i in range(0, len(list_players), 2):
                match = Match(
                    name=f"match{number_match}",
                    player1_id=list_players[i].id_player,
                    player2_id=list_players[i + 1].id_player,
                )
                list_matchs.append(match)
                number_match += 1

        # Create a round
        round = Round(name=f"round{r+1}", list_matchs=list_matchs)

        return round
    
    # To end round:
    def end_round(self, round: Round, tournament:Tournament):
        # Get number of rounds have been done
        number_rounds = len(tournament.list_rounds)

        # If number of rounds have been done is equal or exceed the number of total rounds in tournament object, we end the round and the tournamment.
        if number_rounds >= tournament.number_rounds:
            round.end_round()
            tournament.end_tournament()
            self.save()
            MatchView.display_match(total_score=tournament.total_score)
            return

        # There is more rounds to finish, we end only the round
        else:
            round.end_round()
            self.save()
            return

    # From start a round to the end round  
    def run_round(self, tournament):
        if not tournament.list_players:
            # Round view error missing players error
            RoundView.error(
                "You can't start round there is no players registred in the tournament"
            )
            pass
        elif len(tournament.list_players) % 2 != 0:
            # roundview info
            RoundView.info("Add another player.")
        else:
            round = self.start_round(tournament=tournament)
            for match in round.list_matchs:

                # Get points of two players
                points_players: tuple(str) = MatchView.get_score_player(match)

                # Update the score in match:
                match.score_player1 = points_players[0]
                match.score_player2 = points_players[1]
                MatchView.display_match(match=match, updated=True)

            self.end_round(round=round, tournament=tournament)

            if len(tournament.list_rounds) == tournament.number_rounds:
                return

