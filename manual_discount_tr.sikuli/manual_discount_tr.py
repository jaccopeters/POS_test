from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.manual_discount()

def manual_discount_tr():
    general_functions.errorhandling("ABORT")
    general_functions.extended_wait("main_page_key_pad", 300)

    print('length: ' + str(len(l_test_settings)))
    x = 0

    while x < len(l_test_settings):
        print('x: ' + str(x))
        y = l_test_settings[x]
        print('y: ' + str(y))

        # get article
        general_functions.fill_basket(y[0], y[1])

        # click DISCOUNT buttons
        general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

        # click ITEM DISCOUNT% button
        general_buttons.basket_page_discounts_menu_btns_click('TRANSACTION DISCOUNT TENDER')

        # enter discount
        discount = y[2]
        print('discount: ' + str(discount))
        type(str(discount))

        # confirm
        type(Key.ENTER)

        if x < 10:  # first page with reasons
            # click discount reason

            general_buttons.return_reasons_click('return reason ' + str(x + 1))

            print('return reason: ' + 'return reason ' + str(x + 1))

            # confirm reason
            type(Key.ENTER)
        else:
            if x == 10:
                print("reason 11")
                type(Key.RIGHT)
                type(Key.ENTER)
            else:
                print("reason 12")
                type(Key.RIGHT)
                type(Key.DOWN)
                type(Key.ENTER)
            print("x: " + str(x))

        # click TOTAL button
        general_buttons.main_page_key_pad_btns_click('TOTAL')

        general_functions.start_of_test_case('manual discount on transaction')
        wait(5)
        # general_functions.extended_wait('four_eyes_form', 60)
        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

        general_functions.extended_wait('payment_page_key_pad', 30)

        general_functions.pay_transaction_with_multiple_tenders([['MAESTRO', 'REST']])

        general_functions.end_of_test_case( )

        x = x + 1

    general_functions.end_of_test_case()
