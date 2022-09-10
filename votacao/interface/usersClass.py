class Eleitor:
    def __init__(self, id: int, user: str, password: str, name: str):
        self.setUser(user)
        self.setPassword(password)
        self.setId(id)
        self.setName(name)
        self.__votou__ = False

    def setUser(self, user):
        self.__user__ = user

    def getUser(self):
        return self.__user__

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setId(self, id):
        self.__id__ = id

    def getId(self):
        return self.__id__

    def getVotou(self):
        return self.__votou__

    def setPassword(self, password):
        self.__password__ = password

# -------------------------------------------

    def validarPassword(self, passwd: str):
        return (passwd == self.__password__)

    def Votar(self):
        self.__votou__ = True

class Candidato(Eleitor):
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