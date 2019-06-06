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
l_test_settings = test_settings.returns()


def returns_with_receipt():
    general_functions.start_of_test_case('TC returns with receipt line items')

    receipt_number = general_functions.make_test_receipts(l_test_settings[0], l_test_settings[1])

    print('receipt_number: ' + receipt_number)

    general_functions.extended_wait('main_page_key_pad', 30)

    returns_with_receipt_return_items(receipt_number)

    if l_general_test_settings[13] != 'IT':
        general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_functions.extended_wait('four_eyes_form', 60)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['CHINA UNION PAY', 'REST']])

    general_functions.end_of_test_case( )


def returns_with_receipt_and_exchange():
    general_functions.start_of_test_case('TC returns with receipt and exchange')
    receipt_number = general_functions.make_test_receipts(l_test_settings[0], l_test_settings[1])

    print('receipt_number: ' + receipt_number)

    general_functions.extended_wait('main_page_key_pad', 30)

    returns_with_receipt_return_items(receipt_number)

    # click SEARCH ITEM button

    general_buttons.main_page_key_pad_btns_click('ITEM SEARCH')

    # move to next line on search form
    type(Key.ENTER)
    # article number
    type(l_test_settings[0])
    # click SEARCH button
    # article_search_form_en_GB.png"
    general_buttons.click_element('article_search_form', 300, 40, 'search btn')
    # add product(s)
    z = 0
    print('number of products: ' + str(l_test_settings[1]))
    while z < l_test_settings[1] - 2:
        general_buttons.click_element('add_or_substract_product', 100, 0, 'PLUS btn')
        z += 1
        print('z: ' + str(z))

    general_buttons.main_page_key_pad_btns_click('TOTAL')
    general_functions.extended_wait('four_eyes_form', 60)
    # In case of italy there is no 4 eyes
    if l_general_test_settings[13] != 'IT':
        general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    general_functions.extended_wait('payment_page_key_pad', 60)
    general_functions.pay_transaction_with_multiple_tenders([['DINERS', 'REST']])

    general_functions.end_of_test_case( )


def returns_with_receipt_return_items(receipt_number):
    general_functions.errorhandling("ABORT")

    general_buttons.main_page_items_gv_menu_btns_click('RETURNS WITH RECEIPT')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('goods_return')

    wait(2)

    type(l_general_test_settings[1])  # store
    type(Key.ENTER)
    type(Key.ENTER)  # date is today
    type(l_general_test_settings[7])  # till
    type(Key.ENTER)
    print(str(receipt_number))
    type(str(receipt_number))  # receipt#
    type(Key.ENTER)  # confirm receipt

    wait(5)

    click(Location(250, 210))
    wait('return_reasons_' + locale + '.png', 30)
    general_buttons.click_in_list('LIST ITEM 1')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('goods_return')

    type(Key.ENTER)

    click(Location(250, 350))
    wait('return_reasons_' + locale + '.png', 30)
    general_buttons.click_in_list('LIST ITEM 2')    
    type(Key.ENTER)

    click(Location(250, 540))
    wait('return_reasons_' + locale + '.png', 30)
    general_buttons.click_in_list('LIST ITEM 3')    
    type(Key.ENTER)

    general_buttons.main_page_items_gv_menu_returns_with_receipt_btns_click('RETURN SELECTION')



def finish_returns():
    # finish return
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    general_functions.extended_wait('four_eyes_form', 60)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['VISA', 'REST']])
