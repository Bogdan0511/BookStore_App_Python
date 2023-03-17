from Business.Service import ServiceBibl
from Prezentare.UI import Consola
from Infrastructura.Repository import FileRepo
from Validare.Validation import Validator
from Testare.Testing import Teste

if __name__=='__main__':
    valid = Validator()
    repo = FileRepo()
    service = ServiceBibl(valid, repo)
    ui = Consola(service)
    teste = Teste()

    teste.run_all_tests()
    ui.carti_fisier()
    ui.run()