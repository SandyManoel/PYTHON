"""Criar lista de frutas e outra de vegetais 
Use for loop aninhado (nested for loop) para imprimir todas combinações possiveis de frutas
e vegetais, com a fruta primeiro, e o vegetal em segundo."""

frutas = ['maça', 'morango', 'uva']
vegetais = ['brocolis', 'cenoura', 'batata']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'Fruta: {fruta}, vegetal: {vegetal}')