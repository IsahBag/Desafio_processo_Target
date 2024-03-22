''' Exercício 03 - Descubra a lógica e complete o próximo elemento:'''

# a) 1, 3, 5, 7, ___

def sequencia_a(n):
    return [2*i + 1 for i in range(n)]

resultado = sequencia_a(5)
print(resultado)

# b) 2, 4, 8, 16, 32, 64, ___
    
def sequencia_b(n):    
    return [2**i for i in range(1, n+1)]

resultado = sequencia_b(7)
print(resultado)

# c) 0, 1, 4, 9, 16, 25, 36, ____

def sequencia_c(n):   
    return [i**2 for i in range(n+1)]

resultado = sequencia_c(7)
print(resultado)


# d) 4, 16, 36, 64, ____

def sequencia_d(n):
    return [(2*i)**2 for i in range(1, n+1)]

resultado = sequencia_d(5)
print(resultado)


# e) 1, 1, 2, 3, 5, 8, ____

def sequencia_e(n):
    sequence = [1, 1]
    n1, n2 = 1, 1
    
    while len(sequence) < n:
        prox = n1 + n2
        sequence.append(prox)
        n1, n2 = n2, prox
    
    return sequence

resultado = sequencia_e(7)
print(resultado)

# f) 2,10, 12, 16, 17, 18, 19, ____

