# Questão 4 - Média de 3 provas com regra de reprovação automática
notas = []
for i in range(1, 4):
    n = float(input(f"Nota {i} (0 a 10): ").replace(",", "."))
    notas.append(n)

if any(n == 0 for n in notas):
    print("Reprovado automático (houve nota 0).")
else:
    media = sum(notas) / 3
    if media >= 7:
        print(f"Média = {media:.2f} → Aprovado")
    elif media >= 5:
        print(f"Média = {media:.2f} → Recuperação")
    else:
        print(f"Média = {media:.2f} → Reprovado")
