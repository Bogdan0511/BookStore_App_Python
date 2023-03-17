from Erori.Exceptii import ValidError

class Validator(object):

    def valideaza(self, carte):
        err = ""
        if carte.get_id() < 0:
            err += "ID carte invalid!\n"
        if carte.get_titlu() == "":
            err += "Titlu carte invalid!\n"
        if carte.get_autor() == "":
            err += "Autor carte invalid!\n"
        if carte.get_an() < 0 or carte.get_an() > 2022:
            err += "An aparitie carte invalid!\n"
        if len(err) > 0:
            raise ValidError(err)
