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
l_base_dir = l_general_test_settings[10]


def promotions():

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('promotions')

    l_test_settings = test_settings.promotions()

    x = 0
    while x < len(l_test_settings):
        y = l_test_settings[x]
        print("y: " + str(y))

        general_functions.fill_basket(y[0], y[1])
        general_buttons.main_page_key_pad_btns_click('TOTAL')

        general_functions.pay_transaction_with_multiple_tenders([['DINERS', 'REST']])

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('payment_screen')

        wait(1)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('main_page')

        x += 1

    general_functions.end_of_test_case( )


def bonus_buys():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('bonus buys')

    l_test_settings = test_settings.bonus_buys()

    x = 0
    while x < len(l_test_settings):
        y = l_test_settings[x]
        print("y: " + str(y))

        general_functions.fill_basket(y[0], y[1])
        general_buttons.main_page_key_pad_btns_click('TOTAL')
        general_functions.pay_transaction_with_multiple_tenders([['ALIPAY', 'REST']])

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('payment_screen')

        wait(1)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('main_page')


        x += 1

    general_functions.end_of_test_case( )
