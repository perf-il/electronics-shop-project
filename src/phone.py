from item import Item


class Phone(Item):
    """
    Класс для представления телефонов.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


phone1 = Phone("iPhone 14", 120_000, 5, 2)

