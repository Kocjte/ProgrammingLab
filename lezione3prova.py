def somma(lista):
    somma=0
    for j in lista:
        somma=somma+j
    return (somma)

def lista():
    values=[]
    miofile=open('sales.csv','r')
    for line in miofile:
        elementi=line.split(',')
        if elementi[0]!='Date':
            value = elementi[1]
            date = elementi[0]

            values.append(float(value))
    return (values)
L=lista()
print(L)
S=somma(L)
print(S)

    