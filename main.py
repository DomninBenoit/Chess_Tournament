from controllers.home_controller import HomePageController
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
import subprocess as sp


class Application:
    routes = {
        "homepage": HomePageController.dispatch(),
        #"players_management": PlayerController.list,
        #"create_player": PlayerController.create,
        "tournament_management": TournamentController.list(),
        #"add_tournament": TournamentController.create,
        "add_player_in_tournament": TournamentController.list_tournaments(),
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None

 #   def run(self):
 #       while not self.exit:
  #          # Clear the shell output
 #           sp.call('clear', shell=True)
#
 #           # Get the controller method that should handle our current route
 #           controller_method = self.routes[self.route]
#
 #           # Call the controller method
 #           next_route, next_params = controller_method()
#
 #           # Set the next route and parameters
 #           self.route = next_route
 #           self.route_params = next_params
#
 #           # If the controller returned "quit", end the loop
 #           if next_route == "quit":
 #               self.exit = True
#
#
#if __name__ == "__main__":
#    app = Application()
#    app.run()
