# exercicio004

#Faça um programa que leia algo no teclado e mostre na tela 
#o seu tipo primitivo e todas as informações possiveis sobre ele

i = input('Digite algo: ')
print('{} é do tipo: '.format(i), type(i))
print('É alfabético?', i.isalpha())
print('É um número?', i.isnumeric())
print('É alfanumérico?', i.isalnum())
print('Está em caixa baixa?', i.islower())
print('Está em caixa alta?', i.isupper())
print('Só tem espaços?', i.isspace())
print('Está capitalizada?', i.istitle())   #Tem letras maiúculas e minùsculas

#Todo objeto possui caracteristicas e realiza funcionalidades (atributos e métodos)
# Os parenteses indicam a presença dos métodos ()