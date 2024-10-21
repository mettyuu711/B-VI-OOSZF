# jarat.py
from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.__jaratszam = jaratszam
        self.__celallomas = celallomas
        self.__jegyar = jegyar

    def get_jaratszam(self):
        return self.__jaratszam

    def get_celallomas(self):
        return self.__celallomas

    def get_jegyar(self):
        return self.__jegyar

    @abstractmethod
    def get_tipus(self):
        pass

    def __str__(self):
        return f"{self.get_tipus()}, járatszám: {self.get_jaratszam()}, cél: {self.get_celallomas()}, jegyár: {self.get_jegyar()} Forint"
