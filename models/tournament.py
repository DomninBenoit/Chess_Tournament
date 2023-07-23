from models.player import Player
from models.round import Round
from models.match import Match
import random

from views.tournament_views import TournamentView


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
        self.scores = {}
        self.current_round = 1

    def __str__(self):
        return f"Tournament: {self.name}\n" \
               f"Lieu: {self.place}\n" \
               f"Date début: {self.date_start}\n" \
               f"Date de fin: {self.date_end}\n"

    # Méthodes pour ajout de joueurs dans un tournoi
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
        round_name = f"Round {self.current_round}"
        round_obj = Round(self.current_round)
        self.rounds.append(round_obj)
        return round_name

    def next_round(self):
        self.current_round += 1
        round_name = f"Round {self.current_round}"
        round_obj = Round(self.current_round)
        self.rounds.append(round_obj)
        return round_name

    def get_current_round(self):
        if self.rounds:
            return self.rounds[-1]
        else:
            return None

    def generate_pairs(self):
        self.matches = []
        nb_players = len(self.players)
        if nb_players % 2 != 0:
            equilibrage_player = Player("Equilibrage", "", "", "")  # Crée un objet Player pour "Equilibrage"
            self.players.append(equilibrage_player)
            self.scores[equilibrage_player] = 0

        if self.current_round == 1:
            random.shuffle(self.players)

            for i in range(0, nb_players, 2):
                player_a = self.players[i]
                player_b = self.players[i + 1]
                match = Match(self.name, player_a, player_b)
                self.matches.append(match)

            current_round = self.get_current_round()
            if current_round:
                for match in self.matches:
                    current_round.add_match(match)
            else:
                print("Le tournoi n'a pas encore commencé.")

            return self.matches
        elif self.current_round > 1:
            sorted_dict = dict(sorted(self.scores.items(), key=lambda item: (item[1], random.random()), reverse=True))
            sorted_players = list(sorted_dict.keys())
            print(sorted_dict)
            for i in range(0, nb_players, 2):
                player_a = sorted_players[i]
                player_b = sorted_players[i + 1]
                match = Match(self.name, player_a, player_b)
                self.matches.append(match)

            current_round = self.get_current_round()
            if current_round:
                for match in self.matches:
                    current_round.add_match(match)

        else:
            print("Le numéro de round spécifié n'est pas valide.")
            return []

    def choice_match_winner(self, choice_match, matches):
        choice_match = int(choice_match)
        match = matches[choice_match - 1]
        choice_winner = TournamentView.display_match_winner(match)
        if choice_winner == "1":
            match.score_a = 1
            self.scores[match.player_a] += 1
        elif choice_winner == "2":
            match.score_b = 1
            self.scores[match.player_b] += 1
        else:
            match.score_a = 0.5
            match.score_b = 0.5
            self.scores[match.player_a] += 0.5
            self.scores[match.player_b] += 0.5

    def round(self, round_name):
        current_round = self.get_current_round()
        if current_round:
            matches = current_round.match_list
            TournamentView.display_list_match_in_round(matches, round_name)
            choice_match = TournamentView.display_match(matches)
            Tournament.choice_match_winner(self, choice_match, matches)

    def display_round(self, round_name):
        current_round = self.get_current_round()
        if current_round:
            Tournament.generate_pairs(self)
            count = len(current_round.match_list)
            while count > 0:
                Tournament.round(self, round_name)
                count -= 1

    @staticmethod
    def get_selected_tournament_index():
        selected_index = TournamentView.display_selected_tournament()
        try:
            return selected_index
        except ValueError:
            TournamentView.display_invalid_input()
            return None

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "nb_round": self.nb_round,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

    @classmethod
    def from_dict(cls, tournament_dict):
        name = tournament_dict["name"]
        place = tournament_dict["place"]
        date_start = tournament_dict["date_start"]
        date_end = tournament_dict["date_end"]
        rounds = [Round.from_dict(round_dict) for round_dict in tournament_dict["rounds"]]
        players = [Player.from_dict(player_dict) for player_dict in tournament_dict["players"]]
        tournament = cls(name, place, date_start, date_end)
        tournament.rounds = rounds
        tournament.players = players
        return tournament


