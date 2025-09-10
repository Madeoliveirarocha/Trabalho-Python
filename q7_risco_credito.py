# Questão 7 - Classificação de risco de crédito
idade = int(input("Idade: "))
renda = float(input("Renda mensal: ").replace(",", "."))
dividas = float(input("Total de dívidas: ").replace(",", "."))

if renda <= 0:
    print("Risco não pode ser calculado (renda inválida).")
else:
    perc_dividas = (dividas / renda) * 100

    if renda < 2000 and perc_dividas > 50:
        risco = "Alta"
    elif renda > 5000 and perc_dividas < 30:
        risco = "Baixa"
    elif (2000 <= renda <= 5000) or (30 <= perc_dividas <= 50):
        risco = "Média"
    else:
        risco = "Médio-baixo"

    print(f"Renda: R$ {renda:.2f} | Dívidas: R$ {dividas:.2f} ({perc_dividas:.1f}%) → Risco {risco}")
