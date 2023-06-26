import json
from models.player import Player


class PlayerController:
    players = []

    @classmethod
    def create(cls, firstname, lastname, date_of_birth, national_id):
        player = Player(firstname, lastname, date_of_birth, national_id)
        cls.players.append(player)
        cls.save_player()

    @classmethod
    def save_player(cls):
        players_json = []
        for player in cls.players:
            player_data = {
                'firstname': player.firstname,
                'lastname': player.lastname,
                'date_of_birth': player.date_of_birth,
                'national_id': player.national_id
            }
            players_json.append(player_data)

        # Charger les joueurs existants depuis le fichier JSON
        existing_players = []
        try:
            with open('data/players.json', 'r') as f:
                existing_players = json.load(f)
        except FileNotFoundError:
            pass

        # Ajouter les nouveaux joueurs à la liste existante
        existing_players.extend(players_json)

        with open('data/players.json', 'w') as f:
            json.dump(existing_players, f)
