import json
from models.tournament import Tournament


class TournamentController:
    tournaments = []

    @classmethod
    def create(cls, name, place, date_start, date_end, nb_round=4):
        tournament = Tournament(name, place, date_start, date_end, nb_round)
        cls.tournaments.append(tournament)
        cls.save_tournaments()

    @classmethod
    def save_tournaments(cls):
        tournaments_json = []
        for tournament in cls.tournaments:
            tournament_data = {
                'name': tournament.name,
                'place': tournament.place,
                'date_start': tournament.date_start,
                'date_end': tournament.date_end,
                'nb_round': tournament.nb_round,
                'players': tournament.players,
                'rounds': tournament.rounds
            }
            tournaments_json.append(tournament_data)

        # Charger les tournoi existants depuis le fichier JSON
        existing_tournaments = []
        try:
            with open('data/tournaments.json', 'r') as f:
                existing_tournaments = json.load(f)
        except FileNotFoundError:
            pass

        # Ajouter le nouveau tournoi à la liste existante
        existing_tournaments.extend(tournaments_json)

        with open('data/tournaments.json', 'w') as f:
            json.dump(existing_tournaments, f)
