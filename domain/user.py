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
        punchesToday = self.get_punches_today()
        count_punches_today = self.__count_punches(punchesToday)

        hours = 0
        for index in range(0, count_punches_today, 2):
            start = punchesToday[index]
            end = punchesToday[index + 1]
            hours += (end.hour - start.hour)
        return hours

    def get_punches_today(self):
        today = datetime.now()
        punchesToday = filter(
            lambda punch: punch.day == today.day, self.punches)
        return list(punchesToday)

    @staticmethod
    def __count_punches(punches):
        count_punches = len(punches)
        return count_punches if count_punches % 2 == 0 else count_punches - 1
