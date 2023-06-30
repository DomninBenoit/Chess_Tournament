class TournamentView:
    @classmethod
    def display_list(cls):
        print("1. Add Tournament")
        print("2. Add Player in Tournament")

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





