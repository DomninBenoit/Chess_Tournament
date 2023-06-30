class HomeView:

    @classmethod
    def home(cls):
        print("Welcome\n")
        print("1. Players Management")
        print("2. Tournament Management\n")
        print("Q. Exit")

        return input("Choice: ")
