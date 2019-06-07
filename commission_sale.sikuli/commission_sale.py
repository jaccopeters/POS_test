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
l_test_settings = test_settings.commission_sale()


def line_items():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC commission sale line item')
    
    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])

    # select first line item
    Location(254, 214).click()

    general_buttons.main_page_key_pad_btns_click('SALES PERSON')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('sales_person_search')

    sleep(2)
    type(Key.ENTER)
    sleep(2)
    type(Key.ENTER)
    # general_functions.pause_test_case_msg()

    # select first line item
    Location(254, 214).click()

    general_buttons.main_page_key_pad_btns_click('SALES PERSON')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('select_sales_person')

    sleep(2)
    type(Key.ENTER)
    sleep(2)
    type(Key.DOWN)
    type(Key.ENTER)
    # general_functions.pause_test_case_msg()

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    receipt_meta_data_array = general_functions.get_receipt_meta_data()	
    if brand == 'TH':  # TH has zalando as tender
        general_functions.pay_transaction_with_multiple_tenders([['MAESTRO', 'REST']])
    else:
        general_functions.pay_transaction_with_multiple_tenders([['MAESTRO', 'REST']])

    general_functions.end_of_test_case()

def transaction():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('commission sale line transaction')
    
    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])
    # select first line item
    general_buttons.main_page_key_pad_btns_click('SALES PERSON')
    type(Key.ENTER)
    type(Key.ENTER)

    # general_buttons.click_element_in_region('basket_page_key_pad_end_editing', 100, 100, 'END EDITING btn', general_functions.get_key_pad_area(), 0.7)

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    receipt_meta_data_array = general_functions.get_receipt_meta_data()
    general_functions.pay_transaction_with_multiple_tenders([['MAESTRO', 'REST']])

    general_functions.end_of_test_case()