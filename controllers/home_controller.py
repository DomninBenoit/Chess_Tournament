from views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, route_params=None):
        choice = HomeView.home()
        if choice == "1":
            return "players_management"
        elif choice == "2":
            return "tournament_management"

