altura = float(input())
peso = float(input())

imc = peso/(altura*altura)

if imc < 18.5:
    print("Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Excesso de peso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade de Classe 1")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade de Classe 2")
elif imc >= 40:
    print("Obesidade de Classe 3")

if imc < 18.5:
    peso_ideal = 18.5 * (altura ** 2)
    print("Você deve ganhar", round(peso_ideal - peso, 2), "quilos")
elif imc >= 25:
    peso_ideal = 24.9 * (altura ** 2)
    print("Você deve perder", round(peso - peso_ideal, 2), "quilos")

