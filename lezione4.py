class CSVFile(my_file):
    
    def __init__(self,name):
        
        my_file = open('sales.csv', 'r')

        for line in my_file:
            elements = line.split(',')
        
            if elements[0]!='Date':
                date = elements[0]
                value = elements[1]
            #️attributo
            self.name = name
    
    def get_data():
        my_file = open('sales.csv', 'r')
