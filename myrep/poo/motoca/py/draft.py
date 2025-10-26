class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return int(self.__age)
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
class Moto:
    def __init__(self, power: int, time: int, person: str):
        self.__power = 1
        self.__time = 0
        self.__person = None
    def getPower(self):
        return self.__power
    def getTime(self):
        return self.__time
    def getPerson(self):
        return self.__person
    def insert(self, person: Person) -> bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__person = person
            return True
    def remove(self) -> Person | None:
        if self.__person == None:
            print("fail: empty motorcycle")
            return None
        person = self.__person
        self.__person = None
        print(person)
    def buyTime(self, amount: int):
        self.__time += amount
    def drive(self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
        elif self.__person == None:
            print("fail: empty motorcycle")
        elif self.__person.getAge() > 10:
            print("fail: too old to drive")
        else:
            if time > self.__time:
                print(f"fail: time finished after {self.__time} minutes")
                self.__time = 0
            else:
                self.__time -= time
    def honk(self) -> str:
        return f"P" + "e" * self.__power + "m"
    def enter(self, name: str, age: int):
        self.__person = Person(name, age)
    def init(self, amount: int):
        self.__power = amount
    def __str__(self) -> str:
        st = f"power:{self.__power}, time:{self.__time}, "
        if self.__person == None:
            st += f"person:(empty)"
        else:
            st += f"person:({self.__person})"
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
            person = Person(args[1], args[2])
            motoca.insert(person)
        if args[0] == "init":
            amount = int(args[1])
            motoca.init(amount)
        if args[0] == "leave":
            motoca.remove()
        if args[0] == "buy":
            amount = int(args[1])
            motoca.buyTime(amount)
        if args[0] == "drive":
            amount = int(args[1])
            motoca.drive(amount)
        if args[0] == "honk":
            print(motoca.honk())
main()