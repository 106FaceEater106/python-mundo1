ano = int(input("ano: "))
s = ano %4 and ano %100

b = ano %400
if (s == 0 ) or (b == 0):
    print("Ano bissexto")
else:
    print('Ano não bissexto')

