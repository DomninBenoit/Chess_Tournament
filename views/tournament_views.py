class TournamentView:
    @classmethod
    def display_list(cls, route_params=None):
        print("1. Creation Tournoi")
        print("2. Ajout joueur au tournoi")
        print("3. Lancer un tournoi")
        print("Q. Exit\n")

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
    def display_tournament_list(cls, tournaments, route_params=None):
        if not tournaments:
            print("Aucun tournoi enregistré.")
            input("Appuyez sur une touche pour continuer...")
            return

        print("=== Liste des tournois ===")
        for i, tournament in enumerate(tournaments):
            print(f"{i + 1}. {tournament.name}")

    @classmethod
    def display_selected_tournament(cls, route_params=None):
        selected_index_str = input("Sélection du tournoi (entrez le numéro) :")
        selected_index = int(selected_index_str) - 1
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

        input("Choice:")

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
        for index, match in enumerate(matches, start=1):
            if match.score_a == 0 and match.score_b == 0:
                print(f"Entrer le résultat du match {index}")
        print("")
        choice = input("Choix du numéro de match : ")
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
    def display_round_next(cls):
        print("Tout les match du tour sont valider")
        input("Appuyez sur une touche pour lancer le tour suivant...")

    @classmethod
    def display_round(cls, rounds):
        print("Le Tournoi est maintenant terminé")
        for round_obj in rounds:
            print(f"Round : {round_obj.name}")
            for matches in round_obj.match_list:
                for match in matches:
                    print(f"{match.player_a.firstname} {match.player_a.lastname} : {match.score_a} / {match.score_b} : {match.player_b.firstname} {match.player_b.lastname}")
        input("Appuyez sur une touche pour quitter le tournoi")

    @classmethod
    def display_ranking(cls, selected_tournament):
        sorted_dict = dict(sorted(selected_tournament.scores.items(), key=lambda item: item[1], reverse=True))
        for player in sorted_dict:
            score = selected_tournament.scores[player]
            print(f"{player.firstname} {player.lastname} : {score}")

    @classmethod
    def list_tournaments(cls, tournaments):
        sorted_tournament = sorted(tournaments, key=lambda tournament: f"{tournament.name.capitalize()}")
        for tournament in sorted_tournament:
            print(f"{tournament.name.capitalize()}  du {tournament.date_start} au {tournament.date_end}")

        input("Appuyez sur une touche pour quitter la liste")

    @classmethod
    def list_round_in_tournament(cls, rounds):
        if not rounds:
            print("Le tournoi n'a pas encore débuté")
        else:
            for round_obj in rounds:
                print(f"Round : {round_obj.name}")
                for matches in round_obj.match_list:
                    for match in matches:
                        print(f"{match.player_a.firstname} {match.player_a.lastname} : {match.score_a} / {match.score_b} : {match.player_b.firstname} {match.player_b.lastname}")
            input("Appuyez sur une touche pour quitter le tournoi")