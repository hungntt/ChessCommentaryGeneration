import math


class textUtils:

    @staticmethod
    def isMove(word):
        # Replace this by a regex later
        if "..." in word or (word[-1].isdigit() and len(word) >= 3):
            return True
        else:
            return False
