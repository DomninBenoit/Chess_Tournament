class TournamentView:
    @classmethod
    def display_list(cls):
        print("1. Add Tournament")
        print("2. Add Player in Tournament")
        print("3. Delete Tournament")

        choice = input("Choice:")
        extra_info = None

        return choice, extra_info

    @classmethod
    def create_tournament_form(cls):
        print("=== Création d'un nouveau tournoi ===")
        return {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "date_start": input("Date de début (jj/mm/aaaa) : "),
            "date_end": input("Date de fin (jj/mm/aaaa) : "),
            "nb_round": int(input("Nombre de rounds (facultatif - par défaut : 4) : "))
        }

    @classmethod
    def display_registration_result(cls, result):
        if result == "tournament_not_found":
            print("Le tournoi spécifié n'existe pas.")
        elif result == "player_already_registered":
            print("Le joueur est déjà inscrit dans le tournoi.")
        elif result == "player_registered":
            print("Le joueur a été inscrit dans le tournoi avec succès.")

    @classmethod
    def display_tournament_list(cls, tournaments, result):
        if result == "display_list_tournament":
            print("=== Liste des tournois ===")
            for i, tournament in enumerate(tournaments):
                print(f"{i + 1}. {tournament.name}")
            print()
        elif result == "tournament_not_found":
            print("Aucun tournoi enregistré.")

    @classmethod
    def display_selected_tournament(cls):
        selected_index = input("Sélection du tournoi (entrez le numéro) :")
        return selected_index

    @classmethod
    def display_invalid_tournament_number(cls):
        print("Numéro de tournoi invalide")

    @classmethod
    def display_invalid_input(cls):
        print("Entrée invalide")

    @classmethod
    def get_player_id(cls):
        return input("ID du joueur : ")