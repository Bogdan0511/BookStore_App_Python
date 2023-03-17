from Erori.Exceptii import ValidError, RepoError

class Consola(object):

    def __init__(self, srv):
        self.__srv = srv

    def carti_fisier(self):
        """
        Aceasta functie afiseaza pe ecran toate cartile din fisier
        """
        l = self.__srv.vezi_carti()
        for el in l:
            print(str(el))

    def __adaugare_carte(self):
        """
        Aceasta functie ii cere utilizatorului sa introduca elementele ce compun
        o carte, dupa care apeleaza functia din service care adauga cartea in fisier
        """
        try:
            id = int(input("ID carte: "))
        except ValueError:
            print("ID-ul este un numar intreg pozitiv")
            return
        titlu = input("Titlu carte: ")
        autor = input("Autor carte: ")
        try:
            an = int(input("An aparitie carte: "))
        except ValueError:
            print("Anul aparitie este un numar intreg pozitiv")
            return
        self.__srv.adauga_carte(id, titlu, autor, an)

    def __sterge_carti(self):
        """
        Aceasta functie ii cere utilizatorului o cifra, dupa care
        apeleaza functia din service care sterge acele carti care au in an cifra introdusa
        """
        try:
            cifra = int(input("Cifra cautata in anii de aparitie ai cartilor: "))
        except ValueError:
            print("Aceasta nu este o cifra!")
            return
        if cifra < 0 or cifra > 9:
            print("Aceasta nu este o cifra")
            return
        self.__srv.sterge_carte(cifra)

    def __filtreaza_cartile(self):
        str = input("Sirul cautat in titlul cartilor: ")
        try:
            an = int(input("Anul maxim de aparitie al cartilor"))
        except ValueError:
            print("Anul trebuie sa fie un intreg pozitiv")
            return
        self.__srv.filtrare_carti(str, an)

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "":
                continue
            elif cmd == "exit":
                return
            elif cmd == "adauga carte":
                try:
                    self.__adaugare_carte()
                except ValidError as ve:
                    print("Eroare de validare: \n" + str(ve))
                except RepoError as re:
                    print("Eroare de inregistrare: " + str(re))
                self.carti_fisier()
            elif cmd == "sterge carti":
                self.__sterge_carti()
                self.carti_fisier()
            elif cmd == "filtrare carti":
                self.__filtreaza_cartile()
            else:
                print("Comanda invalida! ")
