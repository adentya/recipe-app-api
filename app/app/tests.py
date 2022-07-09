""" Sample test """


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        """ Test adding numbers together """

        res = calc.add(5, 7)
        self.assertEqual(res, 12)

        res = calc.add(5, 0)
        self.assertEqual(res, 5)

        res = calc.add(5, -3)
        self.assertEqual(res, 2)

    def test_subtract_numbers(self):
        """ Test subtracting numbers together """

        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
