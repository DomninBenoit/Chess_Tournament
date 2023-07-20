from controllers.home_controller import HomePageController
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from models.player import Player
import subprocess as sp

from models.round import Round
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
            "players": [
                Player("Domnin", "Benoit", "15/03/1989", "AB12345"),
                Player("alain", "brin", "15/03/1989", "AB45678"),
                Player("John", "Doe", "01/01/1990", "CD12345"),
                Player("Jane", "Smith", "15/07/1992", "EF12345"),
                Player("Michael", "Johnson", "10/05/1987", "GH12345"),
                Player("Emily", "Brown", "25/09/1995", "IJ12345"),
                Player("David", "Wilson", "08/12/1991", "KL12345"),
                Player("Sarah", "Davis", "22/06/1985", "MN12345"),
            ],
            "tournaments": [],

        }
        player1 = self.store["players"][0]
        player2 = self.store["players"][1]
        player3 = self.store["players"][2]
        player4 = self.store["players"][3]
        player5 = self.store["players"][4]
        player6 = self.store["players"][5]
        player7 = self.store["players"][6]
        player8 = self.store["players"][7]

        tournament = Tournament("Noir", "Bourges", "07/07/2023",
                                "08/08/2023", 4, [player1, player2, player3, player4, player5, player6, player7], [])

        self.store["tournaments"].append(tournament)

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


if __name__ == "__main__":
    app = Application()
    app.run()
