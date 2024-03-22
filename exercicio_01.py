''' Exercício 01 - Observe o trecho de código abaixo:
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}
imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?'''

soma = 0
k = 0

for i in range (13):
    k += 1
    soma += k

print(f"O valor da variável SOMA é: {soma}")