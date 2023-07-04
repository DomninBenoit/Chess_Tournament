class PlayerView:
    @classmethod
    def display_list(cls, route_params=None):
        print("1. Create Player")

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