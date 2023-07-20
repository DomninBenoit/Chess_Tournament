class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. Players Management")
        print("2. Tournament Management")
        print("3. Rapports\n")

        choice = input("Choice:")

        return choice

    @classmethod
    def display_list(cls):
        print("1. Liste des Joueurs")
        print("2. Liste des Tournois")

        choice = input("Choice : ")

        return choice
