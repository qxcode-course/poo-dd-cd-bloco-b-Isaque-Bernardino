class Person:
    def __init__(self, name: str, money: int):
        self.__name = name
        self.__money = money
    def getName(self):
        return self.__name
    def getMoney(self):
        return int(self.__money)
    def setMoney(self, value: int):
        self.__money = value
    def __str__(self) -> str:
        return f"{self.__name}:{self.__money}"
class Moto:
    def __init__(self, cost: int, driver: Person, passenger: Person):
        self.__cost = 0
        self.__driver = None
        self.__passenger = None
    def getCost(self):
        return self.__cost
    def getDriver(self):
        return self.__driver
    def getPassenger(self):
        return self.__passenger
    def setDriver(self, driver: Person):
            self.__driver = driver
    def setPass(self, passenger: Person):
        self.__passenger = passenger
    def drive(self, km: int):
        self.__cost += km
    def leavePass(self):
        if self.__passenger != None:
            moneyPass = self.__passenger.getMoney() - self.__cost
            self.__passenger.setMoney(moneyPass)
        if self.__driver != None:
            moneyDriver = self.__driver.getMoney() + self.__cost
            self.__driver.setMoney(moneyDriver)
        if self.__passenger.getMoney() < self.__cost:
            print("fail: Passenger does not have enough money")
            self.__passenger.setMoney(0)
        print(f"{self.__passenger} left")
        self.__passenger = None
        self.__cost = 0
    def __str__(self) -> str:
        return f"Cost: {self.__cost}, Driver: {self.__driver}, Passenger: {self.__passenger}"
def main():
    motoca = Moto (0, "", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(motoca)
        if args[0] == "setDriver":
            driver = Person(args[1], args[2])
            motoca.setDriver(driver)
        if args[0] == "setPass":
            passenger = Person(args[1], args[2])
            motoca.setPass(passenger)
        if args[0] == "leavePass":
            motoca.leavePass()
        if args[0] == "drive":
            km = int(args[1])
            motoca.drive(km)
main()