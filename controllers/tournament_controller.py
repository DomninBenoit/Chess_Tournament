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
            return "start_tournament", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            return "homepage", None

    @classmethod
    def create(cls, store, route_params=None):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        store["tournaments"].append(tournament)

        TournamentView.display_data(store["tournaments"])

        return "tournament_management", None

    # a passer dans models
    @classmethod
    def find_tournament_by_name(cls, store, name):
        for tournament in store["tournaments"]:
            if tournament.name == name:
                return tournament
        return None

    # a passer dans models
    @classmethod
    def register(cls, store, tournament_name, player):
        tournament = cls.find_tournament_by_name(store, tournament_name)
        if tournament is None:
            result = "tournament_not_found"
        if player in tournament.players:
            result = "player_already_registered"
        else:
            tournament.players.append(player)
            result = "player_registered"

        TournamentView.display_registration_result(result)
        return "tournament_management", None

    @classmethod
    def add_player_to_tournament(cls, store, route_params=None):
        tournaments = store["tournaments"]
        TournamentView.display_tournament_list(tournaments)
        if tournaments:
            selected_index = TournamentView.display_selected_tournament()
            if 0 <= selected_index < len(tournaments):
                selected_tournament = tournaments[selected_index]
                cls.add_player(selected_tournament.name, store, route_params)
            else:
                TournamentView.display_invalid_tournament_number()

        return "tournament_management", None

    # a passer dans models
    @classmethod
    def add_player(cls, tournament_name, store, route_params):
        player_id = TournamentView.get_player_id()

        player = None
        for stored_player in store["players"]:
            if stored_player.national_id == player_id:
                player = stored_player
                break

        if player is not None:
            # L'ID du joueur existe, procéder à l'enregistrement
            cls.register(store, tournament_name, player)
            return "tournament_management", None
        else:
            # L'ID du joueur n'existe pas, afficher un message d'erreur
            PlayerView.display_player_not_found()
            return "tournament_management", None

    # a passer dans models
    @classmethod
    def display_data(cls, store, route_params=None):
        TournamentView.display_data(store["tournaments"])

        return "tournament_management", None

    @classmethod
    def list_tournaments(cls, store, route_params=None):
        tournaments = store["tournaments"]
        result = "display_list_tournament"
        TournamentView.display_tournament_list(tournaments, result)
        return tournaments

    @classmethod
    def start_tournament(cls, store, route_params=None):
        tournaments = cls.list_tournaments(store, route_params)
        if tournaments:
            selected_index = Tournament.get_selected_tournament_index()
            if 0 <= selected_index < len(tournaments):
                selected_tournament = tournaments[selected_index]
                for player_id in selected_tournament.players:
                    selected_tournament.scores[player_id] = 0
                TournamentView.display_tournament_to_start(selected_tournament)
                round_name = Tournament.start_tournament(selected_tournament)
                Tournament.display_round(selected_tournament, round_name)
                return "next_round", selected_tournament

    @classmethod
    def next_round(cls, store, selected_tournament):
        rounds_len = len(selected_tournament.rounds)
        nb_round = int(selected_tournament.nb_round)
        if rounds_len < nb_round:
            round_name = Tournament.next_round(selected_tournament)
            Tournament.display_round(selected_tournament, round_name)
            return "next_round", selected_tournament
        else:
            TournamentView.display_round(selected_tournament.rounds)
            TournamentView.display_ranking(selected_tournament)
            return "homepage", None

    @classmethod
    def listing_tournaments(cls, store, route_params=None):
        tournaments = store["tournaments"]
        TournamentView.list_tournaments(tournaments)
        return "homepage", None

    @classmethod
    def list_players_in_tournament(cls, store, route_params=None):
        tournaments = cls.list_tournaments(store, route_params)
        if tournaments:
            selected_index = Tournament.get_selected_tournament_index()
            selected_tournament = tournaments[selected_index]
            players = selected_tournament.players
            PlayerView.list_players(players)
            return "homepage", None

    @classmethod
    def list_round_and_match_in_tournament(cls, store, route_params=None):
        tournaments = cls.list_tournaments(store, route_params)
        if tournaments:
            selected_index = Tournament.get_selected_tournament_index()
            selected_tournament = tournaments[selected_index]
            TournamentView.list_round_in_tournament(selected_tournament.rounds)
            return "homepage", None
