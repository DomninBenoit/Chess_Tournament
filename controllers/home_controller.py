from views.home_view import HomeView


class HomePageController:

    @classmethod
    def dispatch(cls, input=None):
        choice = HomeView.home()
        if choice.lower() == "q":
            next = "quit"
        elif choice == "1":
            next = "players_management"
        elif choice == "2":
            next = "tournament_management"
        return next, None
