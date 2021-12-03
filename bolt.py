


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self, ):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        try:
            with open(filepath, "r", encoding="UTF-8") as fajl:
            lista = [sor.strip() for sor in fajl]
            return lista
        except FileNotFoundError:
            print("error")

    def feladat_1(self, filepath: str) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: C:\Users\sbert\PycharmProjects\zh2\kosar.txt
        A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        termekek = []
        for i in range(len(lista)):
            if lista[i] not in termekek:
                termekek.append(lista[i])
        termekek.remove("F")
        return termekek
        pass

    def feladat_2(self) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        f = 0
        for i in range(len(lista)):
            if lista[i] == "F":
                f += 1
        print(f'2. Feladat : {f} alkalommal fizettek a pénztárnál.')
        pass

    def feladat_3(self) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        try:
            vasarlas_szama = int(input("Adja meg a vásárlás sorozat számát:"))
            f_indexek = [0]
            aru = []
            for i in range(len(lista)):
                if lista[i] == "F":
                    f_indexek.append(i)
            if vasarlas_szama == 0:
                aru.append(lista[0])
        else:
        i = f_indexek[vasarlas_szama] + 1
        while i < len(lista):
            aru.append(lista[i])
            i += 1
            if lista[i] == "F":
                break

    osszeg = 0
    aru = sorted(aru)
    ismetles = 0
    for i in range(len(aru)):
        if aru[i] in aru:
            osszeg += 1000

    print("3. Feladat. A kosár tartalma:\n", aru)
    print("Összege:", osszeg)
    print(ismetles)

except ValueError:
print("nem megfelelő értéket adott meg.")

pass

    def feladat_4(self) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        print(termekek(lista))
        f_indexek = [0]
        for i in range(len(lista)):
            if lista[i] == "F":
                f_indexek.append(i)
        termek = str(input("Adja meg a termék nevét: "))

        pass

    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        pass
