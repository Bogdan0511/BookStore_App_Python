from Domeniu.Entitati import Carte
from Erori.Exceptii import RepoError

class FileRepo(object):

    def load_from_file(self):
        """
        Functia de citire din fisier: deschide fisierul, dupa care citeste elementele separate prin virgula de pe fiecare linie
        apoi creeaza o carte cu aceste elemente si o adauga in lista. La final returneaza lista
        """
        try:
            f = open("biblioteca.txt", "r")
        except IOError:
            return []
        carti = []
        line = f.readline().strip()
        while line!="":
            parts = line.split(",")
            id = parts[0]
            titlu = parts[1]
            autor = parts[2]
            an = parts[3]
            carte = Carte(id, titlu, autor, an)
            carti.append(carte)
            line = f.readline().strip()
        return carti

    def store(self, crt):
        """
        Functia care adauga o carte noua in fisier. Verifica daca acea carte nu are ID-ul duplicat cu vreo carte din lista
        iar daca nu, o adauga. La final apeleaza functia de scriere in fisier
        """
        l = self.load_from_file()
        ok = True
        for el in l:
            if int(el.get_id()) == int(crt.get_id()):
                ok = False
        if ok == True:
            l.append(crt)
            self.store_to_file(l)
        else:
            raise RepoError("ID-ul este deja inregistrat")

    def store_to_file(self, carti):
        """
        Primeste ca parametru o lista de carti.
        Functia creeaza cate o linie cu elementele fiecarei carti din lista, dupa care o scrie in fisier
        """
        f = open("biblioteca.txt", "w")
        for el in carti:
            line = str(el.get_id()) + "," + el.get_titlu() + "," + el.get_autor() + "," + str(el.get_an())
            f.write(line + "\n")
        f.close()

