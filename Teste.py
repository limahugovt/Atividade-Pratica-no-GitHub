class Teste():
    def __init__(self):
        self.nome = "Victor"
        self.idade = 14
        self.__cpf = 101001010101
        self._conta = 1111


class Modif(Teste):
    teste = Teste()
    def setName(self):
        self.nome = input('digite nome: ')
        
    def getName(self):
        return print(self.nome)
    
    def getCPF(self):
        return print(self._Teste__cpf)