class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. Players Management")
        print("2. Tournament Management\n")

        choice = input("Choice:")
        extra_info = None

        return choice, extra_info
