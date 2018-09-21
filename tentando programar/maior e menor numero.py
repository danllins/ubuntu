a = int(input("informe valor de a:"))
b = int(input("informe valor de b:"))
c = int(input("informe valor de c:"))

if a > b > c:
    print("O maior valor é:", a)
    print("O menor número é:", c)

if a > c > b:
    print("O maior valor é:", a)
    print("O menor número é:", b)

if b > a > c:
    print("O maior valor é:", b)
    print("O menor número é:", c)

if b > c > a:
    print("O maior valor é:", b)
    print("O menor número é:", a)

if c > a > b:
    print("O maior valor é:", c)
    print("O menor número é:", b)

if c > b > a:
    print("O maior valor é:", c)
    print("O menor número é:", a)

if a == b == c:
    print("os valores são iguais")

if a == b > c:
    print("O maior valor é:", a, ",", b)
    print("O menor número é:", c)

if a == b < c:
    print("O maior valor é:", c)
    print("O menor número é:", a, ",", b)

if b == c < a:
    print("O maior valor é:", a)
    print("O menor número é:", b, ",", c)

if b == c > a:
    print("O maior valor é:", b, ",", c)
    print("O menor número é:", a)

if c == a < b:
    print("O maior valor é:", b)
    print("O menor número é:", a, ",", c)

if c == a > b:
    print("O maior valor é:", a, ",", c)
    print("O menor número é:", b)
