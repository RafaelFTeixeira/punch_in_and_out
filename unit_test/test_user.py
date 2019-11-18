import unittest
from datetime import datetime, timedelta
from domain.user import User


class UserTest(unittest.TestCase):
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
        user = User('Rafael Teixeira', 'rafaelteixeiradev@gmail.com')
        punch_in = datetime.now()
        punch_out = datetime.now() + timedelta(hours=hour_expected)
        user.punches = [punch_in, punch_out]

        hours = user.get_work_hours_today()

        self.assertEqual(hour_expected, hours)


if __name__ == "__main__":
    unittest.main()
