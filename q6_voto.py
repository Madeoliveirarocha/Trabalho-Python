# Questão 6 - Pode votar? (regras simplificadas do enunciado)
idade = int(input("Idade: "))
nacionalidade = input("Nacionalidade (ex.: brasileiro, estrangeiro): ").strip().lower()

if idade < 16:
    resp = "não pode votar"
elif 16 <= idade <= 17:
    resp = "voto opcional"
else:
    if "brasil" in nacionalidade or "brasileir" in nacionalidade:
        resp = "voto obrigatório"
    else:
        resp = "voto opcional"

print(resp)
