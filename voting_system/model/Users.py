class Voter:
    def __init__(self, user: str, password: str, name: str, age: int) -> None:
        self.user = user
        self.__password__ = password
        self.age = age
        self.name = name

    def password(self) -> str:
        return self.__password__

    def validate_password(self, passwd: str) -> bool:
        return (passwd == self.__password__)

class Candidate(Voter):
    def __init__(self, user: str, password: str, name: str, age: int, proposal: str):
        super().__init__(user, password, name, age)
        self.proposal = proposal