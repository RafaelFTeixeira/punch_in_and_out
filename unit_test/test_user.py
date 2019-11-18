import unittest
from datetime import datetime, timedelta
from domain.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('Rafael Teixeira', 'rafaelteixeiradev@gmail.com')

    def test_should_create_an_user(self):
        user_expected = {
            'name': 'Rafael Teixeira',
            'email': 'rafaelteixeiradev@gmail.com',
            'punches': []
        }

        user = User('Rafael Teixeira', 'rafaelteixeiradev@gmail.com')

        self.assertEqual(user_expected, user.__dict__)

    def test_should_get_work_hours_today(self):
        hour_expected = 1
        punch_in = datetime.now()
        punch_out = datetime.now() + timedelta(hours=hour_expected)
        self.user.punches = [punch_in, punch_out]

        hours = self.user.get_work_hours_today()

        self.assertEqual(hour_expected, hours)

    def test_should_return_zero_hour_when_no_has_two_punch_clock(self):
        punch_in = datetime.now()
        self.user.punches = [punch_in]

        hours = self.user.get_work_hours_today()

        self.assertEqual(0, hours)

    def test_should_return_sum_hours_with_start_and_end(self):
        punch_in = datetime.now()
        punch_out = datetime.now() + timedelta(hours=1)
        punch_in2 = datetime.now() + timedelta(hours=2)
        self.user.punches = [punch_in, punch_out, punch_in2]

        hours = self.user.get_work_hours_today()

        self.assertEqual(1, hours)


if __name__ == "__main__":
    unittest.main()
