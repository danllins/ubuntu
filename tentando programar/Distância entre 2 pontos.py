import math

x1 = int(input("Digite um numero para x1:"))
y1 = int(input("Digite um numero para y1:"))
x2 = int(input("Digite um numero para x2:"))
y2 = int(input("Digite um numero para y2:"))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Distância entre P1 e P2 é:", d)
