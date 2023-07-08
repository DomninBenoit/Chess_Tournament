from models.round import Round
from models.match import Match
import random


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

    @classmethod
    def generate_pairs(cls, tournaments_players, round):
        nb_players = len(tournaments_players)

        if nb_players % 2 != 0:
            tournaments_players.append("Equilibrage")

        if round == 1:
            random.shuffle(tournaments_players)

            pairs = []
            for i in range(0, nb_players, 2):
                player_a = tournaments_players[i]
                player_b = tournaments_players[i + 1]
                match = Match(player_a, player_b)
                pairs.append(match)

            tournaments_players.add_match_to_round(round, pairs)

            return pairs

    def __str__(self):
        return f"Tournament: {self.name}\n" \
               f"Lieu: {self.place}\n" \
               f"Date début: {self.date_start}\n" \
               f"Date de fin: {self.date_end}\n"
