import pytest
from src.keyboard import KeyBoard


@pytest.fixture()
def kb_1():
    return KeyBoard("Keyboard1", 1000, 40)


@pytest.fixture()
def kb_2():
    return KeyBoard("Keyboard2", 1200, 10)


def test_keyboard(kb_1, kb_2):
    assert str(kb_1) == 'Keyboard1'
    assert str(kb_2) == 'Keyboard2'
    assert repr(kb_1) == "KeyBoard('Keyboard1', 1000, 40)"
    assert repr(kb_2) == "KeyBoard('Keyboard2', 1200, 10)"


def test_change_lang(kb_1):
    assert str(kb_1.language) == 'EN'
    kb_1.change_lang()
    assert str(kb_1.language) == 'RU'
    kb_1.change_lang().change_lang()
    assert str(kb_1.language) == 'RU'


def test_keyboard_lang(kb_1):
    kb_1.language = 'RU'
    assert str(kb_1.language) == 'RU'
    kb_1.language = 'EN'
    assert str(kb_1.language) == 'EN'
    with pytest.raises(AttributeError):
        kb_1.language = 'GR'
        kb_1.language = 1
        kb_1.language = 0.1

