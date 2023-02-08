# Crie um algoritmo que leia um número que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = float(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print('O dobro de {} é igual a: {}'.format(numero, dobro))
print('O triplo de {} é igual a: {}'.format(numero, triplo))
print('A raiz quadrada de {} é igual a: {}'.format(numero, raizQuadrada))