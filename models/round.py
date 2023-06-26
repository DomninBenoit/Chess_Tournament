from datetime import datetime


class Round:

    def __init__(self, name) -> None:
        self.name = name
        self.start_date = datetime.now()
        self.end_date = None
        self.match_list = []

