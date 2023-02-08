# OPERADORES
# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potência **
# Divisão inteira//   resultado da divisão sem virgula
# Módulo %           resto da divisão inteira

# TODOS SÃO OPERADORES ARITMÉTICOS (ACEITA NÚMEROS OU VARIÁVEIS) BINÁRIOS, OU SEJA, PRECISAM DE DOIS OPERANDOS PARA EXECUTAR
# O SÍMBOLO DE IGUALDADE EM PYTHON É REPRESENTADO POR DOIS SÍMBOLOS DE IGUAL ==

# ORDEM DE PRECEDÊNCIA DOS OPERADORES ARITMÉTICOS

#1 Parenteses ()
#2 Potência **
#3 * / // %    Não importa a ordem, faça o que aparecer primeiro
#4 Adição e subtração + -


## Exemplo 1

# 5 + 3 * 2
# 5 + 6
# 11

a = 5
b = 3
c = 2

expressao = a + b * c

print('O resultado da expressão é: {}'.format(expressao))

## Exemplo 2

# 3 * 5 + 4 ** 2
# 3 * 5 + 16
# 15 + 16
# 31

a = 3
b = 5
c = 4
d = 2

expressao = a * b + c ** d

print('O resultado da expressão é: {}'.format(expressao))

## Exemplo 3
# 3 * (5 + 4) ** 2
# 3 * 9 ** 2
# 3 * 81
# 243

a = 3
b = 5
c = 4
d = 2

expressao = a * (b + c) ** d

print('O resultado da expressãao é: {}'.format(expressao))

## Exemplo 4 - outra forma de fazer a potência sem utilizar **
# 5**2
# 25

a = 5
b= 2

expressao = pow(a, b) #pow é a função de potência

print('O resultado da potência é: {}'.format(expressao))

## Exemplo 5 - Concatenação

# Oi + Olá
# OiOlá

a = 'Oi'
b = 'Olá'

expressao = a + b

print('O resultado da expressão é: {}'.format(expressao))

## Exemplo 6 

# oi * 5
# oioioioioi

a = 'oi'  # Se o valor da variável for uma string (letras) ela deve estar entre aspas simples.
b = 5

expressao = a * b

print('O resultado da expressão é: {}'.format(expressao))

## Exemplo 7

# '=' * 20

a = '='
b = 20

expressao = a * b

print('O resultado da expressão é: {}'.format(expressao))

## Exemplo 8 - raíz quadrada, cubica etc

a = 25 #raiz quadrada
b = (1/2)
# 25**(1/2) 


raizQuadrada = a ** (b)
print('A raíz quadrada de {} é igual a {}'.format(a, raizQuadrada))

c = 81 #raiz cubica
d = (1/3)
# 81**(1/3)


raizCubica = c ** (d)
print('A raiz cúbica de {} é igual a {}'.format(c, raizCubica))


## Exemplo 9

nome = input('Digite seu nome: ')

print('Prazer em te conhecer {}'.format(nome)) 








