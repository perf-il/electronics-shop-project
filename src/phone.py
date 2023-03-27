from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number: int) -> None:
        if new_number > 0 and type(new_number) is int:
            self.__number_of_sim = new_number
        else:
            # print('Количество физических SIM-карт должно быть целым числом больше нуля')
            raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


