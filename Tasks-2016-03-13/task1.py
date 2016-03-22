class Book:
    """Класс, представляющий книгу
    """

    def __init__(self, title, year, genre):
        """Конструктор
        Задание: сохраните title, year и genre в виде
        атрибутов объекта self
        """
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        """Возвращает внутреннее строковое представление объекта
        для консоли, отладчика и т.д.
        Задание: верните строку в формате
                 Book("название", год, "жанр")
        """
        return 'Book("{!r}", {!r}, "{!r}")'.format(self.title, self.year, self.genre)

    def __str__(self):
        """Возвращает строку, предназначенную для пользователя
        (str, print и т.д.)
        Задание: верните строку в произвольном формате
        """
        return '{!r} - {!r} ({!r})'.format(self.title, self.year, self.genre)

# Задание: создайте несколько объектов класса Book
# и выведите их на экран

book1 = Book('War and peace', 2011, 'lirics')
print(book1)