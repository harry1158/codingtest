import pytest
from main import perPerson_calculator

def test_perPerson_calculator_normal():
    result = perPerson_calculator(3, 1000)
    print(result)
    assert result == [333, 333, 334]

def test_perPerson_calculator_error():
    with pytest.raises(ValueError) as exc_info:
        perPerson_calculator(0, 100)
    assert "must be at least 1" in str(exc_info.value)