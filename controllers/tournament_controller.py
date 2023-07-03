import json
import os
from models.tournament import Tournament
from views.tournament_views import TournamentView


class TournamentController:
    tournaments = []

    @classmethod
    def list(cls, route_params=None):
        choice = TournamentView.display_list()
        if choice == "1":
            return "add_tournament"
        elif choice == "2":
            return "add_player_in_tournament"
        elif choice == "3":
            return "delete_tournament"

    @classmethod
    def create(cls):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        if os.path.getsize('data/tournaments.json') == 0:
            cls.tournaments.append(tournament)
            cls.save_tournaments()
        else:
            cls.load_tournaments()
            cls.tournaments.append(tournament)
            cls.save_tournaments()

        return "tournament_management"

    # @classmethod
    # def delete(cls):

    @classmethod
    def find_tournament_by_name(cls, tournaments, name):
        for tournament in tournaments:
            if tournament.name == name:
                return tournament
        return None

    @classmethod
    def register(cls, tournament_name, player_id):
        # Charger les tournois à partir du fichier JSON
        tournaments = cls.load_tournaments()

        tournament = cls.find_tournament_by_name(tournaments, tournament_name)
        if tournament is None:
            result = "tournament_not_found"
        if player_id in tournament.players:
            result = "player_already_registered"
        tournament.players.append(player_id)
        cls.save_tournaments()
        result = "player_registered"

        TournamentView.display_registration_result(result)

    @classmethod
    def load_tournaments(cls):
        with open('data/tournaments.json', 'r') as f:
            tournaments_json = json.load(f)

        cls.tournaments = []
        for tournament_data in tournaments_json:
            tournament = Tournament(
                tournament_data['name'],
                tournament_data['place'],
                tournament_data['date_start'],
                tournament_data['date_end'],
                tournament_data['nb_round']
            )
            tournament.players = tournament_data['players']
            tournament.rounds = tournament_data['rounds']
            cls.tournaments.append(tournament)

        return cls.tournaments

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

        with open('data/tournaments.json', 'w') as f:
            json.dump(tournaments_json, f)

    @classmethod
    def list_tournaments(cls):
        cls.load_tournaments()
        if cls.tournaments:
            result = "display_list_tournament"
            TournamentView.display_tournament_list(cls.tournaments, result)
            selected_index = TournamentView.display_selected_tournament()
            try:
                selected_index = int(selected_index) - 1
                if 0 <= selected_index < len(cls.tournaments):
                    selected_tournament = cls.tournaments[selected_index]
                    cls.add_player_to_tournament(selected_tournament.name)
                else:
                    TournamentView.display_invalid_tournament_number()
            except ValueError:
                TournamentView.display_invalid_input()
        else:
            result = "tournament_not_found"
            TournamentView.display_tournament_list(cls.tournaments, result)

    @classmethod
    def selected_tournament(cls, tournaments):
        # demande choix tournoi
        selected_index = input("Sélection du tournoi (entrez le numéro) :")
        try:
            selected_index = int(selected_index) - 1
            if 0 <= selected_index < len(tournaments):
                selected_tournament = tournaments[selected_index]
                cls.add_player_to_tournament(selected_tournament.name)
            else:
                print("Numéro de tournoi invalide")
        except ValueError:
            print("entrée invalide")

    @classmethod
    def add_player_to_tournament(cls, tournament_name):
        player_id = TournamentView.get_player_id()
        cls.register(tournament_name, player_id)

