"""
Crie um loop para imprimir os numeros de 1 a 10 na tela, mas pare de imprimir assim que 
chegar a 5 usando o comando break. em seguida crie um segundo loop que imprima os numeros de 1
a 10 mas pula a impressao do numero 5 usando continue"""

print('Loop com break: ')
for numero in range(1,11):
    if numero>5: #não imprime após o 5
        break
    print (numero)    

print('Loop com o continue: ')
for numero in range(1,11):
    if numero==5: #pula 5
        continue
    print(numero)