"""
Módulo: CS50 Introduction - Hello World & String Manipulation
Autor: Marcella Bongiolo
Descrição: Primeiro exercício prático documentado para o repositório harvard-cs50.
           Focado em limpeza de inputs e formatação de strings em Python.
"""

def saudacao_academica():
    print("=" * 50)
    print(" 🎓 BEM-VINDO AO HARVARD CS50 (PYTHON TRACK) 🚀")
    print("=" * 50)
    
    # Recebe o nome do usuário e remove espaços em branco extras
    nome = input("Digite seu nome completo: ").strip().title()
    
    print("-" * 50)
    print(f"✨ Olá, {nome}! É um prazer ter você trilhando este caminho de excelência.")
    print("   Computacional thinking and problem-solving unlocked successfully.")
    print("=" * 50)

if __name__ == "__main__":
    saudacao_academica()
