class Camisa:
    def __init__(self):
        self.__tamanho = ""
    def getTamanho(self):
        return self.__tamanho
    def setTamanho(self, letter: str):
        if letter != "PP" and letter != "P" and letter != "M" and letter != "G" and letter != "GG" and letter != "XG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else:
             self.__tamanho = letter
    def __str__(self) -> str:
        return f"size: ({self.__tamanho})"
def main():
    camisa = Camisa()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(camisa)
        elif args[0] == "size":
            letter = str(args[1])
            camisa.setTamanho(letter)

main()
        