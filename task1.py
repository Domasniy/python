from time import sleep

class TrafficLight:
    __color = ''

    def running(self):
        while True:
            self.__color = '\033[91mRed'
            print(self.__color)
            sleep(7)
            self.__color = '\u001b[33mYellow'
            print(self.__color)
            sleep(2)
            self.__color = '\u001b[33mGreen'
            print(self.__color)
            sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            sleep(2)
            if input('Повторить?(нажмите Enter для повторения, или введите любой символ, чтобы закончить)'):
                break

light = TrafficLight()
light.running()
