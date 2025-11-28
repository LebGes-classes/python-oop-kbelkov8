from merchandise import (
    Merchandise,
)
from menu import (
    Menu,
)


class Main:
    """Класс для объединения работы Menu и Merchandise."""

    menu = Menu()
    merchandise = Merchandise()
    product_1 = Merchandise("milk", "123milk", 10)
    product_2 = Merchandise()
    list_product = [product_1, product_2]

    programm_ranning = True


    while programm_ranning is True:
        choise_product = int(input("Выберите товар(1 или 2): "))

        menu.print_info_menu()

        choise = int(input("Выбор действия с товаром: "))

        if choise == 10:
            continue

        programm_ranning = menu.choise_menu(choise, list_product[choise_product - 1])


print(Main())
