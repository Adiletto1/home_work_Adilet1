class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(f'Имя героя: {self.name}')

    # не получилось вызвать этот метод, выдовало ошибку
    def health(self):
        return self.health_point * 2

    def __str__(self):
        return f'Прозвище: {self.nickname} \nСупер сила: {self.superpower}\nОчки здоровья: {self.health_point} \nКоронная фраза: {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Монки Д Луффи', 'Соломенная шляпа', 'Резиновый человек', 1000, 'Я стану королём пиратов!!!')
hero.print_name()
print(hero)
print(len(hero))

class Air(SuperHero):
    damage = 100
    fly = False

    def health(self):
        self.fly = True
        return self.health_point ** 2, self.fly

    def printTrue(self):
        print('True in the True_phrase')







class Earth(SuperHero):
    damage = 100
    fly = False

    def health(self):
        self.fly = True
        return self.health_point ** 2, self.fly

    def printTrue(self):
        print('True in the True_phrase')

hero2 = Air('Марко', 'Феникс Марко', 'Дьявольский фрукт', 800, 'больно')
hero2.health()
hero2.print_name()
hero2.printTrue()
hero3 = Earth('Папич', 'Arthas','Батинки - красовки', 20000, 'Я БУДУ ЖИТЬ ВЕЧНО!!!')
hero3.health()
hero3.print_name()
hero3.printTrue()
print(hero3)

class Villian(Air):
    people = 'monster'

    def gen_x(self): ...

    def crit(self):
        return print(self.damage ** 2)

vil1 = Villian('Торфин', 'Сын Торса', 'У него нет врагов', 100, 'У меня нет врагов')
vil1.crit()

# создать класс villain наследованный от нового класса
# изменить  значение  атрибутa people на monster
#
# создать метод gen_x который ПОКА ничего не делает
#
# создать метод crit который возводит в степень урон
#
# создать объекты для этого класса
#
# применить метод crit на объект другого класса  у которого есть аргумент damage
# не смог применить метод crit на другой объект класса, это вообще возможно?