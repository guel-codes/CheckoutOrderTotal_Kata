
from Checkout import Checkout

def check_out():
    check_out = Checkout()
    return check_out

def test_CanAddItemPrice(check_out):
    check_out.addItemPrice("chips", 1)

def test_canAddItemPrice(check_out):
    check_out.addItem("chips")