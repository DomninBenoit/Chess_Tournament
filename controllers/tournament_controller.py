from models.tournament import Tournament
from views.tournament_views import TournamentView
from views.player_views import PlayerView


class TournamentController:

    @classmethod
    def list(cls, store, route_params=None):
        choice = TournamentView.display_list()
        if choice == "1":
            return "add_tournament", None
        elif choice == "2":
            return "add_player_in_tournament", None
        elif choice == "3":
            return "delete_tournament", None
        elif choice == "4":
            return "details_tournaments", None
        else:
            return "tournament_management", None

    @classmethod
    def create(cls, store, route_params=None):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        store["tournaments"].append(tournament)

        TournamentView.display_data(store["tournaments"])

        return "tournament_management", None

    @classmethod
    def find_tournament_by_name(cls, store, name):
        for tournament in store["tournaments"]:
            if tournament.name == name:
                return tournament
        return None

    @classmethod
    def register(cls, store, tournament_name, player_id):
        tournament = cls.find_tournament_by_name(store, tournament_name)
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
    def list_tournaments(cls, store, route_params=None):
        tournaments = store["tournaments"]
        if tournaments:
            result = "display_list_tournament"
            TournamentView.display_tournament_list(tournaments, result)
            selected_index = TournamentView.display_selected_tournament()
            try:
                selected_index = int(selected_index) - 1
                if 0 <= selected_index < len(tournaments):
                    selected_tournament = tournaments[selected_index]
                    cls.add_player_to_tournament(selected_tournament.name, store, route_params)
                else:
                    TournamentView.display_invalid_tournament_number()
            except ValueError:
                TournamentView.display_invalid_input()

        else:
            result = "tournament_not_found"
            TournamentView.display_tournament_list(cls.tournaments, result)
        return "tournament_management", None

    @classmethod
    def add_player_to_tournament(cls, tournament_name, store, route_params):
        player_id = TournamentView.get_player_id()

        player_exists = any(player.national_id == player_id for player in store["players"])

        if player_exists:
            # L'ID du joueur existe, procéder à l'enregistrement
            cls.register(store, tournament_name, player_id)
            return "tournament_management", None
        else:
            # L'ID du joueur n'existe pas, afficher un message d'erreur
            PlayerView.display_player_not_found()
            return "tournament_management", None

    @classmethod
    def display_data(cls, store, route_params=None):
        TournamentView.display_data(store["tournaments"])

        return "tournament_management", None
