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
l_test_settings = test_settings.gv_sale_and_redemption()


def gv_sale():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC gift voucher sale and redemption')

    wait(10)

    general_buttons.main_page_footer_menu_btns_click('ITEMS GV')

    general_buttons.main_page_items_gv_menu_btns_click('GIFT VOUCHER SALE')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('sale_gift_voucher')

    type(l_test_settings[0])

    type(Key.ENTER)

    general_functions.extended_wait("payment_page_key_pad_TOTAL", 300)

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_functions.extended_wait("payment_page_key_pad", 300)

    # general_functions.pause_test_case_msg()

    receipt_meta_data_array = general_functions.get_receipt_meta_data( )
    print('receipt_meta_data_array: ' + str(receipt_meta_data_array))

    r = Region(165, 183, 221, 21)
    r.highlight(2)
    evaluation_string = r.text( )

    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("I", "1")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("O", "0")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("o", "0")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("|", "1")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("l", "1")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace(" ", "")
    print("evaluation str " + evaluation_string)
    evaluation_string = evaluation_string.replace("?", "9")
    print("evaluation str " + evaluation_string)

    gv_number = evaluation_string
    print("gv number " + gv_number)

    general_functions.writeTestResults("gift voucher number", "", gv_number, "", "", "", "", "")

    if brand == "CK":
        general_functions.general_message_with_subject('Check the GV number', 'The GV number we found is ' + gv_number + '. If this not the correct number please write the correct nunmber down on a piece of paper')

    general_functions.pay_transaction_with_multiple_tenders([['CHINA UNION PAY', 'REST']])

    general_functions.fill_basket(l_test_settings[2], l_test_settings[3])

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_functions.pay_transaction_with_multiple_tenders([['GIFT VOUCHER', gv_number, 'REST']])

    general_functions.end_of_test_case( )