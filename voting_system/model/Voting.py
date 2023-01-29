class Votacao:
    def __init__(self, organizer: str) -> None:
        self.organizer = organizer
        self.candidates = []
        self.__wishes__ = []
        self.already_voted = []
        self.__draw__ = False 
        self.__voting_status__ = True
        self.winner = None

    def register_candidate(self, candidate: str) -> bool:
        if self.voting_status():
            if candidate in self.candidates:
                return False
            self.candidates.append(candidate)
            self.__wishes__.append(0)
            return True
        return False

    def voting_status(self) -> bool:
        return self.__voting_status__

    def draw(self) -> bool:
        return self.__draw__

    def start_voting(self) -> None:
        self.__voting_status__ = False

    def is_owner(self, user: str) -> bool:
        return self.organizer == user

    def vote(self, id_candidate: str, id_voter: str) -> bool:
        if id_voter in self.already_voted:
            return False
        self.__wishes__[id_candidate] += 1
        self.already_voted.append(id_voter)
        return True

    def close_voting(self, user: str) -> bool:        
        if not self.__voting_status__ and self.is_owner(user):
            winner_count = 0;       
            draw_value = -1

            for i, item in enumerate(self.__wishes__):
                if (item > winner_count):
                    winner_count = item
                    winner = i
                elif(item == winner_count):
                    draw_value = winner_count

            if draw_value != -1:
                self.__draw__ = True
                return False
                
            self.winner = self.candidates[winner], winner_count
            return True
        return False