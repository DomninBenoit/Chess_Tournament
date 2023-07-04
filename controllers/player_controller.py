from data.json_utils import PlayersJson
from models.player import Player
from views.player_views import PlayerView


class PlayerController:
    players = []

    @classmethod
    def list(cls, route_params=None):
        choice = PlayerView.display_list()
        if choice == "1":
            return "create_player", None
        else:
            return "tournament_management", None

    @classmethod
    def create(cls, firstname, lastname, date_of_birth, national_id):
        player = Player(firstname, lastname, date_of_birth, national_id)
        cls.players.append(player)
        PlayersJson.save_player(cls.players)
