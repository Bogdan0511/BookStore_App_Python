class Carte(object):
    def __init__(self, id, titlu, autor, an):
        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__an = an

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_autor(self):
        return self.__autor

    def get_an(self):
        return self.__an

    def __str__(self):
        return "ID: " + str(self.get_id()) + " Titlu: " + self.get_titlu() + " Autor: " + self.get_autor() + " An: " + str(self.get_an())

    def __eq__(self, other):
        return self.get_id() == other.get_id()