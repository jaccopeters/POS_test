from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time
import string


global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings()
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.local_employee_discount(locale)


def local_employee_discount_line_item(settings_index):

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('employee discount on line item')
    general_functions.extended_wait("main_page_key_pad", 300)

    settings_for_this_test = l_test_settings[settings_index]
    general_functions.fill_basket(settings_for_this_test[0], settings_for_this_test[1])
    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    add_employee(settings_for_this_test)

    general_buttons.basket_page_employee_discounts_menu_btns_click('EMPLOYEE ITEM DISCOUNT')

    general_buttons.basket_page_employee_percentage_discounts_menu_btns_click(settings_for_this_test[4])

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(3)
    general_functions.extended_wait('four_eyes_form', 60)

    general_functions.extended_wait('payment_page_key_pad', 30)
    # general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])    
    general_functions.pay_transaction_with_tender([['tender', 'DINERS']])

    general_functions.end_of_test_case()


def local_employee_discount_transaction(settings_index):

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('employee discount on transaction')
    general_functions.extended_wait("main_page_key_pad", 300)

    settings_for_this_test = l_test_settings[settings_index]

    general_functions.fill_basket(settings_for_this_test[0], settings_for_this_test[1])
    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    add_employee(settings_for_this_test) # add employee data

    # test_cases.does_part_of_screen_exist('employee_search_screen', 0.5, 'are all elements on the employee_search_screen OK')
    # test_cases.does_part_of_screen_exist('employee_discount_btns', 0.5, 'are the right buttons present in the employee discount menu?')

    general_buttons.basket_page_employee_discounts_menu_btns_click('EMPLOYEE TRANSACTION DISCOUNT')

    general_buttons.basket_page_employee_percentage_discounts_menu_btns_click(settings_for_this_test[5])

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(3)
    # general_functions.extended_wait('four_eyes_form', 60)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['DINERS', 'REST']])

    general_functions.end_of_test_case()


def local_employee_discount_remove_employee(settings_index):

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('employee discount remove employee')
    general_functions.extended_wait("main_page_key_pad", 300)

    settings_for_this_test = l_test_settings[settings_index]
    general_functions.fill_basket(settings_for_this_test[0], settings_for_this_test[1])
    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    add_employee(settings_for_this_test) # add employee data

    general_buttons.basket_page_employee_discounts_menu_btns_click('EMPLOYEE ITEM DISCOUNT')

    general_buttons.basket_page_employee_percentage_discounts_menu_btns_click(settings_for_this_test[5])

    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    general_buttons.basket_page_employee_discounts_menu_btns_click('REMOVE EMPLOYEE')

    type(Key.ENTER)

    # test_cases.does_part_of_screen_exist('employee_and_discount_are_removed', 0.7, 'are employee and discount removed')

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(5)
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['WECHAT', 'REST']])

    general_functions.end_of_test_case()


def local_employee_discount_remove_line_item_discount(settings_index):

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('employee discount remove line item discount')
    general_functions.extended_wait("main_page_key_pad", 300)

    settings_for_this_test = l_test_settings[settings_index]
    general_functions.fill_basket(settings_for_this_test[0], settings_for_this_test[1])
    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    add_employee(settings_for_this_test) # add employee data

    general_buttons.basket_page_employee_discounts_menu_btns_click('EMPLOYEE ITEM DISCOUNT')

    general_buttons.basket_page_employee_percentage_discounts_menu_btns_click(settings_for_this_test[5])

    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    general_buttons.basket_page_employee_discounts_menu_btns_click('REMOVE ITEM DISCOUNT')


    type(Key.ENTER)

    # test_cases.does_part_of_screen_exist('discount_is_removed_but_the_employee_isnt', 0.7, 'is the line item discount removed and is the employee still there')

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(5)
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_multiple_tenders([['MAESTRO', 'REST']])

    general_functions.end_of_test_case()


def local_employee_discount_remove_transaction_discount(settings_index):

    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('employee discount remove transaction discount')
    general_functions.extended_wait("main_page_key_pad", 300)

    settings_for_this_test = l_test_settings[settings_index]
    general_functions.fill_basket(settings_for_this_test[0], settings_for_this_test[1])
    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    add_employee(settings_for_this_test) # add employee data

    general_buttons.basket_page_employee_discounts_menu_btns_click('EMPLOYEE TRANSACTION DISCOUNT')

    general_buttons.basket_page_employee_percentage_discounts_menu_btns_click(settings_for_this_test[5])

    general_buttons.basket_page_footer_menu_btns_click('DISCOUNTS')

    general_buttons.basket_page_employee_discounts_menu_btns_click('REMOVE TRANSACTION DISCOUNT')

    type(Key.ENTER)    
	# type(Key.ENTER)

    # test_cases.does_part_of_screen_exist('discount_is_removed_but_the_employee_isnt', 0.7, 'is the line item discount removed and is the employee still there')

    # click TOTAL button
    general_buttons.main_page_key_pad_btns_click('TOTAL')
    wait(5)
    general_functions.extended_wait('payment_page_key_pad', 30)
    general_functions.pay_transaction_with_tender([['tender', 'MAESTRO']])
    type(Key.ENTER)
    general_functions.end_of_test_case()


def add_employee(settings_for_this_test):
    general_buttons.basket_page_discounts_menu_btns_click('ADD EMPLOYEE')

    type(settings_for_this_test[2])  # enter employee number
	
    type(Key.ENTER)
    type(Key.ENTER)

    print('employee selected')
    general_functions.extended_wait("basket_page_key_pad", 300)



