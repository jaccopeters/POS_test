from sikuli import *
import general_functions
import general_buttons
import test_settings
import time

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global brand
brand = l_general_test_settings[6]
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.basic_sale_chf_eur_test_settings(locale)


def basic_sale_chf_to_eur():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('convert CHF to EUR basic sale')

    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
    
    general_buttons.payment_page_other_tenders_menu_btns_click('ZALANDO')

    general_functions.extended_wait('payment_page_key_pad', 1)

    general_functions.pay_transaction_with_multiple_tenders([['CASH', 'REST']])
    
    # general end of test case
    general_functions.end_of_test_case()