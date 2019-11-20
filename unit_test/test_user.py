import unittest
from datetime import datetime
from domain.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('Rafael Teixeira', 'rafaelteixeiradev@gmail.com')

    def test_should_create_an_user(self):
        user_expected = {
            'id': 0,
            'name': 'Rafael Teixeira',
            'email': 'rafaelteixeiradev@gmail.com',
            'punches': []
        }

        user = User('Rafael Teixeira', 'rafaelteixeiradev@gmail.com')

        self.assertEqual(user_expected, user.__dict__)

    def test_should_get_work_hours_by_date(self):
        hour_expected = 1
        punch_in = datetime(2019, 11, 19, 8, 0)
        punch_out = datetime(2019, 11, 19, 9, 0)
        self.user.punches = [punch_in, punch_out]

        hours = self.user.get_work_hours_by(punch_in)

        self.assertEqual(hour_expected, hours)

    def test_should_return_zero_hour_when_no_has_two_punch_clock(self):
        date = datetime(2019, 11, 19, 8, 0)
        self.user.punches = [date]

        hours = self.user.get_work_hours_by(date)

        self.assertEqual(0, hours)

    def test_should_return_sum_hours_with_start_and_end(self):
        punch_in = datetime(2019, 11, 19, 8, 0)
        punch_out = datetime(2019, 11, 19, 9, 0)
        punch_in2 = datetime(2019, 11, 19, 10, 0)
        punch_out2 = datetime(2019, 11, 19, 12, 0)
        punch_in3 = datetime(2019, 11, 19, 14, 0)
        self.user.punches = [punch_in, punch_out,
                             punch_in2, punch_out2, punch_in3]

        hours = self.user.get_work_hours_by(punch_in)

        self.assertEqual(3, hours)

    def test_should_get_punches_with_year_month_and_day(self):
        punch_in = datetime(2019, 11, 19, 8, 0)
        punch_out = datetime(2019, 11, 19, 9, 0)
        punch_in2 = datetime(2018, punch_in.month, punch_in.day, 8, 0)
        punch_out2 = datetime(2018, punch_out.month, punch_in.day, 10, 0)
        punchesExpected = [punch_in, punch_out]
        self.user.punches = [punch_in, punch_out,
                             punch_in2, punch_out2]

        punchesFound = self.user.get_punches_by(punch_in)

        self.assertEqual(punchesExpected, punchesFound)


if __name__ == "__main__":
    unittest.main()
