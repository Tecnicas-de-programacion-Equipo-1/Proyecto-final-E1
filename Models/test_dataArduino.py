from unittest import TestCase
from main import DataArduino


class TestDataArduino(TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def test_on_off(self):
        """-- Test On Off of Lights"""
        msg = "The correct value is not being returned"
        self.assertEqual(DataArduino().on_off("Sala/Comedor", "E", True), '1E', msg=msg)
        self.assertEqual(DataArduino().on_off("Sala/Comedor", "E", False), '0E', msg=msg)

    def test_on__off_parking(self):
        self.fail()

    def test_handle_data(self):
        self.fail()
