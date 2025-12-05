from src.main import elevar, to_upper

def test_elevar():
    assert elevar(5,5) == 3125
    
def test_to_upper():
    assert to_upper("rafael") == "RAFAEL"
    
def test_to_upper():
    assert to_upper("rafael") == "rafael"