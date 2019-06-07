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
l_test_settings = test_settings.cancel_receipt_test_settings()


def cancel_receipt():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC cancel receipt all reasons')

    x = 0
    while x < len(l_test_settings):
        y = l_test_settings[x]
        print("y: " + str(y))
        
        # wait for the main screen to be there
        general_functions.extended_wait('main_page_key_pad', 30)

        general_functions.fill_basket(y[0], y[1])

        if y[2]== 1:  # cancel before the total button is clicked
            general_functions.start_of_test_case('TC cancel receipt before total button is clicked')
            receipt_meta_data_array = general_functions.get_receipt_meta_data()
            general_buttons.main_page_key_pad_btns_click('CANCEL')
        else: # cancel after the total button is clicked
            # click TOTAL button
            general_buttons.main_page_key_pad_btns_click('TOTAL')
            general_functions.start_of_test_case('TC cancel receipt after total button is clicked')
            receipt_meta_data_array = general_functions.get_receipt_meta_data()
            # this is actually the CANCEL TRANSACTION button but it's in the same location as the CANCEL button
            general_buttons.main_page_key_pad_btns_click('CANCEL')

        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('cancellation_warning')

        # confirm cancellation
        type(Key.ENTER)

        # short wait to get cancellation reason screen in focus
        wait(0.5)

        # use all cancelation reasons

        # general_functions.general_message_with_subject('test', 'cancellation_reasons')

        wait(5)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('cancellation_reasons')

        button_name = 'LIST ITEM  ' + str(x+1)
        print('cancel reason: ' + button_name)

        general_buttons.click_in_list(button_name)

        # confirm reason
        type(Key.ENTER)

        x = x + 1
        print("x: " + str(x))
        if x == 3:
            break

    # to return to the main screen

    wait(10)
    general_functions.end_of_test_case()
