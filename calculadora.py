print("Digite um número ")
n1 = int(input(""))
print("Digite o segundo número ")
n2 = int(input(""))
print("Qual operação você deseja usar? (+, -, x ou ÷) ")
op = input("")
if op == "+":
  print(n1, "+", n2, "=", n1 + n2, "é o resultado desta operação")
elif op == "-":
  print(n1, "-", n2, "=", n1 - n2, "é o resultado desta operação")
elif op == "x":
  print(n1, "x", n2, "=", n1 * n2, "é o resultado desta operação")
elif op == "÷":
  print(n1, "÷", n2, "=", n1 / n2, "é o resultado desta operação")
else:
  print("Error")
