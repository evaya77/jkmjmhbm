import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100  
        self.alive = True

    def to_study(self):
        print('Час навчатися')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Сон')
        self.gladness += 3

    def to_chill(self):
        print('Студент грає в доту')
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10  

    def to_work(self):
        print('Студент працює')
        self.money += 50  
        self.gladness -= 4  
        self.progress -= 0.05  

    def is_alive(self):
        if self.progress < -0.5:
            print('Прогрес втрачено')
            self.alive = False
        elif self.gladness <= 0:
            print('Депресія')
            self.alive = False
        elif self.progress > 5:
            print('Прогрес надто швидкий')
            self.alive = False
        elif self.money < 0:
            print('Без грошей! Студент змушений піти на роботу.')
            self.to_work()

    def end_of_day(self):
        print(f'Щастя = {self.gladness}')
        print(f'Прогрес = {round(self.progress, 2)}')
        print(f'Гроші = {self.money}')

    def live(self, day):
        print(f'\n{" День " + str(day) + " життя " + self.name + " ":=^50}')
        if self.money < 20:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_work()

        self.end_of_day()
        self.is_alive()

nick = Student(name='Nick')

for day in range(365):
    if not nick.alive:
        break
    nick.live(day)