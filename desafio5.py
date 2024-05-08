"""Criar um script que solicite ao usuario dois numeros,
em seguida o script deve imprimir a soma, subtração, multiplicação
divisão e exponenciação desses dois numeros"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1+num2
subtração = num1-num2
multiplicacao = num1*num2
divisão = num1/num2
exponenciação = num1 ** num2

print(f"Num1: {num1} e Num2: {num2}\nSoma: {soma}\nSubtração: {subtração}\nMultiplicação: {multiplicacao}\nDivisão:{divisão}\nExponenciação: {exponenciação}")
