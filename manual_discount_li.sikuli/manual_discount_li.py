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
l_test_settings = test_settings.manual_discount( )


def manual_discount_li():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('manual discount on line items all discount reasons')
    general_functions.extended_wait("main_page_key_pad", 300)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    x = 0

    for transaction in l_test_settings:

        #  first item in basket
        if x == 0:
            general_functions.fill_basket(l_test_settings[0][0], l_test_settings[0][1])
        # add item in basket
        elif x > 0:
            general_buttons.click_element('add_or_substract_product', 100, 0, 'PLUS btn')

        # click DISCOUNT buttons
        general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('discounts_footer')

        # click ITEM DISCOUNT% button
        general_buttons.basket_page_discounts_menu_btns_click('ITEM DISCOUNT %')

        # TEST CASE
        if is_gui_test == 'YES':
            gui_screens.check_gui_element('total_discount')

        # enter discount
        type(str(l_test_settings[x][2]))

        # confirm
        type(Key.ENTER)

        if x < 10:  # first page with reasons
            # click discount reason
            y_coordinate = -200 + (45 * x)
            #general_buttons.click_element('discount_reasons_1', 0, y_coordinate, 'one of the discount reasons btn')
            general_buttons.click_in_list('LIST ITEM ' + str(x+1))

            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('discount_reasons_page_1')


            # confirm reason
            type(Key.ENTER)
        else:
            if x == 10:
                print("reason 11")
                type(Key.RIGHT)
                # TEST CASE
                if is_gui_test == 'YES':
                    gui_screens.check_gui_element('discount_reasons_page_2')
                
                type(Key.ENTER)
            else:
                print("reason 12")
                type(Key.RIGHT)
                type(Key.DOWN)
                type(Key.ENTER)
            print("x: " + str(x))

        x = x + 1

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')

    wait(5)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    general_functions.extended_wait('payment_page_key_pad', 30)

    general_functions.pay_transaction_with_multiple_tenders([['CHINA UNION PAY', 'REST']])

    general_functions.end_of_test_case()