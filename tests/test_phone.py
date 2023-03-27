import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item_1():
    return Item("Test1", 10000, 20)


@pytest.fixture()
def item_2():
    return Item("Test2", 20000, 30)


@pytest.fixture()
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture()
def phone_2():
    return Phone("iPhone 12", 100_000, 7, 1)


def test_phone(phone_1, phone_2):
    assert str(phone_1) == 'iPhone 14'
    assert str(phone_2) == 'iPhone 12'
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone_2) == "Phone('iPhone 12', 100000, 7, 1)"


def test_sim(phone_1, phone_2):
    assert phone_1.number_of_sim == 2
    assert phone_2.number_of_sim == 1
    with pytest.raises(Exception):
        phone_1.number_of_sim = 0
        phone_1.number_of_sim = 3.2


def test_add(item_1, phone_1):
    assert (item_1 + phone_1) == 25
    assert (item_1 + item_1) == 40
    assert (phone_1 + phone_1) == 10
    with pytest.raises(Exception):
        phone_1 + 1
        item_1 + 2
