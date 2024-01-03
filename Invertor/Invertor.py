class Invertor :

    def __init__(self,palavra:str ) -> None:
        self.__palavra  = palavra 
    
    @property
    def palavra(self):
        return self.__palavra
    
    @palavra.setter
    def palavra(self, palavra: str):
        self.__palavra = palavra 
    
    def invertor (self, palavra :str ):
        palavra = str(input('Digite uma frase: '))
        string = palavra[::-1]
        print('A frase que você digitou invertida fica: {}'.format(string))
        