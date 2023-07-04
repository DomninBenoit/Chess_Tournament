import json
import os
from models.tournament import Tournament
from views.tournament_views import TournamentView
from views.player_views import PlayerView
from data.json_utils import TournamentJson, PlayersJson


class TournamentController:
    tournaments = []

    @classmethod
    def list(cls, route_params=None):
        choice = TournamentView.display_list()
        if choice == "1":
            return "add_tournament", None
        elif choice == "2":
            return "add_player_in_tournament", None
        elif choice == "3":
            return "delete_tournament", None
        else:
            return "tournament_management", None

    @classmethod
    def create(cls, route_params=None):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        if os.path.getsize('data/tournaments.json') == 0:
            cls.tournaments.append(tournament)
            TournamentJson.save_tournaments(cls.tournaments)
        else:
            TournamentJson.load_tournaments()
            cls.tournaments.append(tournament)
            TournamentJson.save_tournaments(cls.tournaments)

        return "tournament_management", None

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
        cls.tournaments = TournamentJson.load_tournaments()

        tournament = cls.find_tournament_by_name(cls.tournaments, tournament_name)
        if tournament is None:
            result = "tournament_not_found"
        if player_id in tournament.players:
            result = "player_already_registered"
        else:
            tournament.players.append(player_id)
            TournamentJson.save_tournaments(cls.tournaments)
            result = "player_registered"

        TournamentView.display_registration_result(result)

    @classmethod
    def list_tournaments(cls, route_params=None):
        cls.tournaments = TournamentJson.load_tournaments()
        if cls.tournaments:
            result = "display_list_tournament"
            TournamentView.display_tournament_list(cls.tournaments, result)
            selected_index = TournamentView.display_selected_tournament()
            try:
                selected_index = int(selected_index) - 1
                if 0 <= selected_index < len(cls.tournaments):
                    selected_tournament = cls.tournaments[selected_index]
                    cls.add_player_to_tournament(selected_tournament.name, route_params)
                else:
                    TournamentView.display_invalid_tournament_number()
            except ValueError:
                TournamentView.display_invalid_input()

        else:
            result = "tournament_not_found"
            TournamentView.display_tournament_list(cls.tournaments, result)
        return "tournament_management", None

    @classmethod
    def add_player_to_tournament(cls, tournament_name, route_params):
        player_id = TournamentView.get_player_id()
        players = PlayersJson.load_players()

        player_exists = any(player.national_id == player_id for player in players)

        if player_exists:
            # L'ID du joueur existe, procéder à l'enregistrement
            cls.register(tournament_name, player_id)
            return "tournament_management", None
        else:
            # L'ID du joueur n'existe pas, afficher un message d'erreur
            PlayerView.display_player_not_found()
            return "tournament_management", None
