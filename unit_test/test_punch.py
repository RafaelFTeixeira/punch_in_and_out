import unittest
from datetime import datetime
from domain.punch import Punch


class PunchTest(unittest.TestCase):
    def test_should_to_punch_with_date_today(self):
        punch = Punch()

        self.assertEqual(datetime.now().day, punch.date.day)


if __name__ == "__main__":
    unittest.main()
