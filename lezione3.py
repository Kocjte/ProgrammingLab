def sommavalori_sales():
    somma=[]
    
    my_file = open('sales.csv', 'r') 
    
    for line in my_file:
        elements = line.split(',')
        somma = sum elements[1] in my my_file

sommavaliori()       




