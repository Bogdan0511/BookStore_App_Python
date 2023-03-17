from Domeniu.Entitati import Carte
from Validare.Validation import Validator
from Erori.Exceptii import ValidError
from Infrastructura.Repository import FileRepo
from Business.Service import ServiceBibl

class Teste(object):

    def __test_creeaza_carte(self):
        id = 1
        titlu = "Ceva"
        autor = "Cineva"
        an = 2005
        carte = Carte(id, titlu, autor, an)
        assert(carte.get_id() == 1)
        assert(carte.get_titlu() == "Ceva")
        assert(carte.get_autor() == "Cineva")
        assert(carte.get_an() == 2005)

    def __test_valideaza_carte(self):
        id = 1
        titlu = "Carte"
        autor = ""
        an = 1000
        carte_rea = Carte(id, titlu, autor, an)
        valid = Validator()
        try:
            valid.valideaza(carte_rea)
            assert(False)
        except ValidError as ve:
            assert(str(ve) == "Autor carte invalid!\n")

    def __test_adauga_carte(self):
        repo = FileRepo()
        valid = Validator()
        srv = ServiceBibl(valid, repo)
        id = 20
        titlu = "Comoara"
        autor = "Viorel"
        an = 2010
        srv.adauga_carte(id, titlu, autor, an)
        l = repo.load_from_file()
        el = l.pop()
        assert(int(el.get_id()) == 20)
        assert(el.get_titlu() == "Comoara")
        assert(el.get_autor() == "Viorel")
        assert(int(el.get_an()) == 2010)
        repo.store_to_file(l)

    def __test_filtreaza_carti(self):
        str = "nimic"
        an = 100
        repo = FileRepo()
        valid = Validator()
        srv = ServiceBibl(valid, repo)
        srv.filtrare_carti(str, an)
        assert(True)

    def run_all_tests(self):
        print("Testele au inceput")
        self.__test_creeaza_carte()
        self.__test_valideaza_carte()
        self.__test_adauga_carte()
        print("Testele s-au incheiat")
