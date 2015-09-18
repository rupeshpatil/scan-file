import os
class FileScaner:
    """ 
        FileScaner scan the file and return the account numbers
    """    
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

        numbers = []
        for key,num_symbol in number_list.items():
            numbers.append(NUMBER_SYMBOLS.get(''.join(num_symbol)))
        
        return tuple(numbers)
           
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