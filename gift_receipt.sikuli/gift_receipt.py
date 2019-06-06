from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time
import gui_screens


global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global brand
brand = l_general_test_settings[6]
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global is_gui_test
is_gui_test = l_general_test_settings[11]
global country
country = l_general_test_settings[13]
global l_test_settings
l_test_settings = test_settings.gift_receipt()


def gift_receipt_from_line_items():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('print gift receipt from line item')

    # make test receipt and get it to print it as a gift receipt
    get_receipt_for_gift_receipt(general_functions.make_test_receipts(l_test_settings[0], l_test_settings[1]))

    wait(10)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('print_gift_receipt')

    # select 2 items
    Location(254, 214).click( )
    Location(241, 346).click( )
    # print gift receipt
    general_buttons.gift_receipt_key_pad_btns_click('PRINT')

    # general end of test case
    general_functions.end_of_test_case( )


def gift_receipt_from_transaction():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('print gift receipt from transaction')

    # make test receipt and get it to print it as a gift receipt
    get_receipt_for_gift_receipt(general_functions.make_test_receipts(l_test_settings[0], l_test_settings[1]))

    wait(10)
    # select all transaction items
    general_buttons.gift_receipt_key_pad_btns_click('SELECT ALL')

    # print gift receipt
    sleep(2)
    general_buttons.gift_receipt_key_pad_btns_click('PRINT')

    # general end of test case
    general_functions.end_of_test_case( )


def get_receipt_for_gift_receipt(receipt_number):
    # go to the search form to select the receipt that needs to be printed as gift receipt
    wait(10)
    general_buttons.main_page_footer_menu_btns_click('OTHER')

    general_buttons.main_page_other_menu_btns_click('PRINT GIFT RECEIPT')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('search_receipt')

    # select receipt to print
    type(Key.ENTER)
    type(Key.ENTER)
    type(Key.ENTER)
    print('receipt_number: ' + str(receipt_number))
    type(str(receipt_number))
    type(Key.ENTER)