# jegyfoglalas.py
class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglal(self, jarat, utas):
        self.foglalasok.append({"utas": utas, "jarat": jarat})

        print(f"Foglalás: {utas}, {jarat.get_celallomas()} célállomásra {jarat.get_jaratszam()} sorszámra {jarat.get_jegyar()} Forintért.")

    def lemond(self, utas):
        foglalas = next((f for f in self.foglalasok if f["utas"] == utas), None)
        if foglalas:
            self.foglalasok.remove(foglalas)
            print(f"A foglalás törölve!")
        else:
            print(f"Nincs ilyen foglalás! Adjon meg másik nevet!")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsen foglalás.")
        else:
            for foglalas in self.foglalasok:
                jarat = foglalas["jarat"]
                utas = foglalas["utas"]
                print(f"Foglalás: {utas}, járat: {jarat.get_jaratszam()}, célállomás: {jarat.get_celallomas()}, Jegyár: {jarat.get_jegyar()} Forint")
