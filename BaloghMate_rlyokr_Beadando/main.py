# main.py
from legitarsasag import LegiTarsasag
from belfodijarat import belfodijarat
from nemzetkozijarat import nemzetkozijarat
from jegyfoglalas import FoglalasKezelo

def elokeszites():
    legitarsasag = LegiTarsasag("GDE logisztika")
    jarat1 = nemzetkozijarat("GDE5480", "Dubai", 99000)
    jarat2 = nemzetkozijarat("GDE2024", "Párizs", 19000)
    jarat3 = belfodijarat("GDE1016", "Debrecen", 7900)

    legitarsasag.hozzaad_jarat(jarat1)
    legitarsasag.hozzaad_jarat(jarat2)
    legitarsasag.hozzaad_jarat(jarat3)

    foglalas_kezelo = FoglalasKezelo()
    foglalas_kezelo.foglal(jarat1, "Kun Emese")
    foglalas_kezelo.foglal(jarat1, "Kun Sándor")
    foglalas_kezelo.foglal(jarat2, "Balogh Emília")
    foglalas_kezelo.foglal(jarat2, "Baloghné Varga Beáta Éva")
    foglalas_kezelo.foglal(jarat3, "Balogh Máté")
    foglalas_kezelo.foglal(jarat3, "Balogh Lili")


    return legitarsasag, foglalas_kezelo


def felhasznaloi_felulet():
    legitarsasag, foglalas_kezelo = elokeszites()

    while True:
        print("\nMenü")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        menu = input("\nVálasszon egy lehetőséget: ")

        if menu == '1':
            utas = input("Kérem az utas nevét: ")
            jaratszam = input("Kérem a járatszámot (GDE1016 GDE2024 GDE5480): ")
            jarat = next((j for j in legitarsasag.jaratok if j.get_jaratszam() == jaratszam), None)
            if jarat:
                foglalas_kezelo.foglal(jarat, utas)
            else:
                print("Nincsen ilyen járatszám!")
        elif menu == '2':
            utas = input("Kérem az utas nevét: ")
            foglalas_kezelo.lemond(utas)
        elif menu == '3':
            foglalas_kezelo.listaz_foglalasok()
        elif menu == '4':
            print("Viszontlátásra!")
            break
        else:
            print("Hibás menüpont! Próbálja újra!")


if __name__ == "__main__":
    felhasznaloi_felulet()
