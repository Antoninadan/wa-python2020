import links


def get_link_dialog():
    name = input('Enter link name: ')
    try:
        url = links.get_link(name)
    except KeyError:
        print('link does not exist')
    else:
        print(url)


def add_link_dialog():
    name = input('Enter link name: ')
    url = input('Enter URL: ')
    try:
        links.add_link(name, url)
    except KeyError:
        print('link already exists')


def main():
    while True:
        print('''
        Menu:
        1) Get link
        2) Add link
        3) Exit
        ''')
        choice = input('> ')

        print()

        if choice == '1':
            get_link_dialog()
        elif choice == '2':
            add_link_dialog()
        elif choice == '3':
            return
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()
