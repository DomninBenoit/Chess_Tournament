from models.player import Player
from models.round import Round
from models.match import Match
import random


class Tournament:
    matches = []

    def __init__(self, name, place, date_start, date_end, nb_round=4, player_ids=None, rounds=None) -> None:
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round = nb_round
        self.players = [] if player_ids is None else player_ids
        self.rounds = [] if rounds is None else rounds

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
            return round_name, round_num

    def get_current_round(self):
        if self.rounds:
            return self.rounds[-1]
        else:
            return None

    def generate_pairs(self, round_number):
        if round_number == 1:
            nb_players = len(self.players)
            if nb_players % 2 != 0:
                equilibrage_player = Player("Equilibrage", "", "", "")  # Crée un objet Player pour "Equilibrage"
                self.players.append(equilibrage_player)

            random.shuffle(self.players)


            for i in range(0, nb_players, 2):
                player_a = self.players[i]
                player_b = self.players[i + 1]
                match = Match(player_a, player_b)
                Tournament.matches.append(match)

            current_round = self.get_current_round()
            if current_round:
                for match in Tournament.matches:
                    current_round.add_match(match)
            else:
                print("Le tournoi n'a pas encore commencé.")

            return Tournament.matches
        else:
            print("Le numéro de round spécifié n'est pas valide.")
            return []

    def __str__(self):
        return f"Tournament: {self.name}\n" \
               f"Lieu: {self.place}\n" \
               f"Date début: {self.date_start}\n" \
               f"Date de fin: {self.date_end}\n"


