import unittest
from bankfile import FileScaner
import os
class TestCaseUserStories(unittest.TestCase):

    def test_read_zeroes_account_number(self):
        obj = FileScaner()
        zeroes =   " _  _  _  _  _  _  _  _  _ "\
                   "| || || || || || || || || |"\
                   "|_||_||_||_||_||_||_||_||_|"

        account_number = obj.parse_lines(zeroes)
        self.assert_(tuple(account_number) == (0,0,0,0,0,0,0,0,0))

    def test_read_ones_account_number(self):
        obj = FileScaner()
        ones =  "                           "\
                "  |  |  |  |  |  |  |  |  |"\
                "  |  |  |  |  |  |  |  |  |"

        account_number = tuple(obj.parse_lines(ones))
        self.assert_(account_number == (1,1,1,1,1,1,1,1,1))

  
    def test_get_account_numbers_from_file(self):
        """ 
            Read Number from files and verify account number
        """
        obj = FileScaner()
        filename = 'userstory1_input.txt'
        account_numbers = obj.read_file(filename)
        self.assert_(tuple(account_numbers[10]) == (1,2,3,4,5,6,7,8,9))

    def test_read_file_and_check_wrong_characters(self):
        """
            Scan file and find wrong input character with ?
        """
        obj = FileScaner()
        filename = 'userstroy3_input.txt'
        account_numbers = obj.user_story3(filename)
        self.assert_(account_numbers[1] == '49006771? ILL')

    def test_read_file_and_check_right_account_number(self):
        """
            Scan file and find wrong input character with ?
        """
        obj = FileScaner()
        filename = 'userstroy3_input.txt'
        account_numbers = obj.user_story3(filename)
        self.assert_(account_numbers[0] == '000000051')

    def test_check_invalid_checksum_acc_number(self):
        """
            verify account number with invalid checksum
        """
        obj = FileScaner()
        acc_number = [1,1,1,1,1,1,1,1,7]     
        account_number = obj.check_sum(acc_number)
        self.assert_(account_number == False)

    def test_check_valid_checksum_acc_number(self):
        """
            verify account number with valid checksum
        """
        obj = FileScaner()
        acc_number = [7,1,1,1,1,1,1,1,1]     
        account_number = obj.check_sum(acc_number)
        self.assert_(account_number == True)


if __name__ == '__main__':
    unittest.main()