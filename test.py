from main import get_name

def test_uppercase_name():
    assert get_name("john") == "JOHN"

def test_data_retrieval():
    result = get_name("alice")
    assert result == "ALICE"

def test_invalid_name():
    result = get_name("")
    assert result is None