# Questão 1 - Bônus por salário e tempo de empresa
# Entradas: salário (float) e tempo de empresa em anos (int)
# Saída: percentual de bônus e valor do bônus
salario = float(input("Informe o salário do funcionário: ").replace(",", "."))
tempo = int(input("Informe o tempo de empresa (anos): "))

if salario < 2000 and tempo >= 5:
    perc = 0.20
elif salario < 2000 and tempo < 5:
    perc = 0.10
elif salario >= 2000 and tempo >= 5:
    perc = 0.05
else:
    perc = 0.0

bonus = salario * perc
print(f"Bônus: {perc*100:.0f}% (R$ {bonus:.2f})")
