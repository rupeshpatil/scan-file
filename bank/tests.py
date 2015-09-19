import unittest
from bankfile import FileScaner
import os
class TestReadEntries(unittest.TestCase):

    def test_read_zeroes(self):
        obj = FileScaner()
        zeroes =   " _  _  _  _  _  _  _  _  _ "\
                   "| || || || || || || || || |"\
                   "|_||_||_||_||_||_||_||_||_|"

        account_number = obj.parse_lines(zeroes)
        self.assert_(tuple(account_number) == (0,0,0,0,0,0,0,0,0))

    def test_read_ones(self):
        obj = FileScaner()
        ones =  "                           "\
                "  |  |  |  |  |  |  |  |  |"\
                "  |  |  |  |  |  |  |  |  |"

        account_number = tuple(obj.parse_lines(ones))
        self.assert_(account_number == (1,1,1,1,1,1,1,1,1))

  
    def test_get_account_numbers_from_file(self):
        obj = FileScaner()
        filename = 'testcase1.txt'
        account_numbers = obj.read_file(filename)
        self.assert_(tuple(account_numbers[10]) == (1,2,3,4,5,6,7,8,9))

    def test_user_story_3(self):
        obj = FileScaner()
        filename = 'usertestcase3.txt'
        account_numbers = obj.user_story3(filename)
        self.assert_(account_numbers[1] == '49006771? ILL')


if __name__ == '__main__':
    unittest.main()