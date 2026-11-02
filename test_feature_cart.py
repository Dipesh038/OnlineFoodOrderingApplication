import pytest; from feature_cart import total
@pytest.mark.parametrize("price,discount,answer", [(100, 10, 90), (0, 0, 0), (20, 100, 0), (-1, 0, ValueError), (5, 101, ValueError)])
def test_total(price, discount, answer): assert pytest.raises(ValueError, total, price, discount) if answer is ValueError else total(price, discount) == answer
