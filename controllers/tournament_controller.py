from datetime import datetime

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
        elif choice == "5":
            return "start_tournament", None
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
        tournaments = cls.list_tournaments(store, route_params)
        if tournaments:
            selected_index = cls.get_selected_tournament_index()
            if 0 <= selected_index < len(tournaments):
                selected_tournament = tournaments[selected_index]
                cls.add_player(selected_tournament.name, store, route_params)
            else:
                TournamentView.display_invalid_tournament_number()
        else:
            result = "tournament_not_found"
            TournamentView.display_tournament_list(tournaments, result)
        return "tournament_management", None

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
    def get_selected_tournament_index(cls):
        selected_index = TournamentView.display_selected_tournament()
        try:
            selected_index = int(selected_index) - 1
            return selected_index
        except ValueError:
            TournamentView.display_invalid_input()
            return None

    @classmethod
    def start_tournament(cls, store, route_params=None):
        tournaments = cls.list_tournaments(store, route_params)
        if tournaments:
            selected_index = cls.get_selected_tournament_index()
            if 0 <= selected_index < len(tournaments):
                selected_tournament = tournaments[selected_index]
                current_date = datetime.now().date()
                date_format = "%d/%m/%Y"
                date_start = datetime.strptime(selected_tournament.date_start, date_format).date()
                date_end = datetime.strptime(selected_tournament.date_end, date_format).date()
                if date_start <= current_date <= date_end:
                    choice = TournamentView.display_tournament_to_start(selected_tournament)
                    if choice == "1":
                        round_name, round_num = Tournament.start_tournament(selected_tournament)
                        Tournament.generate_pairs(selected_tournament, round_num)
                        while True:
                            cls.round(round_name)

    @classmethod
    def round(cls, round_name):
        matches = Tournament.matches
        TournamentView.display_list_match_in_round(matches, round_name)
        choice_match = TournamentView.display_match(matches)
        cls.choice_match_winner(choice_match, matches)

        return "details_round", round_name

    @classmethod
    def choice_match_winner(cls, choice_match, matches):
        choice_match = int(choice_match)
        match = matches[choice_match - 1]
        choice_winner = TournamentView.display_match_winner(match)
        if choice_winner == "1":
            match.score_a += 1
        elif choice_winner == "2":
            match.score_b += 1
        else:
            match.score_a += 0.5
            match.score_b += 0.5
        TournamentView.display_result_match(match)
