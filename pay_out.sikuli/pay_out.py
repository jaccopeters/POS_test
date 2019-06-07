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
l_test_settings = test_settings.pay_out()


def pay_out():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC pay out')
    general_functions.extended_wait("main_page_key_pad", 300)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    for z in range(0, l_test_settings[0]):

        general_buttons.main_page_footer_menu_btns_click('OTHER')

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('other_screen')

        general_buttons.main_page_other_menu_btns_click('PAY-OUT')

        # four eyes authorization
        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

        # select pay_out reason
        
        print('list item: ' + 'LIST ITEM ' + str(z+1))
        general_buttons.click_in_list('LIST ITEM ' + str(z+1))

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('pay_out_reasons')

         # confirm reason
        type(Key.ENTER)

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('pay_out_total_amount_screen')


        # amount that's payed out
        type(str(z+1) + '.00')

        # confirm amount
        type(Key.ENTER)

        wait(3)

        receipt_meta_data_array = general_functions.get_receipt_meta_data( )

        # click CASH button
        general_buttons.pay_out_key_pad_click('CASH')


        # confirm pay out
        type(Key.ENTER)

        general_functions.close_drawer_msg()

        general_functions.start_of_test_case('pay out ' + 'LIST ITEM ' + str(z+1))

        z =+ 1


    general_functions.start_of_test_case('cancel pay out')

    general_buttons.main_page_footer_menu_btns_click('OTHER')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('other_screen')

    general_buttons.main_page_other_menu_btns_click('PAY-OUT')

    # four eyes authorization
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    # select and confirm pay out reason
    # general_functions.general_message('select pay out reason')
    type(Key.ENTER)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('pay_out_reasons')

    # type amount that's payed out
    # general_functions.general_message('type amount that's payed out')
    type("9.99")

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('pay_out_total_amount_screen')


    # confirm amount
    # general_functions.general_message('confirm amount')
    type(Key.ENTER)

    wait(3)

    #get receipt data and save it
    receipt_meta_data_array = general_functions.get_receipt_meta_data( )

    # click CANCEL TRANSACTION button
    #general_functions.general_message('CANCEL')
    general_buttons.basket_page_key_pad_btns_click('CANCEL')

    # four eyes authorization
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    type(Key.ENTER)
    type(Key.ENTER)

    # general_functions.general_message('end of payout')

    general_functions.end_of_test_case()
