from models.player import Player

class Match:

    def __init__(self, player_a, player_b) -> None:
        self.player_a = player_a
        self.player_b = player_b
        self.score_a = 0
        self.score_b = 0

    def __str__(self):
        return f"Match:\n" \
               f"Player A: {self.player_a}\n" \
               f"Player B: {self.player_b}\n" \
               f"Score A: {self.score_a}\n" \
               f"Score B: {self.score_b}"

    def to_dict(self):
        return {
            "player_a": self.player_a.national_id,
            "player_b": self.player_b.national_id,
            "score_a": self.score_a,
            "score_b": self.score_b,
        }

    @classmethod
    def from_dict(cls, match_dict, players_dict):
        player_a_national_id = match_dict["player_a"]
        player_b_national_id = match_dict["player_b"]

        player_a = players_dict[player_a_national_id]
        player_b = players_dict[player_b_national_id]

        score_a = match_dict["score_a"]
        score_b = match_dict["score_b"]
        match = cls(player_a, player_b)
        match.score_a = score_a
        match.score_b = score_b
        return match
