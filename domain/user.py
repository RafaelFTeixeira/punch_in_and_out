from domain.punch import Punch


class User:
    def __init__(self, name, email):
        self.id = 0
        self.name = name
        self.email = email
        self.punches = []

    def to_punch(self):
        self.punches.append(Punch())

    def get_work_hours_by(self, date):
        punches = self.get_punches_by(date)
        count_punches = self.__count_punches(punches)

        hours = 0
        for index in range(0, count_punches, 2):
            start = punches[index]
            end = punches[index + 1]
            hours += (end.hour - start.hour)
        return hours

    def get_punches_by(self, date):
        punches = filter(
            lambda punch: (punch.day == date.day
                           and punch.month == date.month
                           and punch.year == date.year),
            self.punches)
        return list(punches)

    @staticmethod
    def __count_punches(punches):
        count_punches = len(punches)
        return count_punches if count_punches % 2 == 0 else count_punches - 1
