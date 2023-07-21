from models.tournament import Tournament
from models.player import Player
import json


class JsonUtils:
    @classmethod
    def save_store(cls, store):
        with open('data/players.json', 'w') as outfile:
            player_dicts = []
            for player in store["players"]:
                player_dicts.append(player.to_dict())

            json.dump(player_dicts, outfile, indent=4)

        with open('data/tournaments.json', 'w') as outfile:
            tournament_dicts = []
            for tournament in store["tournaments"]:
                tournament_dicts.append(tournament.to_dict())

            json.dump(tournament_dicts, outfile, indent=4)

    @classmethod
    def load_store(cls, store):
        with open('players.json', 'r') as infile:
            json_data = json.load(infile)

            for player_dict in json_data:
                player = Player.from_dict(player_dict)
                store["players"].append(player)

        with open('tournament.json', 'r') as infile:
            json_data = json.load(infile)

            for tournament_dict in json_data:
                tournament = Tournament.from_dict(tournament_dict, store)
                store["tournaments"].append(tournament)
