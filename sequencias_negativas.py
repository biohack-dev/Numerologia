#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#===============================================================================
#
# File...........: sequencias_negativas.py
# Title..........: Analisador de Piramide Numerologica com Sequencias Negativas
# Program........: Python Template Code - GNU/Linux
#
# Description....: Este programa calcula e exibe a piramide numerologica de um nome,
#                  destacando sequencias de tres numeros iguais (sequencias negativas)
#                  que indicam pontos de atencao na numerologia cabalistica.
#
# Copyright......: Copyright(c) 2026 / @BIOHACK - HackLab
# License........: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
#
# Author.........: @BIOHACK
# E-Mail.........: b10h4ck.br@protonmail.me
#
# Dependency.....: Python 3.7+
#
# Date...........: 12/07/2026
# Update.........: 12/07/2026
#
# Version........: 1.0.0
#
#===============================================================================
#
# ###########
# # History #
# ###########
#
#     12/07/2026 : Criacao do template
#     12/07/2026 : Implementacao da logica de piramide numerologica
#     12/07/2026 : Adicao de deteccao de sequencias negativas (3 numeros iguais)
#     12/07/2026 : Correcao da reducao de numeros para 1-9
#     12/07/2026 : Adicao de espacamento entre letras do nome
#     12/07/2026 : Testes e validacao do sistema
#
#===============================================================================

import re
import sys
import os

# Configuracao de cores para diferentes sistemas operacionais
if sys.platform == 'win32':
    import colorama
    colorama.init(autoreset=True)
    from colorama import Fore, Style
else:
    # Cores ANSI para Linux/Mac
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        CYAN = '\033[96m'
        RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'
        RESET_ALL = '\033[0m'

# Dicionario de correspondencia letra-numero (Tabela Pitagorica)
# Cada letra do alfabeto e convertida em um numero de 1 a 9
COD = {
    'A':1,'I':1,'Q':1,'J':1,'Y':1,'B':2,'K':2,'R':2,
    'C':3,'G':3,'L':3,'S':3,'D':4,'M':4,'T':4,
    'E':5,'H':5,'N':5,'U':6,'V':6,'W':6,'X':6,
    'O':7,'Z':7,'F':8,'P':8
}

def reduzir(n):
    """
    Reduz um numero para um unico digito entre 1 e 9.
    
    Args:
        n (int): Numero a ser reduzido
        
    Returns:
        int: Numero reduzido entre 1 e 9
        
    Example:
        >>> reduzir(15)
        6  # 1+5 = 6
        >>> reduzir(28)
        1  # 2+8 = 10, 1+0 = 1
    """
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def piramide(nome):
    """
    Constroi a piramide numerologica de um nome.
    
    A piramide e construida da seguinte forma:
    - Primeira linha: numeros correspondentes a cada letra do nome
    - Linhas seguintes: soma dos numeros adjacentes da linha anterior, reduzidos a 1-9
    - Ultima linha: numero final (destino)
    
    Args:
        nome (str): Nome a ser analisado
        
    Returns:
        list: Lista de listas, onde cada sublista representa um nivel da piramide
        
    Example:
        >>> piramide("Ana")
        [[1, 5, 1], [6, 6], [3]]
    """
    # Remove caracteres especiais e converte para maiusculas
    nome_limpo = re.sub(r'[^A-Za-z]', '', nome).upper()
    
    # Converte letras em numeros usando a tabela COD
    nums = [COD.get(l, 0) for l in nome_limpo]
    
    if not nums:
        return []
    
    # Inicializa a piramide com a primeira linha
    resultado = [nums[:]]
    
    # Constroi as linhas seguintes
    while len(nums) > 1:
        nums = [reduzir(nums[i] + nums[i+1]) for i in range(len(nums)-1)]
        resultado.append(nums[:])
    
    return resultado

def sequencia_3(nivel):
    """
    Detecta sequencias de tres numeros iguais em um nivel da piramide.
    
    Sequencias negativas sao pontos de atencao que indicam:
    - Energia bloqueada
    - Desafios a serem superados
    - Licoes importantes
    
    Args:
        nivel (list): Lista de numeros de um nivel da piramide
        
    Returns:
        list: Lista de tuplas (indice, valor) para cada sequencia encontrada
        
    Example:
        >>> sequencia_3([1, 1, 1, 2, 2, 2])
        [(0, 1), (3, 2)]
    """
    seq = []
    i = 0
    while i < len(nivel) - 2:
        if nivel[i] == nivel[i+1] == nivel[i+2]:
            seq.append((i, nivel[i]))
            i += 3  # Pula os 3 numeros da sequencia
        else:
            i += 1
    return seq

# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

def main():
    """
    Funcao principal do programa.
    Gerencia a interface do usuario e a exibicao dos resultados.
    """
    # Limpa a tela para melhor visualizacao
    os.system('cls' if sys.platform == 'win32' else 'clear')
    
    # Cabecalho do programa
    print("="*50)
    print("  ANALISADOR DE PIRAMIDE")
    print("="*50)
    print()
    print("  Sequencias Negativas = 3 numeros iguais")
    print("  indicam pontos de atencao")
    print()
    print("="*50)
    print()
    
    # Entrada do usuario
    nome = input("Nome: ").strip()
    
    if not nome:
        print("\nNome vazio! Encerrando...")
        sys.exit(0)
    
    # Remove espacos para processamento
    nome_sem_espacos = nome.replace(" ", "")
    
    # Limpa a tela para exibir os resultados
    os.system('cls' if sys.platform == 'win32' else 'clear')
    
    # Calcula a piramide
    pi = piramide(nome_sem_espacos)
    
    if not pi:
        print("\nNenhum caractere valido encontrado!")
        sys.exit(0)
    
    # Exibe o nome com espacos entre as letras
    print()
    nome_com_espacos = ' '.join(nome_sem_espacos.upper())
    print(nome_com_espacos)
    print("-"*50)
    
    # Exibe cada nivel da piramide
    for nivel in pi:
        # Detecta sequencias negativas no nivel
        seq = sequencia_3(nivel)
        linha = []
        i = 0
        
        while i < len(nivel):
            # Verifica se o indice atual e inicio de uma sequencia
            if any(s[0] == i for s in seq):
                # Destaca os 3 numeros da sequencia em vermelho
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i]}{Style.RESET_ALL}")
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i+1]}{Style.RESET_ALL}")
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i+2]}{Style.RESET_ALL}")
                i += 3
            else:
                # Numeros normais (sem destaque)
                linha.append(str(nivel[i]))
                i += 1
        
        # Alinha o nivel a direita para formar a piramide
        espacos = " " * (len(pi[0]) - len(nivel))
        print(f"{espacos}{' '.join(linha)}")
    
    print("-"*50)
    print()
    print("  LEGENDA:")
    print(f"  {Fore.RED}Numeros em vermelho = Sequencia Negativa (3 iguais){Style.RESET_ALL}")
    print("  Indicam bloqueios ou desafios a serem superados")
    print()
    
    # Informacoes adicionais sobre sequencias negativas
    print("  INTERPRETACAO:")
    print("  - Sequencias de 3 numeros iguais mostram areas de conflito")
    print("  - Quanto mais sequencias, mais desafios na area")
    print("  - O numero repetido indica a natureza do desafio")
    print()
    
    input("Tecle ENTER para sair...")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()