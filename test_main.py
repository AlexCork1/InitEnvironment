# test_main.py

from main import return0, returnNTimesA

def test_return0():
    assert return0() == 0

def test_returnNTimesA():
    assert returnNTimesA(1, 5) == 5
    assert returnNTimesA(-1, 5) == -5
    assert returnNTimesA(4, 4) == 16
    assert returnNTimesA(3, 2) == 6
