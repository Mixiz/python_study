# Класс Светофор. Включаемся и моргаем цветами
import time


class TrafficLight:
    COLORS = ('красный', 'желтый', 'зеленый')
    __PERIODS = (7, 2, 10)
    __TOTALTIME = __PERIODS[0] + __PERIODS[1] + __PERIODS[2]
    __color = COLORS[0]
    __time = time.time()

    def running(self):
        local_time = (time.time() - self.__time) % self.__TOTALTIME
        if local_time < self.__PERIODS[0]:
            self.__color = self.COLORS[0]
        elif local_time < self.__PERIODS[0] + self.__PERIODS[1]:
            self.__color = self.COLORS[1]
        else:
            self.__color = self.COLORS[2]
        print(f'Горит {self.__color}')


if __name__ == '__main__':
    light = TrafficLight()
    light.running()

    while True:
        check = input("Узнать светофор. q - выйти\n")
        if check == 'q':
            break;
        else:
            light.running()
