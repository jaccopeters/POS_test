from sikuli import *
import general_functions
import general_buttons
import test_cases
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
#l_test_settings = test_settings.basic_sale_off_line_card_test_settings(locale)
l_test_settings = test_settings.issue_tax_free_form_test_settings(locale)

global receipt_meta_data_array
receipt_meta_data_array = general_functions.get_receipt_meta_data()


def issue_tax_form_basic_sale_any_tender():
    y = l_test_settings[0]
    
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('Issue tax form on basic sale paid with ' + str('card AMEX, paying exact amount.'))
    
    # fil basket and press total button
    wait(0.1)
    general_functions.fill_basket(y[0], y[1])
    #wait(0.1)
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    
    # select the Other button to go to Issue tax form button
    wait(0.1)
    general_buttons.payment_page_footer_menu_btns_click('OTHER')
    
    # select the Issue tax form button
    #wait(0.1)
    general_buttons.payment_page_other_menu_btns_click('ISSUE TAX FREE')
    
    # 'Verify steps after this point ', 'are ok now.'
    #general_functions.show_value__msg('Tax free form requested', 'Global Blue form pulled up to be ready')
    wait(0.5)
    general_functions.extended_wait('payment_page_key_pad', 30)
    #wait(0.1)
    general_functions.get_receipt_meta_data()
    wait(1)
    general_functions.pay_transaction_with_multiple_tenders([['AMEX', 'REST']])
    
    # select the OK button to show the Issue tax form
    wait(1)
    click(Location(810, 584))
    wait(1)
    general_functions.extended_wait('TFF', 30)
    
    # Enter at least mandatory fields: country and tender
    # 'Verify steps after this point ', 'are ok now.'
    #general_functions.show_value__msg('Verify steps after this point ', 'are ok now.')
    
    # mandatory field1: select a country
    # click area
    click(Location(200, 490))
    type('1')
    type(Key.DOWN)
    type(Key.ENTER)
    
    # mandatory field2: select a tender
    # click area
    click(Location(535, 235))
    type('4') 
    type(Key.DOWN)
    type(Key.ENTER)
    
    # select the Yes button to submit the Issue tax form
    wait(1)
    type(Key.ALT+'y')
    
    wait(6)
    # general end of test case
    general_functions.end_of_test_case()