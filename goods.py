# каталог товаров с возможностью добавления отзывов
# наполнение каталога - название, стоимость в грн, категория
categories = {
    '1': 'научно-популярная литература',
    '2': 'беллетристика',
    '3': 'медицина',
}

def input_category(prompt):
    input_value = input(prompt).strip()
    if input_value in categories:
        return input_value
    else:
        print('Неверная категория!')
        return input_category(prompt)

def input_money(prompt):
    input_value = input(prompt).strip()
    try:
        return float(input_value)
    except ValueError:
        print('Неверный формат цены!')
        return input_money(prompt)

def input_uniq(prompt, list):
    input_value = input(prompt).strip()
    if input_value not in list:
        return input_value
    else:
        print('Неуникальный артикул!')
        return input_uniq(prompt, list)

class Goods():

    list_id = []
    list_goods = []

    def __init__(self, id, name, cost, category):
        self.id = id
        self.name = name
        self.cost = cost
        self.category = category
        Goods.list_id.append(self.id)
        Goods.list_goods.append(self)

    @classmethod
    def new_good(cls):
        good_id = input_uniq('Введите уникальный артикул: ', Goods.list_id)
        good_name = input('Введите название: ')
        good_cost = input_money('Введите стоимость в грн: ')
        good_category = input_category('Введите категорию (1 для науч-поп., 2 для беллетристики, 3 для медицины): ')
        return cls(good_id, good_name, good_cost, good_category)

    def __repr__(self):
        return 'Артикул: {}, название: "{}", жанр: {} (цена: {} грн)'.format(self.id, self.name, categories[self.category], self.cost)

    @staticmethod
    def find_good():
        input_value = input('Введите артикул товара: ').strip()
        if input_value in Goods.list_id:
            return input_value
        else:
            print('Не существует такого артикула!')
            return Goods.find_good()

    @staticmethod
    def add_comment_id(good_id_):
        for good in Goods.list_goods:
            if good.id == good_id_:
                good.self_add_comment()

    def self_add_comment(self):
        comment_name = input('Введите ваш отзыв: ').strip()
        return Comment(comment_name, self.id)

    def self_add_comment_with_name(self, comment_name_):
        return Comment(comment_name_, self.id)

class Comment():
    list_comments = []

    def __init__(self, name_, good_id_):
        self.name = name_
        self.good_id = good_id_
        Comment.list_comments.append(self)

    @staticmethod
    def print_4_good(good_id_):
        print('Комментарии: ')
        count = 0
        for comment in Comment.list_comments:
            if comment.good_id == good_id_:
                count += 1
                print(count, ': ', comment.name)
            else:
                print('- отсутствуют')
                break

good1 = Goods('1', 'good1', '100', '1')
good2 = Goods('2', 'good2', '200', '2')
good4 = Goods('3', 'good3', '300', '3')
good1.self_add_comment_with_name('Жуткая книга')
good1.self_add_comment_with_name('Ничего так книга')

def main():

    while True:
        print('''
        Меню:
        1) Добавить новый товар
        2) Добавить комментарий к существующему товару
        3) Распечатать все комментарии к существующему товару
        4) Выход
        ''')
        choice = input('> ')

        print()

        if choice == '1':
            Goods.new_good()
            print()
            print('Вы создали новый товар:', '\n', Goods.list_goods[len(Goods.list_goods) - 1])

        elif choice == '2':
            Goods.add_comment_id(Goods.find_good())

        elif choice == '3':
            print()
            Comment.print_4_good(Goods.find_good())
        elif choice == '4':
            break
        else:
            print('Вы внесли неверный код!')

        print()


if __name__ == '__main__':
    main()