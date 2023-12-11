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
    # def health(self):
    #     return self.health_point * 2

    def __str__(self):
        return f'Прозвище: {self.nickname} \nСупер сила: {self.superpower}\nОчки здоровья: {self.health_point} \nКоронная фраза: {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Монки Д Луффи', 'Соломенная шляпа', 'Резиновый человек', '1000', 'Я стану королём пиратов!!!')
hero.print_name()
print(hero)
print(len(hero))
