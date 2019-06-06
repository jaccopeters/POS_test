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
l_test_settings = test_settings.remove_promotion(locale)


def remove():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC remove promotion')

    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])
    wait(5)

    # select first line item
    Location(254, 214).click()

    general_buttons.basket_page_edit_line_item_click('REMOVE PROMOTION')

    general_buttons.item_editing_key_pad_btns_click('END EDITING')

    general_buttons.basket_page_key_pad_btns_click('TOTAL')

    receipt_meta_data_array = general_functions.get_receipt_meta_data( )

    general_functions.pay_transaction_with_multiple_tenders([['VISA', 'REST']])

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('payment_screen')

    wait(1)

    # type(Key.ENTER)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    general_functions.end_of_test_case()