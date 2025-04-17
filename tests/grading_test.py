from main import return0, returnNTimesA

def test_return0_extra():
    assert return0() == 0
    assert isinstance(return0(), int)

def test_returnNTimesA_edge_cases():
    assert returnNTimesA(0, 999) == 0
    assert returnNTimesA(1000, 0) == 0
    assert returnNTimesA(-3, -3) == 9
    assert returnNTimesA(999999, 1) == 999999
    assert returnNTimesA(2**10, 2**5) == 2**15
    assert returnNTimesA(3, 2) == 9
