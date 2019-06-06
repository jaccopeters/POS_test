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
l_test_settings = test_settings.item_not_found()


def item_not_found():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC item not found all divisions test ')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    time.sleep(5)

    if is_gui_test == 'YES':
        # for the GUI test 1 division is enough
        number_of_divisions = 1
    else:
        number_of_divisions = l_test_settings[0]

    for div in range(0, number_of_divisions):

        general_buttons.main_page_items_gv_menu_btns_click('ITEM NOT FOUND')

        if div == 0:
            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('item_not_found')

        division = "DIV " + str(div + 1)

        print('division: ' + str(division))

        general_buttons.main_page_items_gv_menu_item_not_found_btns_click(division)

        type("123456789")

        type(Key.ENTER)
        amount = 50 + div
        type(str(amount) + ".00")

        type(Key.ENTER)

    # click the TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_functions.extended_wait('four_eyes_form', 60)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    general_functions.extended_wait('payment_page_key_pad', 60)

    general_functions.pay_transaction_with_multiple_tenders(l_test_settings[1])

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    # general end of test case
    general_functions.end_of_test_case()