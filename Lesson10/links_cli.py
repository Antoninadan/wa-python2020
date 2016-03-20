import links


def get_link_dialog():
    name = input('Enter link name: ')
    try:
        url = links.get_link(name)
    except KeyError:
        print('link does not exist')
    else:
        print(url)


def remove_link_dialog():
    name = input('Enter link name: ')
    try:
        links.remove_link(name)
    except KeyError:
        print('link does not exist')


def add_link_dialog():
    name = input('Enter link name: ')
    url = input('Enter URL: ')
    try:
        links.add_link(name, url)
    except KeyError:
        print('link already exists')


def main():
    links.initialize()

    while True:
        print('''
        Menu:
        1) Get link
        2) Add link
        3) Delete link
        4) Exit
        ''')
        choice = input('> ')

        print()

        if choice == '1':
            get_link_dialog()
        elif choice == '2':
            add_link_dialog()
        elif choice == '3':
            remove_link_dialog()
        elif choice == '4':
            break
        else:
            print('Incorrect input')

        print()

    links.finalize()


if __name__ == '__main__':
    main()
