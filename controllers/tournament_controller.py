import json, os
from models.tournament import Tournament
from views.tournament_views import TournamentView


class TournamentController:
    tournaments = []

    @classmethod
    def list(cls, route_params=None):
        choice = TournamentView.display_list()

        if choice == "1":
            return "add_tournament"
        elif choice == "2":
            return "add_player_in_tournament", None

    @classmethod
    def create(cls):
        data = TournamentView.create_tournament_form()
        tournament = Tournament(**data)
        if os.path.getsize('data/tournaments.json') == 0:
            cls.tournaments.append(tournament)
            cls.save_tournaments()
        else:
            cls.load_tournaments()
            cls.tournaments.append(tournament)
            cls.save_tournaments()

        print("Le tournoi a été créé avec succès!")
        print()

        return "tournament_management"

    @classmethod
    def find_tournament_by_name(cls, tournaments, name):
        for tournament in tournaments:
            if tournament.name == name:
                return tournament
        return None

    @classmethod
    def register(cls, tournament_name, player_id):
        # Charger les tournois à partir du fichier JSON
        tournaments = cls.load_tournaments()

        # Rechercher le tournoi spécifié par son nom
        tournament = cls.find_tournament_by_name(tournaments, tournament_name)
        if tournament is None:
            print("Le tournoi spécifié n'existe pas.")
            return

        # Vérifier si le joueur est déjà inscrit dans le tournoi
        if player_id in tournament.players:
            print("Le joueur est déjà inscrit dans le tournoi.")
            return

        # Ajouter le joueur à la liste des joueurs du tournoi
        tournament.players.append(player_id)

        # Enregistrer les tournois mis à jour dans le fichier JSON
        cls.save_tournaments()

        print("Le joueur a été inscrit dans le tournoi avec succès.")

    @classmethod
    def load_tournaments(cls):
        with open('data/tournaments.json', 'r') as f:
            tournaments_json = json.load(f)

        cls.tournaments = []
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
            cls.tournaments.append(tournament)

        return cls.tournaments

    @classmethod
    def save_tournaments(cls):
        tournaments_json = []
        for tournament in cls.tournaments:
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

    @classmethod
    def list_tournaments(cls):
        tournaments = cls.tournaments
        if tournaments:
            print("=== Liste des tournois ===")
            for i, tournament in enumerate(tournaments):
                print(f"{i + 1}. {tournament.name}")
            print()

            # demande choix tournoi
            selected_index = input("Sélection du tournoi (entrez le numéro) :")
            try:
                selected_index = int(selected_index) - 1
                if 0 <= selected_index < len(tournaments):
                    selected_tournament = tournaments[selected_index]
                    cls.add_player_to_tournament(selected_tournament.name)
                else:
                    print("Numéro de tournoi invalide")
            except ValueError:
                print("entrée invalide")
        else:
            print("Aucun tournoi enregistré.")
        print()

    @classmethod
    def add_player_to_tournament(cls, tournament_name):
        player_id = input("ID du joueur : ")
        cls.register(tournament_name, player_id)
        print()