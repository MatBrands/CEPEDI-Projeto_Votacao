class Votacao:
    def __init__(self, organizador):
        self.organizador = organizador
        self.candidatos = []
        self.__votos__ = []
        self.votantes = []
        self.__Empate__ = False 
        self.__votacaoDisponivel__ = True
        self.vencedor = None

# ---------------------------------------------
    
    def setCandidato(self, candidato):
        if self.getVotacaoDisp():
            self.candidatos.append(candidato)
            self.__votos__.append(0)
            return True
        return False

    def getCandidatos(self):
        return self.candidatos

    def getVencedor(self):
        return self.vencedor

    def getVotacaoDisp(self):
        return self.__votacaoDisponivel__

    def getVotantes(self):
        return self.votantes

    def setEmpate(self):
        self.__Empate__ = True

    def getEmpate(self):
        return self.__Empate__

# ---------------------------------------------

    def iniciarVotacao(self):
        self.__votacaoDisponivel__ = False

    def verificaOrganizador(self, user):
        return self.organizador.getUser() == user

    def votar (self, id_candidato, eleitor):
        if not eleitor in self.votantes:
            self.__votos__[id_candidato] += 1
            self.votantes.append(eleitor)
        else:
            return

    def encerrarVotacao(self, user):
        if not self.__votacaoDisponivel__ and self.verificaOrganizador(user):
            contagemDoVencedor = 0;       
            valor_empate = -1

            for i, item in enumerate(self.__votos__):
                if (item > contagemDoVencedor):
                    contagemDoVencedor = item
                    vencedor = i
                elif(item == contagemDoVencedor):
                    valor_empate = contagemDoVencedor

            if valor_empate != -1:
                self.setEmpate()
                return False
                
            self.vencedor = self.candidatos[vencedor], contagemDoVencedor
            return True
        else:
            return False