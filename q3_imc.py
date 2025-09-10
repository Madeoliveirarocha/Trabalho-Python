# Questão 3 - IMC
peso = float(input("Peso (kg): ").replace(",", "."))
altura = float(input("Altura (m): ").replace(",", "."))
imc = peso / (altura ** 2)

if imc < 18.5:
    cls = "abaixo do peso"
elif imc < 25:
    cls = "peso normal"
elif imc < 30:
    cls = "sobrepeso"
elif imc < 35:
    cls = "obesidade grau I"
elif imc < 40:
    cls = "obesidade grau II"
else:
    cls = "obesidade grau III"

print(f"IMC = {imc:.1f} → {cls}")
