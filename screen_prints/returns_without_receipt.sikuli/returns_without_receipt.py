from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time
import string
import returns_with_receipt

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings()
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.returns(locale)


def returns_with_out_receipt_item_not_found():
    general_functions.start_of_test_case('returns without receipt item not found')
    # add items to be returned
    returns_with_out_receipt_add_return_items()
    # finish returns
    returns_with_receipt.finish_returns()
    # general end of test case
    general_functions.end_of_test_case()

def returns_with_out_receipt_item_not_found_and_exchange():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('returns without receipt item not found and exchange')
    # add items to be returned
    returns_with_out_receipt_add_return_items()

    # click SEARCH ITEM button
    general_buttons.main_page_key_pad_btns_click('ITEM SEARCH')

    # move to next line on search form
    type(Key.ENTER)

    # article number
    type(l_test_settings[0])

    # click SEARCH button
    general_buttons.article_search_form_btns_click('SEARCH')

    general_functions.extended_wait('basket_page_key_pad', 30)

    # finish returns
    returns_with_receipt.finish_returns()

    # general end of test case
    general_functions.end_of_test_case()


def returns_with_out_receipt_add_return_items():

    x = 0
    while x < 3:

        general_functions.extended_wait('main_page_key_pad', 30)

        general_buttons.main_page_items_gv_menu_btns_click('RETURNS NO RECEIPT')

        wait(2)

        general_buttons.main_page_items_gv_menu_returns_no_receipt_btns_click('ITEM NOT FOUND')

        general_buttons.main_page_items_gv_menu_item_not_found_btns_click('DIV ' + str(x + 1))

        type('1234567890')

        type(Key.ENTER)

        price = (x + 1) * 11

        type(str(price) + ',' + str(price))

        type(Key.ENTER)

        # this is different in italy

        type('1234-1234')

        #END RETURNS
		general_buttons.returns_page_key_pad_btns_click('END RETURNS')

        general_buttons.main_page_key_pad_btns_click('TOTAL')

        general_functions.extended_wait('return_reasons', 30)

        general_buttons.click_element('return_reasons', -70, -30 + (45 * x), 'select return reason')
        type(Key.ENTER)

        x += 1

    general_buttons.returns_page_key_pad_btns_click('END RETURNS')


def with_loyalty_number():
    general_functions.start_of_test_case('returns without receipt with loyalty number')

    # add items to be returned
    returns_with_out_receipt_add_return_items()
    wait(1)

    # customer add loyalty number

    general_buttons.basket_page_returns_footer_menu('CUSTOMER btn', 200, 0)

    general_buttons.click_element('basket_page_customer_menu', -200, -70, 'ENTER LOYALTY NUMBER btn')
    type(l_test_settings[2])
    type(Key.ENTER)
    type(Key.ENTER)

    general_buttons.click_element('basket_page_customer_loyalty_menu', 70, -70, 'ENTER VOUCHER NUMBER btn')
    type(l_test_settings[3])
    type(Key.ENTER)
    type(Key.ENTER)

    general_buttons.click_element('secondary_pages_key_pad', 100, 100, 'TOTAL btn')
    receipt_meta_data_array = general_functions.get_receipt_meta_data()
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    type(Key.ENTER)
    general_functions.pay_transaction_with_tender([['tender','MAESTRO']])

    # general end of test case
    general_functions.end_of_test_case()