# Questão 2 - Classificação de triângulo
a = float(input("Lado A: ").replace(",", "."))
b = float(input("Lado B: ").replace(",", "."))
c = float(input("Lado C: ").replace(",", "."))

if a <= 0 or b <= 0 or c <= 0:
    print("Não forma triângulo (lado inválido).")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Não forma triângulo.")
else:
    if a == b == c:
        print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
