class Tournament:

    def __init__(self, name, place, date_start, date_end, nb_round=4) -> None:
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.players = []
        self.rounds = []
