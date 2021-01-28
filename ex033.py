n = int(input("Digite um numero: "))
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

#verificando quem é o menor
menor = n
if n1<n and n1<n2:
    menor = n1
if n2<n and n2<n1:
    menor = n2

print("O menor valor digitado foi {}.".format(menor))
maior = n
if n1>n and n1>n2:
    maior = n1
if n2>n and n2>n1:
    maior = n2
print('O maior valor digitado foi {}.'.format(maior))