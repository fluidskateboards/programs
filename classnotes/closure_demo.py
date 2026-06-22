def sequence(start, delta):
    value = start
    def advance():
        nonlocal value 
        current = value
        value += delta
        return current
    return advance

s = sequence(start=10, delta=3)
def test_sequence():
    assert(s() == 10)
    assert(s() == 13)
    assert(s() == 16)
