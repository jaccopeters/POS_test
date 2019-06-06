# general modules
from sikuli import *
from datetime import datetime
import general_functions
import general_buttons
import time
import test_settings
import test_cases


# test modules
import pay_in
import pay_out
import drop_off
import item_not_found
import void_line_item
import basic_sale

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings()
global locale
locale = l_general_test_settings[8]
l_base_dir = ocale = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.basic_sale_off_line_card_test_settings(locale)


def cancel_receipt():
    general_functions.errorhandling("ABORT")
    l_test_settings = test_settings.void_tender_type_settings(locale)
    l_general_test_settings = test_settings.general_test_settings()

    x = 0
    while x < len(l_test_settings):
        y = l_test_settings[x]
        print("y: " + str(y))

        general_functions.fill_basket(y[0], y[1])

        if y[5]== 1:  # cancel before the total button is clicked
            general_buttons.click_element('secondary_pages_key_pad', 190, -100, 'CANCEL btn')
        else:
            # click TOTAL button
            general_buttons.click_element('secondary_pages_key_pad', 100, 100, 'TOTAL btn')
			receipt_meta_data_array = general_functions.get_receipt_meta_data()			
            general_buttons.click_element('secondary_pages_key_pad_after_TOTAL', 190, -100,
                                          'CANCEL TRANSACTION btn')

        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

        test_cases.errors_and_warnings_tc_0030("does the cancellation warning pop up")

        # confirm cancelation
        type(Key.ENTER)

        # use all cancelation reasons

        y_coordinaat = (160 + (x * 50)) * -1
        print("y_coordinaat: " + str(y_coordinaat))
        general_buttons.click_element('cancelation_reasons', 0, y_coordinaat, 'CANCEL REASON btn')

        # confirm reason
        type(Key.ENTER)

        x = x + 1
        print("x: " + str(x))
        if x == 3:
             break