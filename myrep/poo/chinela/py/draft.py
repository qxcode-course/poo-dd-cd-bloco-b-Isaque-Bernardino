class Chinela():
    def __init__(self):
        self.__tamanho = 0
    def get_tamanho(self):
        return self.__tamanho
    def set_tamanho(self, valor: int) -> bool:
        if valor % 2 != 0:
            print("valor inválido")
            return False
        if valor < 20 or valor > 50:
            print("valor inválido")
            return False
        self.__tamanho = valor
        return True
def main():
    chinela = Chinela()
    while chinela.get_tamanho() == 0:
        valor = int(input("Digite seu tamanho de chinela: "))
        if chinela.set_tamanho(valor) == True:
            break
    print("Parabens, você comprou uma chinela tamanho", chinela.get_tamanho())
main();