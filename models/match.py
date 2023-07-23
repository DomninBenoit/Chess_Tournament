class Match:

    def __init__(self, tournament_name, player_a, player_b) -> None:
        self.tournament_name = tournament_name
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
