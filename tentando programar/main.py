import math

a = int(input("informe valor de a:"))
b = int(input("informe valor de b:"))
c = int(input("informe valor de c:"))

delta = b * b - 4 * a * c

print("delta:", delta)

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Raiz x1:", x1)
    print("Raiz x2:", x2)
else:
    print("Não existem raízes reais")
