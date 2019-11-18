from domain.punch import Punch
from datetime import datetime


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.punches = []

    def to_punch(self):
        self.punches.append(Punch())

    def get_work_hours_today(self):
        today = datetime.now()
        punchesToday = filter(
            lambda punch: punch.day == today.day, self.punches)
        punchesToday = list(punchesToday)

        hours = 0
        for index in range(0, len(punchesToday), 2):
            start = punchesToday[index]
            end = punchesToday[index + 1]
            hours = end.hour - start.hour
        return hours
