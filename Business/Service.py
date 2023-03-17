from Infrastructura.Repository import FileRepo
from Domeniu.Entitati import Carte
from Validare.Validation import Validator
from Erori.Exceptii import RepoError

class ServiceBibl(object):
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo

    def vezi_carti(self):
        """
        Returneaza toate cartile existente in fisier
        """
        return self.__repo.load_from_file()

    def adauga_carte(self, id, titlu, autor, an):
        """
        Are ca parametrii elementele unei carti
        Creeaza cartea cu parametrii primiti, o valideaza, iar apoi o adauga in fisier
        """
        carte = Carte(id, titlu, autor, an)
        self.__valid.valideaza(carte)
        try:
            self.__repo.store(carte)
        except RepoError as re:
            print("Eroare de inregistrare: " + str(re))

    def sterge_carte(self, cifra):
        """
        Are ca parametru o cifra
        Elimina toate cartile care au in anul aparitiei acea cifra
        """
        l = self.__repo.load_from_file()
        rez = []
        for el in l:
            an = int(el.get_an())
            i = 0
            while an > 0:
                cf = an % 10
                if cf == cifra:
                    i = i + 1
                an = an // 10
            if i == 0:
                rez.append(el)
        self.__repo.store_to_file(rez)

    def filtrare_carti(self, str, an):
        """
        Parametrii acestei functii sunt un sir si un an
        Functia cauta in cartile din fisier acele carti care contin in titlu sirul specificat si au anul de
        aparitie mai mic decat anul specificat
        """
        l = self.__repo.load_from_file()
        rez = []
        for el in l:
            if str in el.get_titlu() and int(an) >= int(el.get_an()):
                rez.append(el)
        if len(rez) == 0:
            print("Nu exista astfel de carti!")
        else:
            print(str)
            print(an)
            for ele in rez:
                print(ele)



