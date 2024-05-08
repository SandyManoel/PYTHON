"""Criar lista chamada frutas e remova a manga da lista usando
remove() e remova o ultimo item da lista usando del"""

frutas = ['maça', 'banana', 'manga', 'uva', 'abacaxi']
frutas.remove('manga')
del frutas[-1]

print(frutas)