import random
import math
'''n = random.randint(1,100)'''
n = float(input('Digite o valor: ' ))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O valor aleatorio é {}, em seno é {:.2f} em cosseno é {:.2f} e a tangente é {:.2f}'.format(n,sen,cos,tan))
