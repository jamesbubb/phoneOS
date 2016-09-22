import unittest
from Phone import Phone
# Phone class tests
class PhoneTests(unittest.TestCase):

    def setUp(self):
        self.Phone = Phone()

    def tearDown(self):
        self.Phone = None

    def test_phoneSwitchesOn(self):
        self.assertFalse(self.Phone.isOn)
        self.Phone.switchOn()
        self.assertTrue(self.Phone.isOn)
