
from Checkout import Checkout

def test_CanAddItemPrice():
    check_out = Checkout()
    check_out.addItemPrice("chips", 1)