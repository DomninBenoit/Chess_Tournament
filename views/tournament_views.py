from controllers.tournament_controller import TournamentController


def create_tournament_form():
    print("=== Création d'un nouveau tournoi ===")
    name = input("Nom du tournoi : ")
    place = input("Lieu du tournoi : ")
    date_start = input("Date de début (jj/mm/aaaa) : ")
    date_end = input("Date de fin (jj/mm/aaaa) : ")
    nb_round = int(input("Nombre de rounds (facultatif - par défaut : 4) : "))

    TournamentController.create(name, place, date_start, date_end, nb_round)

    print("Le tournoi a été créé avec succès!")
    print()



def process_create_tournament_form():
    create_tournament_form()
    return
