class Home:
    b = None

    def new(a):
        try:
            int(a)
            print('Всё чётко)))')
        except ValueError:
            print('Ну это: ValueError!')

b = Home
b.new('qwert')