from views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store, route_params=None):
        choice = HomeView.home()
        if choice == "1":
            return "players_management", None
        elif choice == "2":
            return "tournament_management", None
        elif choice == "3":
            return "rapports", None
        elif choice.lower() == "q":
            return "quit", None

    @classmethod
    def list_rapport(cls, store, route_params=None):
        choice = HomeView.display_list()
        if choice == "1":
            return "list_players", None
        elif choice == "2":
            return "listing_tournaments", None
        elif choice == "3":
            return "list_players_in_tournament", None
        elif choice == "4":
            return "list_round_and_match_in_tournament", None
        elif choice.lower() == "q":
            return "quit", None
