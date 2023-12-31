class Player:

    def __init__(self, firstname, lastname, date_of_birth,
                 national_id) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.national_id = national_id

    def __str__(self):
        return f"Prénom: {self.firstname}\n" \
               f"Nom: {self.lastname}\n" \
               f"Date de naissance: {self.date_of_birth}\n" \
               f"Id national: {self.national_id}\n"

    def to_dict(self):
        return {
            "national_id": self.national_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "date_of_birth": self.date_of_birth,
        }

    @classmethod
    def from_dict(cls, player_dict):
        national_id = player_dict["national_id"]
        firstname = player_dict["firstname"]
        lastname = player_dict["lastname"]
        date_of_birth = player_dict["date_of_birth"]
        player = cls(firstname, lastname, date_of_birth, national_id)
        return player
