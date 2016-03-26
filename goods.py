# каталог товаров с возможностью добавления отзывов
# наполнение каталога - название, стоимость в грн, категория
categories = {
    '1': 'science',
    '2': 'novel',
    '3': 'medicine',
}

def input_category(prompt):
    input_value = input(prompt)
    if input_value in categories:
        return input_value
    else:
        print('Неверная категория!')
        return input_category(prompt)

def input_money(prompt):
    input_value = input(prompt)
    try:
        return float(input_value)
    except ValueError:
        print('Неверный формат цены!')
        return input_money(prompt)

def input_uniq(prompt, list):
    input_value = input(prompt)
    if input_value not in list:
        return input_value
    else:
        print('Неуникальный артикул!')
        return input_uniq(prompt, list)

class Goods():

    list_names = []

    def __init__(self, id, name, cost, category):
        self.id = id
        self.name = name
        self.cost = cost
        self.category = category
        Goods.list_names.append(self.id)

    @classmethod
    def new_good(cls):
        good_id = input_uniq('Введите уникальный артикул: ', Goods.list_names)
        good_name = input('Введите название: ')
        good_cost = input_money('Введите стоимость в грн: ')
        good_category = input_category('Введите категорию (1 для science, 2 для novel, 3 для medicine): ')
        return cls(good_id, good_name, good_cost, good_category)

    def __repr__(self):
        return 'Артикул: {}, название: "{}", {} (цена: {} грн)'.format(self.id, self.name, categories[self.category], self.cost)

    @staticmethod
    def find_good():
        input_value = input('Введите артикул товара: ')
        if input_value in Goods.list_names:
            return input_value
        else:
            print('Не существует такого артикула!')
            return find_good()

    def get_good(self, good_id_):
        if self.id == good_id_:
            return self

    def add_comment(self):
        comment_name = input('Введите ваш отзыв: ')
        return Comment(comment_name, self.id)

    # def print_comments(self):
    #     Comment.good == self:
    #         print('Комментарий: ', Comment.name)

class Comment():
    list_comments = []

    def __init__(self, name_, good_id_):
        self.name = name_
        self.good_id = good_id_
        Comment.list_comments.append(self)

    @staticmethod
    def print_4_good(good_id_):
        for comment in Comment.list_comments:
            if comment.good_id == good_id_:
                print('Комментарий: ', comment.name)
            else:
                print('Нет комментариев')


# good1 = Goods.new_good()
# print(good1)
good1 = Goods('11', 'good1', '100', '1')
good2 = Goods('22', 'good2', '200', '2')
good4 = Goods('332', 'good3', '200', '2')
# good3 = Goods.new_good()
# print(good3)

print(Goods.find_good())
# print(Goods.get_good(Goods.find_good()))

# good1.add_comment()
# good1.add_comment()
# Comment.print_4_good(good1.id)
 # 3
# good2.print_comments()


# print_comments(good2, comment1)  #3



def main():

    while True:
        print('''
        Меню:
        1) Добавить новый товар
        2) Добавить комментарий к товару
        3) Выход
        ''')
        choice = input('> ')

        print()

        if choice == '1':
            Goods.new_good()
        elif choice == '2':
            good_id = find_good()
            get_good(good_id).add_comment()

            if
                add_comment(self)

        elif choice == '3':
            break
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()