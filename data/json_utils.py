import json, os
from models.tournament import Tournament


class TournamentJson:
    @classmethod
    def load_tournaments(cls):
        tournaments = []

        if os.path.getsize('data/tournaments.json') > 0:  # Vérifie si le fichier n'est pas vide
            try:
                with open('data/tournaments.json', 'r') as f:
                    file_content = f.read()

                tournaments_json = json.loads(file_content)

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
                    tournaments.append(tournament)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading tournaments: {e}")

        return tournaments

    @classmethod
    def save_tournaments(cls, tournaments):
        tournaments_json = []
        for tournament in tournaments:
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


class PlayersJson:
    @classmethod
    def save_player(cls, players):
        players_json = []
        for player in players:
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