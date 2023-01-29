class Eleitor:
    def __init__(self, user: str, password: str, name: str, age: int):
        self.setUser(user)
        self.setPassword(password)
        self.setAge(age)
        self.setName(name)

    def setUser(self, user):
        self.__user__ = user

    def getUser(self):
        return self.__user__

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setPassword(self, password):
        self.__password__ = password

    def getPassword(self):
        return self.__password__

# -------------------------------------------

    def validarPassword(self, passwd: str):
        return (passwd == self.__password__)

class Candidato(Eleitor):
    def __init__(self, user: str, password: str, name: str, age: int, proposta: str):
        super().__init__(user, password, name, age)
        self.setProposta(proposta)

    def setProposta(self, proposta):
        self.proposta = proposta

    def getProposta(self):
        return self.proposta