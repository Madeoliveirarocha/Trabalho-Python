# Questão 10 - Validador de senha
# Regras: mínimo 8 caracteres, contém ao menos:
# 1 maiúscula, 1 minúscula, 1 número e 1 símbolo entre !@#$%
import re
senha = input("Digite a senha: ")

regras = [
    (len(senha) >= 8, "mínimo de 8 caracteres"),
    (re.search(r"[A-Z]", senha) is not None, "pelo menos 1 letra maiúscula"),
    (re.search(r"[a-z]", senha) is not None, "pelo menos 1 letra minúscula"),
    (re.search(r"\d", senha) is not None, "pelo menos 1 número"),
    (re.search(r"[!@#$%]", senha) is not None, "pelo menos 1 símbolo entre !@#$%"),
]

faltando = [msg for ok, msg in regras if not ok]
if not faltando:
    print("Senha válida.")
else:
    print("Senha inválida. Faltam: " + "; ".join(faltando))
