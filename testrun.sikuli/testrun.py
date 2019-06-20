#general modules
from sikuli import *
from datetime import datetime
import general_functions
import time
import test_settings
import string

# test modules
import gui_screens
import drop_off
import pay_in
import pay_out
import no_sale
import custom
import item_not_found
import void_line_item
import basic_sale
import basic_sale_chf_eur
import cancel_receipt
import non_merchandise_sale
import manual_discount_li
import manual_discount_tr
import returns_with_receipt
import returns_without_receipt
import price_override
import local_employee_discount
import fms_promotions_and_markdowns
import check_GUI_elements
import gv_sale_and_redemption
import loyalty_number
import gift_receipt
import commission_sale
import remove_promotion
import pick_up
import tax_free

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global locale
locale = l_general_test_settings[8]
l_base_dir = l_general_test_settings[10]
global brand
brand = l_general_test_settings[6]

global l_test_settings
l_test_settings = test_settings.basic_sale_off_line_card_test_settings()

myScriptPath = l_base_dir + "on till regression test"
if not myScriptPath in sys.path:
    sys.path.append(myScriptPath)
    print("NOT PRESENT " + myScriptPath)

def tc_drop_off():
    drop_off.drop_off( )


def tc_pay_in():
    pay_in.pay_in( )


def tc_pay_out():
    pay_out.pay_out( )

def tc_no_sale():
    no_sale.no_sale( )

def make_receipts():
    pre_make_receipts.temp( )

def tc_custom():
    custom.custom()

def tc_item_not_found():
    item_not_found.item_not_found( )


def tc_basic_sale():
    basic_sale.basic_sale_off_line_card( )


def tc_basic_sale_chf_eur():
    basic_sale_chf_eur.basic_sale_chf_to_eur( )


def tc_void_line_item():
    void_line_item.void_line_item( )


def tc_cancel_receipt():
    cancel_receipt.cancel_receipt( )


def tc_non_merchandise_sale():
    non_merchandise_sale.non_merchandise_sale( )


def tc_manual_discount_li():
    manual_discount_li.manual_discount_li( )


def tc_manual_discount_tr():
    manual_discount_tr.manual_discount_tr( )


def tc_returns_with_receipt():
    returns_with_receipt.returns_with_receipt( )


def tc_returns_with_receipt_and_exchange():
    returns_with_receipt.returns_with_receipt_and_exchange()


def tc_returns_without_receipt():
    returns_without_receipt.returns_with_out_receipt_item_not_found( )


def tc_returns_without_receipt_with_loyalty_number():
    returns_without_receipt.with_loyalty_number( )


def tc_returns_with_out_receipt_item_not_found_and_exchange():
    returns_without_receipt.returns_with_out_receipt_item_not_found_and_exchange()


def tc_price_override():
    price_override.price_override( )


def tc_local_employee_discount():
    local_employee_discount.local_employee_discount_line_item(0)
    local_employee_discount.local_employee_discount_line_item(1)
    local_employee_discount.local_employee_discount_transaction(2)
    local_employee_discount.local_employee_discount_transaction(3)
    local_employee_discount.local_employee_discount_remove_employee(4)
    local_employee_discount.local_employee_discount_remove_line_item_discount(5)
    local_employee_discount.local_employee_discount_remove_transaction_discount(6)


def tc_fms_promotions_and_markdowns():
    fms_promotions_and_markdowns.promotions( )
    fms_promotions_and_markdowns.bonus_buys( )


def tc_check_GUI_elements():
    check_GUI_elements.screens( )

def tc_gv_sale_and_redemption():
    gv_sale_and_redemption.gv_sale()


def tc_loyalty_number():
    loyalty_number.add( )
    loyalty_number.remove( )
    #loyalty_number.search( )
    #loyalty_number.suspend( )


def tc_gift_receipt():
    gift_receipt.gift_receipt_from_line_items( )
    gift_receipt.gift_receipt_from_transaction( )


def tc_commission_sale():
    commission_sale.line_items( )
    commission_sale.transaction( )


def tc_remove_promotion():
    remove_promotion.remove( )

def tc_pick_up():
    pick_up.pick_up( )


def tc_tax_free():
    #is ok again#tax_free.issue_tax_form_basic_sale_any_tender( )
    tax_free.issue_tax_form_after_sale_any_tender( )


general_functions.start_of_test_run( )

#tc_drop_off()
#tc_pay_out()
#tc_pay_in()
#tc_no_sale()
#tc_basic_sale()
#tc_item_not_found()
#tc_void_line_item()
#tc_cancel_receipt()
#tc_non_merchandise_sale()
#tc_manual_discount_li()
#tc_manual_discount_tr()
# tc_returns_with_receipt()
# tc_returns_with_receipt_and_exchange()
# tc_returns_without_receipt()
# tc_returns_with_out_receipt_item_not_found_and_exchange()
# tc_price_override()
tc_local_employee_discount()
# tc_fms_promotions_and_markdowns()
# if brand == "TH":
   # tc_loyalty_number()
#tc_gift_receipt()
#tc_commission_sale()
#tc_remove_promotion()
#tc_pick_up()
#tc_gv_sale_and_redemption()
# tc_tax_free()



general_functions.end_of_test_run()

