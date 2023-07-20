class PlayerView:
    @classmethod
    def display_list(cls, route_params=None):
        print("1. Create Player")
        print("Q. Exit\n")

        choice = input("Choice:")
        extra_info = None

        return choice, extra_info

    @classmethod
    def create_player_form(cls, route_params=None):
        print("=== Création d'un nouveau joueur ===")
        return {
            "firstname": input("Prénom : "),
            "lastname": input("Nom : "),
            "date_of_birth": input("Date de naissance (jj/mm/aaaa) : "),
            "national_id": input("Identifiant National : "),
        }

    @classmethod
    def display_player_not_found(cls):
        print("L'ID du joueur n'existe pas")

    @classmethod
    def list_players(cls, players):
        sorted_players = sorted(players, key=lambda player: f"{player.lastname.capitalize()} {player.firstname.capitalize()}")
        for player in sorted_players:
            print(f"{player.lastname.upper()} {player.firstname.capitalize()}")

        input("Appuyez sur une touche pour quitter la liste")

