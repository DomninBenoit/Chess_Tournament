class TournamentView:
    @classmethod
    def display_list(cls, route_params=None):
        print("1. Creation Tournoi")
        print("2. Ajout joueur au tournoi")
        print("3. Supprimer tournoi")
        print("4. Afficher les tournoi")
        print("5. Lancer un tournoi")

        choice = input("Choice:")

        return choice

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
    def get_player_id(cls, route_params=None):
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
                print(f"- Player :\n{player}")
            print("---------")

    @classmethod
    def display_tournament_to_start(cls, tournament):
        print(f"Nom: {tournament.name}")
        print(f"Lieu: {tournament.place}")
        print(f"Date: {tournament.date_start}")
        print("")
        print("1. Lancer le premier round")

        choice = input("Choice:")

        return choice

    @classmethod
    def display_list_match_in_round(cls, matches, round_name):
        print(f"{round_name}\n")
        match_number = 1
        for match in matches:
            if match.score_a == 1:
                result = f"{match.player_a.firstname} {match.player_a.lastname} wins"
            elif match.score_b == 1:
                result = f"{match.player_b.firstname} {match.player_b.lastname} wins"
            elif match.score_a == 0.5 and match.score_b == 0.5:
                result = "egality"
            else:
                result = "waiting for result"
            print(
                f"match {match_number} : {match.player_a.firstname} {match.player_a.lastname} vs {match.player_b.firstname} {match.player_b.lastname} - {result}")
            match_number += 1
        print("")

    @classmethod
    def display_match(cls, matches):
        match_number = 1
        for match in matches:
            if match.score_a == 0 and match.score_b == 0:
                print(f" entrer le resultat du match {match.player_a.firstname} {match.player_a.lastname} vs {match.player_b.firstname} {match.player_b.lastname}")
                match_number += 1
        print("")
        choice = input("Choice num match:")
        print("")
        return choice

    @classmethod
    def display_match_winner(cls, match):
        print(f"1. {match.player_a.firstname} {match.player_a.lastname} wins")
        print(f"2. {match.player_b.firstname} {match.player_b.lastname} wins")
        print("3. egalité")
        print("")
        choice = input("Choice:")
        print("")
        return choice

    @classmethod
    def display_result_match(cls, match):
        print(f"{match.player_a.firstname} {match.player_a.lastname} score : {match.score_a}")
        print(f"{match.player_b.firstname} {match.player_b.lastname} score : {match.score_b}")