class Merchandise:
    """Класс хранения информации о товарах. """

    def __init__(self, name: str="Товар", cipher: str=None, count = 0) -> None:
        """Конструктор класса Merchandise.

        Args:
            name: Название товара.
            cipher: Шифр товара.
            count: Количество товара.
        """

        self.__name = name
        self.__cipher = cipher
        self.__count = count

    def set_name(self, name: str) -> None:
        """Сеттер названия товара.

        Args:
            name: Название товара.
        """

        self.__name = name

    def set_cipher(self, cipher: str) -> None:
        """Сеттер шифра товара.

                 Args:
                     cipher: Шифр товара.
                 """

        self.__cipher = cipher

    def set_count(self, count: int) -> None:
        """Сеттер количества товара.

        Args:
            count: Количество товаров.
        """

        while count <= 0:
            count = int(input("Введите количество товара больше 0: "))

        self.__count = count

    def get_name(self) -> str:
        """Геттер названия товара.

        Returns:
            name: Название товара.
        """

        return self.__name

    def get_cipher(self) -> str:
        """Геттер шифра товара.

        Returns:
            cipher: Шифр товара.
        """

        return self.__cipher

    def get_count(self) -> int:
        """Геттер количества товара.

        Returns:
            count: Количество товара.
        """

        return self.__count

    def print_info(self) -> None:
        """Вывод полной информации о товаре."""

        print(
            f'\nНазвание товара: {self.get_name()}\n'
            f'Шифр данного товара: {self.get_cipher()}\n'
            f'Количество данного товара: {self.get_count()}\n\n'
        )
