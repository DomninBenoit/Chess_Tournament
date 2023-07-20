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

    @classmethod
    def list_rapport(cls, store, route_params=None):
        choice = HomeView.display_list()
        if choice == "1":
            return "list_players", None
        if choice == "2":
            return "list_tournaments", None


