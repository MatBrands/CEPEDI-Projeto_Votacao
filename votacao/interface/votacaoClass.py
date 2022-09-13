from usersClass import *

class Votacao:
    def __init__(self, organizador):
        self.organizador = organizador
        self.candidatos = []
        self.__Empate__ = False 
        self.__votacaoDisponivel__ = True
        self.vencedor = None

# ---------------------------------------------
    
    def setCandidato(self, candidato):
        if self.getVotacaoDisp() and type(candidato) is Candidato:
            self.candidatos.append(candidato)
            return True
        return False

    def getVotacaoDisp(self):
        return self.__votacaoDisponivel__

    def setEmpate(self):
        self.__Empate__ = True

# ---------------------------------------------

    def iniciarVotacao(self):
        self.__votacaoDisponivel__ = False

    def verificaOrganizador(self, user):
        return self.organizador.getUser() == user

    def votar (self, id_candidato, eleitor):
        if not eleitor.getVotou():
            self.candidatos[id_candidato].setContagem()
            eleitor.Votar()
        else:
            return

    def encerrarVotacao(self, user):
        if not self.__votacaoDisponivel__ and self.verificaOrganizador(user):
            contagemDoVencedor = 0;       
            valor_empate = -1

            for i, item in enumerate(self.candidatos):
                if (item.getContagem() > contagemDoVencedor):
                    contagemDoVencedor = item.getContagem()
                    vencedor = i
                elif(item.getContagem() == contagemDoVencedor):
                    valor_empate = contagemDoVencedor

            if valor_empate != -1:
                self.setEmpate()
                self.vencedor = -2
                
            self.vencedor = self.candidatos[vencedor]