# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):

        # Verificando linhas
        for l in range(3):  
            soma_linha = sum(self.matriz[l])  
            if soma_linha == 3:               
                return Tabuleiro.JOGADOR_0
            elif soma_linha == 12:           
                return Tabuleiro.JOGADOR_X
        
        # Verificando colunas
        for c in range(3): 
            soma_coluna = sum(self.matriz[l][c] for l in range(3))  
            if soma_coluna == 3:                
                return Tabuleiro.JOGADOR_0
            elif soma_coluna == 12:             
                return Tabuleiro.JOGADOR_X

        # Verificando diagonais
        soma_diagonal_principal = sum(self.matriz[i][i] for i in range(3))     
        soma_diagonal_secundaria = sum(self.matriz[i][2 - i] for i in range(3)) 
        if soma_diagonal_principal == 3 or soma_diagonal_secundaria == 3:    
            return Tabuleiro.JOGADOR_0
        elif soma_diagonal_principal == 12 or soma_diagonal_secundaria == 12: 
            return Tabuleiro.JOGADOR_X

        # Se nenhuma das condições for atendida
        return Tabuleiro.DESCONHECIDO