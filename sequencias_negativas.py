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

import re
import sys
import os

# Configuracao de cores para diferentes sistemas operacionais
if sys.platform == 'win32':
    import colorama
    colorama.init(autoreset=True)
    from colorama import Fore, Style
else:
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
COD = {
    'A':1,'I':1,'Q':1,'J':1,'Y':1,'B':2,'K':2,'R':2,
    'C':3,'G':3,'L':3,'S':3,'D':4,'M':4,'T':4,
    'E':5,'H':5,'N':5,'U':6,'V':6,'W':6,'X':6,
    'O':7,'Z':7,'F':8,'P':8
}

# Descricoes resumidas e objetivas das sequencias negativas
DESCRICOES = {
    1: '''111 – A pessoa fica limitada, perdendo a coragem de se aventurar em algo novo. Pode, também, ficar um longo período inativo (a), desempregado (a) ou mesmo impotente para realizar o que quer que seja permanecendo nesse estado o tempo que durar o Arcano que domina o período. Esta sequência indica, eventualmente, tendência para desenvolver alguns distúrbios ou doenças cardíacas.''',
    2: '''222 – Esta sequência indica possibilidade de timidez e indecisão, podendo levar o (a) seu (a) possuidor (a) a ser subjugado (a) por aqueles mais próximos, sejam eles amigos, sócios, colegas de trabalho ou simplesmente conhecidos. Faz perder a autoestima, limitando-o (a) quanto a seus projetos e realizações. Pode, eventualmente, surgir alguma doença que provoque dependência.''',
    3: '''333 – Indica possibilidade de ser incompreendido (a), dificuldade no diálogo, principalmente com colegas de trabalho e com a (o) companheira (o). Tem dificuldade de se impor em seus projetos e para convencer as pessoas. Esta sequência pode, eventualmente, indicar possibilidade de doenças respiratórias ou de articulações.''',
    4: '''444 – Reflete dificuldade na realização profissional. Pode ser mal remunerado (a) e as perspectivas profissionais serem difíceis, ou ter dificuldade em se manter no emprego, ou se dar bem em qualquer atividade. Pode, eventualmente, indicar possibilidade de doenças reumáticas ou arteriais.''',
    5: '''555 – Indica possíveis mudanças não desejadas de casa, de profissão ou meio social. Sob esta influência, a pessoa tem frequentes altos e baixos, não se fixando profissionalmente, sempre à procura de melhores oportunidades, e ter dificuldade para as encontrar. Pode, também, causar fuga do meio social em que habita e a desenvolver alguma doença de pele.''',
    6: '''666 – Indica possibilidade de haver decepções com amigos, sócios, parentes e até com o cônjuge (namorada (o) ou companheira (o)), que não o (a) compreende em seus propósitos e sentimentos. Algum tipo de doença cardíaca pode aparecer nesse estado.''',
    7: '''777 – Faz com que se afaste de tudo e de todos. Pode levar ao desmando, transforma-lo (a) em um ser dependente, vaidoso (a), arrogante e, consequentemente, vítima da própria intolerância. A persistência nesse sentimento provoca sentimentos de solidão, doenças nervosas, dependências e, eventualmente, algum tipo de câncer.''',
    8: '''888 – Esta sequência torna arredio (a), afastando-o (a) das atividades sociais. Caso não seja evoluído (a) espiritualmente, poderá descontrolar-se emocionalmente com muita facilidade. Sob esta vibração, poderá oscilar entre a riqueza e a pobreza e, como consequência desse estresse, poderá desenvolver alguma doença.''',
    9: '''999 – Reflete uma tendência a passar por dificuldades financeiras, eventualmente perdas de bens, eventuais fracassos nos negócios e vários tipos de provações provocadas pelos períodos de estagnação. Tudo isto pode afetar o sistema nervoso e o coração.'''
}
def reduzir(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def piramide(nome):
    nome_limpo = re.sub(r'[^A-Za-z]', '', nome).upper()
    nums = [COD.get(l, 0) for l in nome_limpo]
    
    if not nums:
        return []
    
    resultado = [nums[:]]
    
    while len(nums) > 1:
        nums = [reduzir(nums[i] + nums[i+1]) for i in range(len(nums)-1)]
        resultado.append(nums[:])
    
    return resultado

def sequencia_3(nivel):
    seq = []
    i = 0
    while i < len(nivel) - 2:
        if nivel[i] == nivel[i+1] == nivel[i+2]:
            seq.append((i, nivel[i]))
            i += 3
        else:
            i += 1
    return seq

def main():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    
    print("")
    # Entrada do usuario
    nome = input("Nome: ").strip()
    
    if not nome:
        print("\nNome vazio! Encerrando...")
        sys.exit(0)
    
    nome_sem_espacos = nome.replace(" ", "")
    pi = piramide(nome_sem_espacos)
    
    if not pi:
        print("\nNenhum caractere valido encontrado!")
        sys.exit(0)
    
    # Exibe o nome com espacos
    print()
    nome_com_espacos = ' '.join(nome_sem_espacos.upper())
    print(nome_com_espacos)
    
    # Exibe a piramide com destaque em vermelho
    for nivel in pi:
        seq = sequencia_3(nivel)
        linha = []
        i = 0
        
        while i < len(nivel):
            if any(s[0] == i for s in seq):
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i]}{Style.RESET_ALL}")
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i+1]}{Style.RESET_ALL}")
                linha.append(f"{Fore.RED}{Style.BRIGHT}{nivel[i+2]}{Style.RESET_ALL}")
                i += 3
            else:
                linha.append(str(nivel[i]))
                i += 1
        
        espacos = " " * (len(pi[0]) - len(nivel))
        print(f"{espacos}{' '.join(linha)}")
    
    # Exibe apenas as sequencias encontradas (sem duplicatas)
    print()
    sequencias_unicas = []
    for nivel in pi:
        seq = sequencia_3(nivel)
        for pos, valor in seq:
            if valor not in sequencias_unicas:
                sequencias_unicas.append(valor)
    
    if sequencias_unicas:
        for valor in sequencias_unicas:
            print(DESCRICOES.get(valor, "Descricao nao disponivel"))
            print()
    
    input("\nTecle ENTER para sair...")

if __name__ == "__main__":
    main()