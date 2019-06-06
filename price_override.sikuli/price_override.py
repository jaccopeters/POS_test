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
l_test_settings = test_settings.price_override(locale)

def price_override():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('price override')
    
    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])
    wait(2)
    # decrease price of first article 
    click(Location(256, 188)) # first article
    general_buttons.basket_page_key_pad_btns_click('PRICE OVERRIDE')
    # general_buttons.click_element('basket_page_end_editing_key_pad', 100, -40, 'price override btn')

    wait(2)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('price_override')

    type('44,90') # given new price
    type(Key.ENTER) # confirm

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('price_override_reasons')
    
    
    type(Key.ENTER) # select & confirm price override reason

    # increase price of second item
    click(Location(256, 188))  # first article
    general_buttons.basket_page_key_pad_btns_click('PRICE OVERRIDE')
    # general_buttons.click_element('basket_page_end_editing_key_pad', 100, -40, 'price override btn')

    type('64,90') # given new price

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('price_override')

    type(Key.ENTER) # confirm
    type(Key.DOWN) # select price override reason

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('price_override_reasons')

    type(Key.ENTER) # confirm price override reason
    
    # test_cases.price_override_tc_0010("are the override amounts OK?")

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(5)
    # general_functions.extended_wait('four_eyes_form', 60)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['DINERS', 'REST']])

    general_functions.end_of_test_case()