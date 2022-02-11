from safe import *

def test_sit():
    assert sit("123","145") == (1,0)
    assert sit("123","142") == (1,1)
    assert sit("123","231") == (0,3)
    assert sit("123","123") == (3,0)

