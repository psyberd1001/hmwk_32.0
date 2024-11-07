import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        days = 0
        warriors = 100
        print(f'{self.name}, на нас напали!')
        while warriors > 0:
            time.sleep(1)
            days += 1
            warriors -= self.power
            if warriors > 0:
                print(f'{self.name} сражается {days}, осталось {warriors} воинов.\n')
            else:
                print(f'{self.name} сражается {days}, осталось 0 воинов. \n')

        print(f'{self.name} одержал победу спустя {days} дней(дня)\n')


thread1 = Knight('Abbadon', 10)
thread2 = Knight('Lucifer', 8)
thread1.start()
thread2.start()
thread2.join()
print('Все битвы закончились!')
