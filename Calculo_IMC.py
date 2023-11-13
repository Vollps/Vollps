

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
print("Seu IMC é: ", imc)

