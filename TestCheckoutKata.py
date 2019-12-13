
from Checkout import Checkout

def check_out():
    check_out = Checkout()
    return check_out

def test_CanCalculateTotal(check_out):
    check_out.addItemPrice("chips", 1)
    check_out.addItem("chips")
    assert check_out.calculateTotal() == 1