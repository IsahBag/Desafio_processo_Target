'''Exercício 05 - Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def separar_letras(palavra):
    letras = []
    for letra in palavra:
        letras.append(letra)
    return letras

def inverter_letras(letras):
    palavra_inv = []
    for i in range(len(letras) - 1, -1, -1):
        palavra_inv.append(letras[i])
    return palavra_inv

def formar_palavra_invertida(palavra_inv):
    palavra = ''.join(palavra_inv)
    return palavra

palavra = input("Digite uma palavra: ")

letras = separar_letras(palavra)
letras_invertidas = inverter_letras(letras)
palavra_invertida = formar_palavra_invertida(letras_invertidas)

print("Palavra original:", palavra)
print("Palavra invertida:", palavra_invertida)
        