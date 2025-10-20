class Person:
    def __init__(self, name: str, age: int):
        self.__name: str
        self.__age: int
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
class Moto:
    def __init__(self, power: int, time: int, person: str):
        self.power = 1
        self.time = 0
        self.person = None
    def insert(self, person: str) -> bool:
        if self.person != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.person = person
            return True
    def remove(self, person: str) -> Person | None:
        if self.person == None:
            print("fail: empty motorcycle")
            return None
        else:
            self.person - person
            return True
    def enter(self, name: str, age: int):
        self.person = Person(name, age)
    def __str__(self) -> str:
        st = f"power:{self.power}, time:{self.time}, "
        if self.person == None:
            st += f"person:(empty)"
        else:
            st += f"person:{self.person}"
        return st
def main():
    motoca = Moto (1, 0, "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(motoca)
        if args[0] == "enter":
            motoca.enter(args[1], args[2])
             
main()