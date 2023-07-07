from models.tournament import Tournament
from views.tournament_views import TournamentView
from views.player_views import PlayerView


class TournamentController:
    tournaments = []

    @classmethod
    def list(cls, store, route_params=None):
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
    def create(cls, store, route_params=None):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        cls.tournaments.append(tournament)
        TournamentView.display_data(cls.tournaments)

        return "tournament_management", None

    @classmethod
    def delete(cls, store, route_params=None):
        tournament_name = TournamentView.get_tournament_name()
        tournament_found = False
        for tournament in cls.tournaments:
            if tournament.name == tournament_name:
                cls.tournaments.remove(tournament)
                tournament_found = True
                break
        if tournament_found:
            result = "tournament_delete"
        else:
            result = "tournament_not_found"
        TournamentView.display_delete_result(result)

        return "tournament_management", None

    @classmethod
    def find_tournament_by_name(cls, name):
        for tournament in cls.tournaments:
            if tournament.name == name:
                return tournament
        return None

    @classmethod
    def register(cls, tournament_name, player_id):
        tournament = cls.find_tournament_by_name(tournament_name)
        if tournament is None:
            result = "tournament_not_found"
        if player_id in tournament.players:
            result = "player_already_registered"
        else:
            tournament.players.append(player_id)
            result = "player_registered"

        TournamentView.display_registration_result(result)
        return "tournament_management", None

    @classmethod
    def list_tournaments(cls, route_params=None):
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

        player_exists = any(player.national_id == player_id for player in cls.players)

        if player_exists:
            # L'ID du joueur existe, procéder à l'enregistrement
            cls.register(tournament_name, player_id)
            return "tournament_management", None
        else:
            # L'ID du joueur n'existe pas, afficher un message d'erreur
            PlayerView.display_player_not_found()
            return "tournament_management", None

    @classmethod
    def display_data(cls):
        TournamentView.display_data(cls.tournaments)
