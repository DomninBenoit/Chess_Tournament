from models.player import Player
from views.player_views import PlayerView
import os


class PlayerController:
    players = []

    @classmethod
    def list(cls, store, route_params=None):
        choice = PlayerView.display_list()
        if choice == "1":
            return "create_player", None
        elif choice.lower() == "q":
            return "quit", None
        else:
            return "homepage", None

    @classmethod
    def create(cls, store, route_params=None):
        data = PlayerView.create_player_form()
        player = Player(**data)
        store["players"].append(player)

        return "players_management", None

    @classmethod
    def list_players(cls, store, route_params=None):
        players = store["players"]
        PlayerView.list_players(players)
        return "homepage", None
