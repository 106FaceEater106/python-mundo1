import random
n = random.randint(0,5)
r = int(input('Qual é o numero? '))
if r == n:
    print('Voce acertou, o numero era {}'.format(n))
else:
    print('Voce errou, o numero era {}'.format(n))