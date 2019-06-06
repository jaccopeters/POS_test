from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time


def basic_sale_off_line_card():
    general_functions.errorhandling("ABORT")

    l_general_test_settings = test_settings.general_test_settings()
    locale = l_general_test_settings[8]
    l_test_settings = test_settings.global_blue_transactions(locale)

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('basic sale paid with ' + y[2])

    wait(1)

    general_functions.fill_basket(y[0], y[1])

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_buttons.payment_page_other_menu_btns_click('ISSUE TAX FREE')

    type(Key.ENTER)

    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([y[2], 'REST']])