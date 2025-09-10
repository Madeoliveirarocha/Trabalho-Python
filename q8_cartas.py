# Questão 8 - Jogo das cartas
# Ordem correta: para A,B,C,D → B,C,D,A (índice-posição)
correta = ['B', 'C', 'D', 'A']

entrada = input("Digite sua sequência de 4 cartas (ex.: A B C D): ").strip().upper()
seq = [ch for ch in entrada.replace(",", " ").split() if ch]
if len(seq) == 1 and len(seq[0]) == 4:
    seq = list(seq[0])

# Garante 4 itens
if len(seq) != 4 or any(c not in ['A','B','C','D'] for c in seq):
    print("Sequência inválida. Use 4 cartas entre A, B, C, D.")
else:
    pontos = 0
    for i in range(4):
        if seq[i] == correta[i]:
            pontos += 10

    if 'A' in seq:
        pontos += 5

    tem_cd = any(seq[i] == 'C' and seq[i+1] == 'D' for i in range(3))
    if tem_cd:
        pontos += 5

    pontos = min(pontos, 50)

    print(f"Pontuação: {pontos}/50")
