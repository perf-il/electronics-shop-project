from src.item import Item


class MixinLang:
    """Миксин-Класс для хранения и изменения раскладки клавиатуры"""
    languages = ('EN', 'RU')

    def __init__(self):
        self.__language = self.languages[0]

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language: str):
        if new_language in self.languages:
            self.__language = new_language
        else:
            raise AttributeError

    def change_lang(self):
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


class KeyBoard(Item, MixinLang):
    """Класс для представления товара - клавиатуры"""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)




