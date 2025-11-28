from merchandise import (
    Merchandise,
)


def check_new_count(cheker, merchandise):
    while cheker is False:
        try:
            new_count = int(input("Введите новое количество товара: "))

            merchandise.set_count(new_count)
            cheker = True

        except ValueError:
            print("Ввод в формате числа!")


class Menu:
    """Класс меню для работы с классом Merchandise."""

    def print_info_menu(self) -> None:
        """Метод для вывода пунктов меню."""

        print(
            '1 - Просмотр полной информации о товаре.\n'
            '2 - Изменить название товара.\n'
            '3 - Изменить шифр товара.\n'
            '4 - Изменить количество товара.\n'
            '5 - Получение информации о названии товара.\n'
            '6 - Получение информации о шифре товара.\n'
            '7 - Получение информации о количестве товара.\n'
            '8 - Донат разрабу на покушать.\n'
            '10 - Возврат к меню выбора товара\n'
            '0 - ЗАВЕРШЕНИЕ РАБОТЫ ПРОГРАММЫ.\n'
        )

    def choise_menu(self, choise: int, merchandise: Merchandise) -> bool:
        """Пользовательское меню.

        Args:
            choise: Выбор действия пользователем.

        Returns:
            programm_ranning: Проверка работы программы.
        """

        cheker = False
        programm_ranning = True

        match choise:
            case 1:
                merchandise.print_info()
            case 2:
                new_name = input("Введите новое название товара: ")

                merchandise.set_name(new_name)
            case 3:
                new_cipher = input("Введите новый шифр товара: ")

                merchandise.set_cipher(new_cipher)
            case 4:
                check_new_count(cheker, merchandise)
            case 5:
                print(f'Название товара: {merchandise.get_name()}\n')
            case 6:
                print(f'Шифр товара: {merchandise.get_cipher()}\n')
            case 7:
                print(f'Количество товара: {merchandise.get_count()}\n')
            case 8:
                print(
                    '+7(927)475-25-68\n'
                    'Буду рад любой сумме на любой банк!\n'
                )
            case 0:
                programm_ranning = False

        return programm_ranning