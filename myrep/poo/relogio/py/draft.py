class Watch:
    def __init__(self, hour: int, minute: int, second: int):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
    def getHour(self):
        return self.__hour
    def getMinute(self):
        return self.__minute
    def getSecond(self):
        return self.__second
    def setHour(self, hour: int):
        if hour < 0 or hour > 23:
            print("fail: hora invalida")
            return
        else:
            self.__hour = hour
    def setMinute(self, minute: int):
        if minute < 0 or minute > 59:
            print("fail: minuto invalido")
            return
        else:
            self.__minute = minute
    def setSecond(self, second: int):
        if second < 0 or second > 59:
            print("fail: segundo invalido")
            return
        else:
            self.__second = second
    def nextSecond(self):
        if self.__hour != 23:
            self.__hour += 1
        else:
            self.__hour = 0
        if self.__minute != 59:
            self.__minute += 1
        else:
            self.__minute = 0
        if self.__second != 59:
            self.__second += 1
        else:
            self.__second = 0
    def __str__(self) -> str:
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
def main():
    relogio = Watch(0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(relogio)
        if args[0] == "set":
            hour = int(args[1])
            minute = int(args[2])
            second = int(args[3])
            relogio.setHour(hour)
            relogio.setMinute(minute)
            relogio.setSecond(second)
        if args[0] == "init":
            hour = int(args[1])
            minute = int(args[2])
            second = int(args[3])
            relogio.setHour(hour)
            relogio.setMinute(minute)
            relogio.setSecond(second)
        if args[0] == "next":
            relogio.nextSecond()
main()