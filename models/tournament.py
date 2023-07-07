from models.round import Round


class Tournament:

    def __init__(self, name, place, date_start, date_end, nb_round=4) -> None:
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.players = []
        self.rounds = []

    # Méthodes pour ajout et suppression de joueurs dans un tournoi
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
        else:
            print("Le joueur est déjà inscrit au tournoi.")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            print("Le joueur n'est pas inscrit au tournoi.")

    # Méthodes pour gérer les tours
    def start_tournament(self):
        for round_num in range(1, self.nb_round + 1):
            round_name = f"Round {round_num}"
            round_obj = Round(round_name)
            self.rounds.append(round_obj)

    def get_current_round(self):
        if self.rounds:
            return self.rounds[-1]
        else:
            return None

    def advance_to_next_round(self):
        if self.rounds:
            current_round = self.get_current_round()
            if current_round.is_completed():
                next_round_num = current_round.round_number + 1
                if next_round_num <= self.nb_round:
                    round_name = f"Round {next_round_num}"
                    next_round = Round(round_name)
                    self.rounds.append(next_round)
                else:
                    print("Le tournoi est terminé.")
            else:
                print("Le tour actuel n'est pas encore terminé.")
        else:
            print("Le tournoi n'a pas encore commencé.")

    # getter et setter
    def get_name(self):
        return self.name

    def get_place(self):
        return self.place

    def get_date_start(self):
        return self.date_start

    def get_date_end(self):
        return self.date_end

    def get_nb_round(self):
        return self.nb_round

    def get_players(self):
        return self.players

    def get_rounds(self):
        return self.rounds

    def set_name(self, name):
        self.name = name

    def set_place(self, place):
        self.place = place

    def set_date_start(self, date_start):
        self.date_start = date_start

    def set_date_end(self, date_end):
        self.date_end = date_end

    def set_nb_round(self, nb_round):
        self.nb_round = nb_round
