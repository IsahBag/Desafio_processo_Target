''' Exercício 04 - Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as 
lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor 
controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada
lâmpada?'''

class Interruptor:

    def __init__(self, nome):
        self.nome = nome
        self.status = "desligado"

    def ligar(self):
        self.status = "ligado"

    def desligar(self):
        self.status = "desligado"

    def __str__(self):
        return f"O {self.nome} está {self.status}"

class Sala:
    def __init__(self, nome):
        self.nome = nome
        self.status = "apagada"
        
    def acender(self):
        self.status = "acesa"

    def apagar(self):
        self.status = "apagada"

    def __str__(self):
        return f"A {self.nome} está {self.status}"

interruptor1 = Interruptor("Interruptor 1")
interruptor2 = Interruptor("Interruptor 2")
interruptor3 = Interruptor("Interruptor 3")

sala1 = Sala("Sala 1")
sala2 = Sala("Sala 2")
sala3 = Sala("Sala 3")

# Supondo que os interruptores estejam na sala na 1, e sejam numerados de 1 a 3, temos as seguintes possibilidades:    

# Hipótese 1:    

# Ligar o interruptor 1:
interruptor1.ligar()
print(interruptor1)

# Interruptor 1 acendeu sala 1!
sala1.acender()
print(sala1)

# Ligar o interruptor 2:
interruptor2.ligar()
print(interruptor2)

# Ir até a sala 2 e verificar se está acesa. Caso esteja acesa:    
sala2.acender()
print(sala2)
print("Interruptor 1 = Sala 1 / Interruptor 2 = Sala 2 / Interruptor 3 = Sala 3")

# Caso esteja apagada:
sala2.apagar()
print(sala2)  
sala3.acender()                        
print("Interruptor 1 = Sala 1 / Interruptor 2 = Sala 3 / Interruptor 3 = Sala 2")


# Hipótese 2:
    
# Ligar o interruptor 1:
interruptor1.ligar() 
print(interruptor1)

# Interruptor 1 não acende sala 1! Ligar o interruptor 2:
interruptor2.ligar()
print(interruptor2)
        
# Interruptor 2 acende sala 1!
sala1.acender()
print(sala1)

# Ir na sala 2 verificar se está acesa. Caso esteja acesa:
sala2.acender()
print(sala2)
print("Interruptor 1 = Sala 2 / Interruptor 2 = Sala 1 / Interruptor 3 = Sala 3")

# Caso sala 2 não esteja acesa:
sala2.apagar()
print(sala2)
sala3.acender()
print("Interruptor 1 = Sala 3 / Interruptor 2 = Sala 1 / Interruptor 3 = Sala 2")
    

# Hipótese 3:
    
# Ligar o interruptor 1:
interruptor1.ligar()
print(interruptor1)

# Interruptor 1 não acende sala 1! Ligar interruptor 2:
interruptor2.ligar()
print(interruptor2)

# Interruptor 2 também não acende sala 1! Ligar interruptor 3:
interruptor3.ligar()
print(interruptor3)
sala1.acender()
print(sala1)

# Desligar o interruptor 1:
interruptor1.desligar()    
print(interruptor1)

# Verificar a sala 2. Caso esteje apagada:
sala2.apagar()
print(sala2)
sala3.acender()
print("Interruptor 1 = Sala 2 / Interruptor 2 = Sala 3 / Interruptor 3 = Sala 1")

# Caso esteja acesa:
sala2.acender()
print(sala2)
sala3.apagar()
print("Interruptor 1 = Sala 3 / Interruptor 2 = Sala 2 / Interruptor 3 = Sala 1")