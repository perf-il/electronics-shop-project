import csv


class InstantiateCSVError(Exception):
    """Класс-исключение для обработки ошибок при открытии CSV-файла"""

    def __init__(self, massage='Файл item.csv поврежден'):
        self.massage = massage

    def __str__(self):
        return self.massage


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(str_num: str):
        try:
            return int(float(str_num))
        except TypeError:
            return 'Введено некорректное значение'

    @classmethod
    def instantiate_from_csv(cls, path='../src/items_er.csv'):
        cls.all.clear()
        # пробуем открыть файл items.csv
        try:
            with open(path, encoding="CP1251", newline='') as f:
                csv_file = csv.DictReader(f)
                # если файл открыт, но не содержит полей, необходимых для инициализации класса Item,
                # вызываем исключение из класса InstantiateCSVError
                if csv_file.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError()
                # если необходимые поля присутствуют, инициализируем класс Item
                for row in csv_file:
                    cls(row['name'], row['price'], row['quantity'])
        # если файл не удалось открыть, вызываем исключение FileNotFoundError
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            print('Длина наименования товара превышает 10 символов.')
            # raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception('Сложение невозможно')
