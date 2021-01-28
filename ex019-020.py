import random
#n = random.randint(1,20)
aluno1=(input('digite o nome do aluno: '))
aluno2=(input('Digite o nome do aluno: '))
aluno3=(input('Digite o nome do aluno: '))
aluno4=(input('Digite o nome do aluno: '))
alunos = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(alunos)

print('o aluno numero {}'.format(alunos))
