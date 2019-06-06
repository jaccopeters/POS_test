from sikuli import *
import general_functions
import general_buttons
import test_settings
import time
import test_cases
from datetime import datetime


def custom():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('item not found all divisions')

    l_general_test_settings = test_settings.general_test_settings( )
    locale = l_general_test_settings[8]
    brand = l_general_test_settings[6]
    transactions = test_settings.custom(locale)

    # test_cases.item_not_found_tc_0010("does the main screen look OK?")

    time.sleep(5)

    for transaction in transactions:
        general_buttons.main_page_items_gv_menu_btns_click('ITEM NOT FOUND')

        division = transaction[0]

        print('division: ' + division)

        general_buttons.main_page_items_gv_menu_item_not_found_btns_click(division)
        
        type(transaction[1])

        type(Key.ENTER)

        type(transaction[2])

        type(Key.ENTER)

        # click the TOTAL button
        general_buttons.main_page_key_pad_btns_click('TOTAL')

        general_functions.extended_wait('four_eyes_form', 60)

        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

        general_functions.extended_wait('payment_page_key_pad', 60)

        general_functions.pay_transaction_with_multiple_tenders(transaction[3])

        general_functions.extended_wait('main_page_key_pad', 60)

    # general end of test case
    general_functions.end_of_test_case( )