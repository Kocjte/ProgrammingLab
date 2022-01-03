def somma(lista):
    somma=0
    for n in lista:
        somma=somma+n
    return (somma)     

def lista():
    values = []
    my_file = open('sales.csv', 'r') 
    for line in my_file:
        elementi=line.split(',')
        if elementi[0]!='Date':
        #️data e valore
            date = elementi[0]
            value = elementi[1]

            values.append(float(value))
    return (values)

L=lista()
print(L)
s1=somma(L)
print(round(s1))


