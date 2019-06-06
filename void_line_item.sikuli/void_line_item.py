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
l_test_settings = test_settings.void_line_item_test_settings()

def void_line_item():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC void line item')
    
    wait(1)

    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])

    time.sleep(5)

    print("VOID LINE ITEM")
    # void line item
    general_buttons.click_element('add_or_substract_product', -100, 0, 'PLUS or MINUS btn')
    time.sleep(5)

    #test_cases.void_line_item_tc_0010('is the line item voided ')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('is_the_line_item_voided')

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_functions.extended_wait('payment_page_key_pad', 30)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('payment_screen')

    general_functions.pay_transaction_with_multiple_tenders(l_test_settings[2])

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')
    
    general_functions.end_of_test_case()
