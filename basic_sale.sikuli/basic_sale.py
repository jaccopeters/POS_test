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
l_test_settings = test_settings.basic_sale_off_line_card_test_settings()

def basic_sale_off_line_card():
    general_functions.errorhandling("ABORT")

    x = 0
    while x < len(l_test_settings):

        y = l_test_settings[x]

        general_functions.start_of_test_case('basic sale paid with ' + str(y[2]))

        wait(1)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('main_page')

        general_functions.fill_basket(y[0], y[1])

        general_buttons.main_page_key_pad_btns_click('TOTAL')

        general_functions.extended_wait('payment_page_key_pad', 30)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('payment_screen')

        general_functions.pay_transaction_with_multiple_tenders(y[2])

        wait(1)

        # type(Key.ENTER)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('main_page')

        print('x: ' + str(x))
        x += 1

    # general end of test case
    general_functions.end_of_test_case()