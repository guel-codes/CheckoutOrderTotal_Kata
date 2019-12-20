
from Checkout import Checkout

def check_out():
    check_out = Checkout()
    check_out.addItemPrice("chips", 1)
    check_out.addItemPrice("candy", 2)
    return check_out

def test_CanCalculateTotal(check_out):
    check_out.addItem("chips")
    assert check_out.calculateTotal() == 1

def test_TotalWithMultipleItems(check_out):
    check_out.addItem("chips")
    check_out.addItem("candy")
    assert check_out.calculateTotal == 3

def test_CanAddDiscountRule(check_out):
    check_out.addDiscount("chips", 3, 2)

def testCanApplyDiscountRuleToTotal(check_out):
    check_out.addDiscount("chips", 3, 2)
    check_out.addItem("chips")
    check_out.addItem("chips")
    check_out.addItem("chips")
    assert check_out.calculateTotal == 2


