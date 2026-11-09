"""Exercício introdutório de saudação via terminal."""


def saudar(nome: str) -> str:
    """Retorna uma saudação após validar e limpar o nome."""
    if not isinstance(nome, str):
        raise TypeError("O nome deve ser uma string.")
    nome = nome.strip()
    if not nome:
        raise ValueError("Informe um nome.")
    return f"Olá, {nome}!"


def main() -> None:
    try:
        print(saudar(input("Qual é o seu nome? ")))
    except ValueError as erro:
        print(erro)


if __name__ == "__main__":
    main()
