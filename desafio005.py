
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

numero = int(input('Digite um número: '))

print('O antecessor de {} é: {}'.format(numero, numero -1))
print('O sucessor de {} é: {}'.format(numero, numero + 1))


## Exemplo com mais variáveis

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('O antecessor de {} é: {}'.format(numero, antecessor))
print('O sucessor de {} é: {}'.format(numero, sucessor))

# Quanto menos variáveis menos uso de memória
