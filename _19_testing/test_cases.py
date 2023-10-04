from _2_pytest import add 

def test_case1():
    assert add(3,1) == 4

def test_case2():
    assert add("a","b") == "abc"

class Test_Cases:
    def test_case1(self):
        assert add(3,1) == 4

    def test_case2(self):
        assert add("a","b") == "abc"