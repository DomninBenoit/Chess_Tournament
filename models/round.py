from datetime import datetime
from models.match import Match


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

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end_date": self.end_date.strftime('%Y-%m-%d %H:%M:%S') if
            self.end_date else None,
            "match_list": [match.to_dict() for match in self.match_list],
        }

    @classmethod
    def from_dict(cls, round_dict, players_dict):
        name = round_dict["name"]
        start_date = datetime.strptime(round_dict["start_date"],
                                       '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(round_dict["end_date"],
                                     '%Y-%m-%d %H:%M:%S') if \
            round_dict["end_date"] else None
        matches = [Match.from_dict(match_dict, players_dict)
                   for match_dict in round_dict["match_list"]]
        round_obj = cls(name)
        round_obj.start_date = start_date
        round_obj.end_date = end_date
        round_obj.match_list = matches
        return round_obj
