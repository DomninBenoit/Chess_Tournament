from datetime import datetime


class Round:

    def __init__(self, name) -> None:
        self.name = name
        self.start_date = datetime.now()
        self.end_date = None
        self.match_list = []

    def add_match(self, match):
        self.match_list.append(match)

    def __str__(self):
        matches_str = '\n'.join(str(match) for match in self.match_list)
        return f"Round: {self.name}\nMatches:\n{matches_str}"
