from controllers.home_controller import HomePageController
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from data.json_utils import JsonUtils
from models.player import Player
from models.tournament import Tournament


class Application:
    routes = {
        "homepage": HomePageController.dispatch,
        "players_management": PlayerController.list,
        "tournament_management": TournamentController.list,
        "rapports": HomePageController.list_rapport,
        "list_players": PlayerController.list_players,
        "listing_tournaments": TournamentController.listing_tournaments,
        "create_player": PlayerController.create,
        "add_tournament": TournamentController.create,
        "add_player_in_tournament": TournamentController.add_player_to_tournament,
        "list_players_in_tournament": TournamentController.list_players_in_tournament,
        "list_round_and_match_in_tournament": TournamentController.list_round_and_match_in_tournament,
        "start_tournament": TournamentController.start_tournament,
        "next_round": TournamentController.next_round,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = {
            "players": [],
            "tournaments": [],
        }
        JsonUtils.load_store(self.store),

    def run(self):
        while not self.exit:

            # Get the controller method that should handle our current route
            controller_method = self.routes[self.route]

            # Call the controller method
            next_route, next_params = controller_method(
                self.store, self.route_params
            )

            # Set the next route and parameters
            self.route = next_route
            self.route_params = next_params
            # If the controller returned "quit", end the loop
            if next_route == "quit":
                self.exit = True

        JsonUtils.save_store(self.store)


if __name__ == "__main__":
    app = Application()
    app.run()
