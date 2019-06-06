from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time
import string
import returns_with_receipt

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.loyalty_number(locale)


def add():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC add loyalty number')

    print(str(l_test_settings))

    for test_data in l_test_settings:
        general_functions.start_of_test_case('TC add loyalty number ' + test_data[5])

        general_functions.fill_basket(test_data[0], test_data[1])

        general_buttons.main_page_footer_menu_btns_click('CUSTOMER')

        # click ENTER LOYALTY NUMBER button
        general_buttons.main_page_customer_menu_btns_click('ENTER LOYALTY NUMBER')

        type(test_data[2])
        type(Key.ENTER)
        wait(1)
        type(Key.ENTER)
        wait(2)

        # click ENTER VOUCHER NUMBER button

        general_buttons.main_page_customer_menu_btns_click('ENTER VOUCHER NUMBER')
        type(test_data[3])
        type(Key.ENTER)
        wait(1)
        type(Key.ENTER)
        wait(2)

        general_functions.extended_wait('payment_page_key_pad_TOTAL', 30)

        general_buttons.main_page_key_pad_btns_click('TOTAL')
        general_functions.extended_wait('payment_page_key_pad', 30)
        general_functions.pay_transaction_with_multiple_tenders(test_data[4])

        # general end of test case
        general_functions.end_of_test_case( )


def remove():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC remove loyalty number')

    y = l_test_settings[0]
    general_functions.fill_basket(str(y[0]), y[1])

    general_buttons.main_page_footer_menu_btns_click('CUSTOMER')

    # click ENTER LOYALTY NUMBER button
    general_buttons.main_page_customer_menu_btns_click('ENTER LOYALTY NUMBER')

    type(y[2])
    type(Key.ENTER)
    wait(1)
    type(Key.ENTER)
    wait(2)

    # click ENTER VOUCHER NUMBER button

    general_buttons.main_page_customer_menu_btns_click('ENTER VOUCHER NUMBER')
    type(y[3])
    type(Key.ENTER)
    wait(1)
    type(Key.ENTER)
    wait(2)

    general_functions.extended_wait('payment_page_key_pad_TOTAL', 30)
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    type(Key.ENTER)
    wait(2)

    # remove loyalty
    general_buttons.main_page_footer_menu_btns_click('CUSTOMER')

    general_buttons.main_page_customer_menu_btns_click('REMOVE LOYALTY')
    type(Key.ENTER)

    general_functions.pay_transaction_with_multiple_tenders(y[4])

    general_functions.end_of_test_case( )


def search():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC search loyalty number')

    y = l_test_settings[0]
    general_functions.fill_basket(str(y[0]), y[1])
    # select loyalty client by loyalty number

    general_buttons.main_page_footer_menu_btns_click('CUSTOMER')
    general_buttons.main_page_customer_menu_btns_click('LOYALTY NUMBER SEARCH')

    type(y[4])
    type(Key.ENTER)
    type(Key.ENTER)
    type(Key.ENTER)

    general_functions.pay_transaction_with_multiple_tenders(y[4])

    general_functions.end_of_test_case( )


def suspend():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC suspend sale with loyalty number')

    y = l_test_settings[0]
    general_functions.fill_basket(str(y[0]), y[1])
    # select loyalty client by loyalty number

    general_buttons.main_page_footer_menu_btns_click('CUSTOMER')
    general_buttons.main_page_customer_menu_btns_click('LOYALTY NUMBER SEARCH')

    type(y[4])
    type(Key.ENTER)
    type(Key.ENTER)
    type(Key.ENTER)

    general_functions.extended_wait('payment_page_key_pad_TOTAL', 30)
    general_buttons.main_page_key_pad_btns_click('TOTAL')

    receipt_meta_data_array = general_functions.get_receipt_meta_data( )

    general_buttons.hamburger_click('HAMBURGER')
    general_buttons.hamburger_basket_menu_btns_click('SUSPEND')

    type(Key.ENTER)

    general_functions.end_of_test_case( )