class Player:
    def __init__(self, sign):
        self.sign = sign
        self.score = 0

    def get_score(self):
        self.score += 1
