''' Exercício 02 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência
de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def verificacao(num):
    i = 0
    while fibonacci(i) <= num:
        if fibonacci(i) == num:
            return True
        i += 1
    return False

num = int(input("Digite um número: "))

if verificacao(num):
    print(f"O número {num} pertence à sequencia de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequencia de Fibonacci.")