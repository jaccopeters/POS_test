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
l_test_settings = test_settings.non_merchandise_sale_test_settings()


def non_merchandise_sale():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('non merchandise sale all types')
    general_functions.extended_wait("main_page_key_pad", 300)

    print('length: ' + str(len(l_test_settings)))

    for transaction in l_test_settings:

        general_buttons.main_page_items_gv_menu_btns_click('NON MERCHANDISE SALE')

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('non_merchandise_sale_footer')

        general_buttons.main_page_items_gv_menu_non_merchandise_sale_btns_click(transaction[0])

        wait(0.5)

        # enter price
        type(str(transaction[1]))

        # confirm
        type(Key.ENTER)


    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')

    wait(2)

    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    wait(2)

    general_functions.pay_transaction_with_multiple_tenders([['AMEX', 'REST']])

    general_functions.end_of_test_case( )