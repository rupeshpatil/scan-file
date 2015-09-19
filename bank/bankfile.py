import os
class FileScaner():
    """ 
        FileScaner scan the file and return the account numbers
    """ 
    NUMBER_SYMBOLS = {
                    ' _ | ||_|': 0,
                    '     |  |': 1,
                    ' _  _||_ ': 2,
                    ' _  _| _|': 3,
                    '   |_|  |': 4,
                    ' _ |_  _|': 5,
                    ' _ |_ |_|': 6,
                    ' _   |  |': 7,
                    ' _ |_||_|': 8,
                    ' _ |_| _|': 9
                    }

    def user_story1(self, filename):
        numbers = self.read_file(filename)
        return numbers   
 

    def user_story3(self, filename):
        numbers = self.read_file(filename)
        eligible_numbers = []  
        for num in numbers:
            eligible_numbers.append(self.find_elligible_number(num))
        return eligible_numbers

    
    def parse_lines(self, lines):
        number_list = {}
        linesbychars = ''
        for chars in lines:
            linesbychars += chars
            if len(linesbychars) == 27:
                num_offset = 0
                for num in range(9):
                    if num_offset <=27:
                        number_list.setdefault(num,[]).append(linesbychars[num_offset:num_offset+3])
                    num_offset +=3
                linesbychars = ''
        return self.get_number(number_list)


    def get_number(self, number_list):
        numbers = []
        for key,num_symbol in number_list.items():
            num = self.NUMBER_SYMBOLS.get(''.join(num_symbol))
            
            if num != None:
                numbers.append(num)
            else:
                numbers.append('?')
        return numbers

    def check_sum(self, numbers):
        reverse_number = numbers[::-1]
        products_num = []
        for i,v in enumerate(reverse_number):
            products_num.append(int(i+1) * int(v))
        if sum(products_num) % 11 == 0:
            return True
        return False
    
    def find_elligible_number(self, acc_number):
        acount_num = ''.join(str(x) for x in acc_number)
        if '?' in acc_number:
            return acount_num  +" "+ "ILL"
        elif self.check_sum(acc_number):
            return acount_num
        else:
            return acount_num +" "+ "ERR"

    def read_file(self, filename):
        """Returns all account numbers found in <filename>, as a list of tuples"""
        
        filepath = os.path.realpath(filename)
        account_numbers = []
        linecount = 0
        lines = ''
        with open(filepath, 'r') as f:
            for line in f:
                linecount += 1
                if linecount <=3:
                    # Remove trailing from line
                    lines += line.rstrip('\n')
                else:
                    account_numbers.append(self.parse_lines(lines))
                    linecount = 0
                    lines = []
        return account_numbers