# nemzetkozijarat.py
from jarat import Jarat

class nemzetkozijarat(Jarat):
    def __init__(self, jaratszam, celallomas, ar):
        super().__init__(jaratszam, celallomas, ar)

    def get_tipus(self):
        return "Nemzetközi járatok"
