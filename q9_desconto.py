# Questão 9 - Preço com desconto + VIP
preco = float(input("Preço do produto: ").replace(",", "."))
vip = input("Cliente VIP? (s/n): ").strip().lower() in ("s", "sim", "y", "yes")

if preco >= 100:
    desc = 0.20
elif preco >= 50:
    desc = 0.10
else:
    desc = 0.0

if vip:
    desc += 0.05

preco_final = preco * (1 - desc)
print(f"Desconto total: {desc*100:.0f}% → Preço final: R$ {preco_final:.2f}")
