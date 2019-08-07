class CarStore:
    def order(self, car_type):
        if car_type == '索纳塔':
            return Suonata()
        elif car_type == '明图':
            return Mingtu()


class Car:
    def move(self):
        print('车在移动')

    def music(self):
        print('车在放音乐')

    def stop(self):
        print('车在停止')


class Suonata(Car):
    def fly(self):
        print('车在飞')


class Mingtu(Car):
    pass


car_store = CarStore()
car = car_store.order('索纳塔')
car.move()
car.music()
car.stop()
car.fly()
