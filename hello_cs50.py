"""Exercício introdutório de Python inspirado no CS50.

O programa recebe um nome pelo terminal e exibe uma saudação formatada.
"""


def saudacao_academica() -> None:
    """Solicita um nome e exibe uma saudação."""
    print("=" * 50)
    print("HARVARD CS50 — PYTHON")
    print("=" * 50)

    nome = input("Digite seu nome completo: ").strip()

    if not nome:
        print("Erro: informe um nome válido.")
        print("=" * 50)
        return

    nome_formatado = nome.title()

    print("-" * 50)
    print(f"Olá, {nome_formatado}!")
    print("Bem-vindo ao seu laboratório de estudos de Ciência da Computação.")
    print("=" * 50)


if __name__ == "__main__":
    saudacao_academica()
