from controllers.home_controller import HomePageController
from controllers.tournament_controller import TournamentController


class Application:
    routes = {
        "homepage": HomePageController.dispatch,
        "tournament_management": TournamentController.list(),
        "add_tournament": TournamentController.create(),
        "add_player_in_tournament": TournamentController.list_tournaments()
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None

