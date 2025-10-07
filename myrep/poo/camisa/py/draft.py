class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    def get_tamanho(self):
        return self.__tamanho
    def set_tamanho(self, etiqueta: str):
        if etiqueta != "PP" and etiqueta != "P" and etiqueta != "M" and etiqueta != "G" and etiqueta != "GG" and etiqueta != "XG":
            print("tamanho inválido! Os tamanhos permitidos são: PP, P, M e G, GG e XG.")
            return False
        self.__tamanho = etiqueta
        return True
def main():
    camisa = Camisa()
    while True:
        etiqueta = str(input("informe o tamanho da roupa: "))
        if camisa.set_tamanho(etiqueta) == True:
            break
    print("Parabens, você comprou uma roupa tamanho", camisa.get_tamanho())
main();
