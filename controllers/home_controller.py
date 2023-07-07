from views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, store, route_params=None):
        choice = HomeView.home()
        if choice == "1":
            return "players_management", None
        elif choice == "2":
            return "tournament_management", None

