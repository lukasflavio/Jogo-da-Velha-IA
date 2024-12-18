# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):

        # Regra 1 : Verificação de possibilidade de vitória
        for l in range(3):
            soma_linha = 0
            for c in range(3):
                soma_linha += self.matriz[l][c]
            if soma_linha == 2:
                for c in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        for c in range(3):
            soma_coluna = 0
            for l in range(3):
                soma_coluna += self.matriz[l][c]
            if soma_coluna == 2:
                for l in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        soma_diagonal_principal = 0
        soma_diagonal_secundaria = 0
        for i in range(3):
            soma_diagonal_principal += self.matriz[i][i]
            soma_diagonal_secundaria += self.matriz[i][2 - i]

        if soma_diagonal_principal == 2:
            for i in range(3):
                if self.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                    return (i, i)

        if soma_diagonal_secundaria == 2:
            for i in range(3):
                if self.matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                    return (i, 2 - i)

        # Regra 2 : 
        for l in range(3):
            soma_linha = 0
            for c in range(3):
                soma_linha += self.matriz[l][c]
            if soma_linha == 8:
                for c in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        for c in range(3):
            soma_coluna = 0
            for l in range(3):
                soma_coluna += self.matriz[l][c]
            if soma_coluna == 8:
                for l in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        soma_diagonal_principal = 0
        soma_diagonal_secundaria = 0
        for i in range(3):
            soma_diagonal_principal += self.matriz[i][i]
            soma_diagonal_secundaria += self.matriz[i][2 - i]

        if soma_diagonal_principal == 8:
            for i in range(3):
                if self.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                    return (i, i)

        if soma_diagonal_secundaria == 8:
            for i in range(3):
                if self.matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                    return (i, 2 - i)

        # Regra 3: 
        for l in range(3):
            soma_linha = 0
            for c in range(3):
                soma_linha += self.matriz[l][c]
            if soma_linha == 1:
                for c in range(3):
                    soma_coluna = 0
                    for l2 in range(3):
                        soma_coluna += self.matriz[l2][c]
                    if soma_coluna == 1 and self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        # Regra 4: 
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # Regra 5: 
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
                l_oposto, c_oposto = 2 - l, 2 - c
                if self.matriz[l_oposto][c_oposto] == Tabuleiro.DESCONHECIDO:
                    return (l_oposto, c_oposto)

        # Regra 6: 
        cantos_disponiveis = []
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                cantos_disponiveis.append((l, c))

        if len(cantos_disponiveis) > 0:
            indice = randint(0, len(cantos_disponiveis) - 1)
            return cantos_disponiveis[indice]

        # Escolher qualquer posição aleatória
        posicoes_disponiveis = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    posicoes_disponiveis.append((l, c))

        if len(posicoes_disponiveis) > 0:
            indice = randint(0, len(posicoes_disponiveis) - 1)
            return posicoes_disponiveis[indice]

        # Caso nenhuma jogada seja possível
        return None
