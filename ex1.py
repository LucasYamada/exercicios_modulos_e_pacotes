comprimento = float(input())
altura = float(input())
largura = float(input())

volume = (comprimento*largura*altura)*1000
temperatura_ambiente = 10
temperatura_desejada = 15

print("O volume e:", volume,"litros")
print("A potência do termostato deve ser:",volume * 0.05 * (temperatura_desejada - temperatura_ambiente),"watts")
print("A filtragem deve ser de",volume*2,"litros por hora")
