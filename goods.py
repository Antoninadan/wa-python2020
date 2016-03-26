
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