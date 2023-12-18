import random

def adivinhe (X):   
    num_aleatorio = random.randint(1, X)
    adivinhe = 0
    while adivinhe != num_aleatorio:
        adivinhe = int(input(f"Adivinhe o numero entre 1 e {X}:"))
        if adivinhe < num_aleatorio:
            print("Desculpa, tente um numero mais alto!")
        elif adivinhe > num_aleatorio:
            print("Desculpe, tente um numero mais baixo!")

    print(f"Parabens, você adivinhou o numero {num_aleatorio}")

adivinhe(10)
