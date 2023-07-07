class TournamentView:
    @classmethod
    def display_list(cls, route_params=None):
        print("1. Creation Tournoi")
        print("2. Ajout joueur au tournoi")
        print("3. Supprimer tournoi")

        choice = input("Choice:")
        extra_info = None

        return choice, extra_info

    @classmethod
    def create_tournament_form(cls, route_params=None):
        print("=== Création d'un nouveau tournoi ===")
        return {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "date_start": input("Date de début (jj/mm/aaaa) : "),
            "date_end": input("Date de fin (jj/mm/aaaa) : "),
            "nb_round": int(input("Nombre de rounds (facultatif - par défaut : 4) : "))
        }

    @classmethod
    def get_tournament_name(cls):
        tournament_name = input("Entrer le nom du tournoi à supprimer : ")
        return tournament_name

    @classmethod
    def display_delete_result(cls, result, route_params=None):
        if result == "tournament_delete":
            print("Le tournoi est supprimé")
        elif result == "tournament_not_found":
            print("Le tournoi spécifié n'existe pas.")

    @classmethod
    def display_registration_result(cls, result, route_params=None):
        if result == "tournament_not_found":
            print("Le tournoi spécifié n'existe pas.")
        elif result == "player_already_registered":
            print("Le joueur est déjà inscrit dans le tournoi.")
        elif result == "player_registered":
            print("Le joueur a été inscrit dans le tournoi avec succès.")

    @classmethod
    def display_tournament_list(cls, tournaments, result, route_params=None):
        if result == "display_list_tournament":
            print("=== Liste des tournois ===")
            for i, tournament in enumerate(tournaments):
                print(f"{i + 1}. {tournament.name}")
            print()
        elif result == "tournament_not_found":
            print("Aucun tournoi enregistré.")

    @classmethod
    def display_selected_tournament(cls, route_params=None):
        selected_index = input("Sélection du tournoi (entrez le numéro) :")
        return selected_index

    @classmethod
    def display_invalid_tournament_number(cls, route_params=None):
        print("Numéro de tournoi invalide")

    @classmethod
    def display_invalid_input(cls, route_params=None):
        print("Entrée invalide")

    @classmethod
    def get_player_id(cls,route_params=None):
        return input("ID du joueur : ")

    @classmethod
    def display_data(cls, tournaments):
        for tournament in tournaments:
            print(f"Tournament: {tournament.name}")
            print(f"Place: {tournament.place}")
            print(f"Date Start: {tournament.date_start}")
            print(f"Date End: {tournament.date_end}")
            print(f"Number of Rounds: {tournament.nb_round}")
            print("Players:")
            for player in tournament.players:
                print(f"- Player ID: {player}")
            print("---------")