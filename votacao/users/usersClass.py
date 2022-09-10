class Votante:
    def __init__(self, id: int, user: str, password: str, name: str):
        self.setUser(user)
        self.setPassword(password)
        self.setId(id)
        self.setName(name)
        self.setVotou(False)
        

    def getUser(self):
        return self.__user__

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getId(self):
        return id
    
    def setId(self, id):
        self.__id__ = id

    def validarPassword(self, passwd: str):
        return (passwd == self.__password__)

    def Votar(self):
        self.__votou__ = True

    @property
    def setUser(self, user):
        self.__user__ = user

    @property
    def setPassword(self, password):
        self.__password__ = password
        
    @property
    def setVotou(self, votou):
        self.__votou__ = votou

class Candidato(Votante):
    def __init__(self, id: int, user: str, password: str, name: str, proposta: str):
        super().__init__(id, user, password, name)
        self.setProposta(proposta)
        self.__contagem_voto__ = 0

    def setProposta(self, proposta):
        self.proposta = proposta

    def getProposta(self):
        return self.proposta

    def setContagem(self):
        self.__contagem_voto__ += 1

    def getContagem(self):
        return self.__contagem_voto__