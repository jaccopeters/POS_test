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
l_test_settings = test_settings.tax_free_test_settings()


global l_test_aftersales_settings
#l_test_settings = test_settings.basic_sale_off_line_card_test_settings(locale)
l_test_aftersales_settings = test_settings.tax_free_aftersales_test_settings()

global receipt_meta_data_array
receipt_meta_data_array = general_functions.get_receipt_meta_data()


def issue_tax_form_basic_sale_any_tender():
    y = l_test_settings[0]
    
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC Issue tax form on basic sale paid with ' + str('card AMEX, paying exact amount.'))
    
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
    #DE#click(Location(200, 490)) 
    #BE#
    click(Location(200, 470))
    type('1')
    type(Key.DOWN)
    type(Key.ENTER)
    
    # mandatory field2: select a tender
    # click area
    #DE#click(Location(535, 235))
    #BE#
    click(Location(580, 220))
    type('4') 
    type(Key.DOWN)
    type(Key.ENTER)
    
    # select the Yes button to submit the Issue tax form
    ##
    wait(1)
    ##
    type(Key.ALT+'y')
    
    ##
    wait(16)
    # general end of test case
    general_functions.end_of_test_case()



def issue_tax_form_after_sale_any_tender():
    ##y = l_test_settings[0]
    
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC Issue tax form on AFTER sale with ' + str('receipt number ...'))
    
    # create a receipt with_number to retrieve for after sales tax free form test case
    #is ok now#
    receipt_number = general_functions.make_test_receipts(l_test_aftersales_settings[0], l_test_aftersales_settings[1])

    #is ok now#
    print('receipt_number: ' + receipt_number)

    #is ok now#
    general_functions.extended_wait('main_page_key_pad', 30)

    # # select the Customer button to go to Issue tax form button
    #is ok now#
    wait(1)
    general_buttons.main_page_footer_menu_btns_click('CUSTOMER')
    
    # # select the Issue tax form button
    wait(0.1)
    #is ok now#
    general_buttons.main_page_customer_menu_btns_click_taxfree('ISSUE TAX FREE')

    #is ok now#
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
    
    # # select the OK button to show the Issue tax form pop-up confirmation
    #is ok now# 
    click(Location(900, 700))
    
    # # select the OK button to show the Issue tax form
    #is ok now#
    click(Location(810, 584))
    
    wait(1)
    general_functions.extended_wait('TFF', 30)
    
    
    # # # 'Verify steps after this point ', 'are ok now.'
    #is ok now#
    # general_functions.show_value__msg('Tax free form requested', 'Global Blue form pulled up to be ready')
    # wait(0.5)

    #review 1st#
    # # mandatory field1: select a country
    # # click area
    click(Location(200, 510))
    type('1')
    type(Key.DOWN)
    type(Key.ENTER)
    
    # # mandatory field2: select a tender
    # # click area
    click(Location(660, 250))
    type('4') 
    type(Key.DOWN)
    type(Key.ENTER)
    
    # # Enter at least mandatory fields: country and tender
    # # 'Verify steps after this point ', 'are ok now.'
    #general_functions.show_value__msg('Verify steps after this point ', 'are ok now.')
    
    
    # # select the Yes button to submit the Issue tax form
    wait(1)
    type(Key.ALT+'y')
    
    ##wait(16)
    wait(6)
    # general end of test case
    general_functions.end_of_test_case()