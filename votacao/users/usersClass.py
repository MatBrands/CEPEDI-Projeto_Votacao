class Pessoa:
    def __init__(self, id: int, user: str, password: str, name: str):
        self.setUser(user)
        self.setPassword(password)
        self.setId(id)
        self.setName(name)

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

    @property
    def setUser(self, user):
        self.__user__ = user

    @property
    def setPassword(self, password):
        self.__password__ = password

class Votante(Pessoa):
    def __init__(self, id: int, user: str, password: str, name: str):
        super().__init__(id, user, password, name)
        self.__votou__ = False

    def Votar(self):
        self.__votou__ = True

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