# belfoldijarat.py
from jarat import Jarat

class belfodijarat(Jarat):
    def __init__(self, jaratszam, cel, ar):
        super().__init__(jaratszam, cel, ar)

    def get_tipus(self):
        return "Belföldi járatok"
