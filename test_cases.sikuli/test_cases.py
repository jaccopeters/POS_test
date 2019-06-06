from sikuli import *
import time
import string
import glob

import general_functions
import general_buttons
import test_cases
import test_settings
import returns_with_receipt

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings()
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.returns()

'''
TEST CASES

item not found
0010 does the main screen look OK?
0020 does the

drop off
0010 is the drop off amount correct?

basic sale off ine card
0010 does the the payment processed button appear
0020 if payment processed is canceled do you go back to the basket page?

cancel receipt

void line item
0010 is the line item voided

price override
0010 are the override amounts OK?

local employee discount
0010 are the right buttons present in the employee discount menu

errors and warnings
0010 does the the payment processed button appear
0020 if payment processed is canceled do you go back to the basket page
0030 0010 does the cancellation warning pop up
'''''


def gui_screens_tc_0010_001():
    picture = 'main_screen_complete_' + locale + '.png'

    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults('check main screen layout', "GUI", "gui_test_tc_0010_001", test_result, "", "main page", reg, picture)

def gui_screens_tc_0010_002():
    picture = 'select_sales_person_' + locale + '.png'

    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults('check sales person screen layout', "GUI", "gui_test_tc_0010_002", test_result, "", "main page", reg, picture)

def gui_screens_tc_0010_003():
    picture = 'article_search_form_' + locale + '.png'

    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults('check article search form screen layout', "GUI", "gui_test_tc_0010_003", test_result, "", "main page", reg, picture)


# item not found

# 0010 does the main screen look OK?

def item_not_found_tc_0010(test_case_description):
    l_general_test_settings = test_settings.general_test_settings()
    print("l_general_test_settings 1: " + l_general_test_settings[8])

    picture = 'main_screen_complete_' + locale + '.png'

    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults(test_case_description, "GUI", "home_page_TC_0010_002", test_result, "", "main page", reg, picture)


# drop off

# 0010 is the drop off amount correct?

def drop_off_tc_0010(test_case_description):
    picture = "drop_off_amount_" + locale + '.png'

    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""

    # general_functions.writeTestResults("drop off", "GUI", "drop off TC 0010", test_result, "", "")
    general_functions.writeTestResults(
        test_case_description, "GUI", "home_page_TC_0010_002", test_result, "", "menu level 1 home", reg, picture)


# basic sale off line card

# 0010 does the the payment processed button appear

def basic_sale_off_line_card_tc_0010(test_case_description):
    picture = 'off_line_cards_payment_procesed_pop_up_' + locale + '.png'

    if exists(Pattern(picture).similar(0.60)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.60))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults(test_case_description, "GUI", "basic_sale_off_line_card_TC_0010", test_result, "", "basket page", reg, picture)


# 0020 if payment processed is canceled do you go back to the basket page

def basic_sale_off_line_card_tc_0020(test_case_description):
    picture = 'basket_page_key_pad_and_footer_menu_' + locale + '.png'

    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults(test_case_description, "GUI", "basic_sale_off_line_card_TC_0020", test_result, "", "basket page", reg, picture)

# VOID LINE ITEM

# 0010 is the line item voided

def void_line_item_tc_0010(test_case_description):

    picture = "voided_line_item_" + locale + ".png"
    if exists(Pattern(picture).similar(0.30)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.30))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "void_line_item_tc_0010", test_result, "", " basket page", reg, picture)


# PRICE OVERRIDE
# 0010 are the override amounts OK?
def price_override_tc_0010(test_case_description):

    picture = "price_override_" + locale + ".png"
    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "price_override_tc_0010", test_result, "", " basket page", reg, picture)

# LOCAL EMPLOYEE DISCOUNT
# 0010 are the right buttons present in the employee discount menu
def local_employee_discount_tc_0010(test_case_description):

    picture = "employee_discount_btns_" + locale + ".png"
    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "local_employee_discount_tc_0010", test_result, "", "employee discount menu", reg, picture)


# errors and warnings

# 0010 are the validations for the 4-eyes OK

def errors_and_warnings_tc_0010(test_case_description):
    # non existing user
    type("589423287")
    type(Key.ENTER)
    # supervisor password
    type(l_general_test_settings[5])
    # confirm authentification
    type(Key.ENTER)

    sleep(2)

    picture = "4_eyes_wrong_user_" + locale + ".png"
    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "errors_and_warnings_tc_0010", test_result, "", "4 eyes form", reg, picture)

    sleep(2)

    # close error message
    type(Key.ENTER)

    sleep(2)

    # 4 eyes required
    type(l_general_test_settings[2])
    type(Key.ENTER)
    type(l_general_test_settings[3])
    type(Key.ENTER)

    sleep(2)

    picture = "4_eyes_validation_required_" + locale + ".png"
    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "errors_and_warnings_tc_0010", test_result, "", "4 eyes form", reg, picture)

    sleep(2)

    # close error message
    type(Key.ENTER)

    sleep(2)

    # invalid password
    type(l_general_test_settings[4])
    type(Key.ENTER)
    type("123456789")
    type(Key.ENTER)

    sleep(2)

    picture = "4_eyes_invalid_password_" + locale + ".png"
    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""
    general_functions.writeTestResults(test_case_description, "GUI", "errors_and_warnings_tc_0010", test_result, "", "4 eyes form", reg, picture)

    sleep(2)

    # close error message
    type(Key.ENTER)

    sleep(2)

    # correct authorization
    type(l_general_test_settings[4])
    type(Key.ENTER)
    type(l_general_test_settings[5])
    type(Key.ENTER)

    sleep(2)


# 0020 does the footwear item not found error appear?

def errors_and_warnings_tc_0020(test_case_description):
    print("l_general_test_settings 1: " + l_general_test_settings[8])

    # "item_not_found_error_en_GB.png"

    print("picture: " + "item_not_found_error_" + locale + ".png")
    picture = "item_not_found_error_" + locale + ".png"

    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""

    general_functions.writeTestResults(test_case_description, "GUI", "home_page_TC_0010_002", test_result, "", "item not found page", reg, picture)


def errors_and_warnings_tc_0030(test_case_description):

    # "does the cancellation warning pop up"

    print("picture: " + "item_not_found_error_" + locale + ".png")
    picture = "item_not_found_error_" + locale + ".png"

    if exists(Pattern(picture).similar(0.85)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.85))
    else:
        test_result = "NOK"
        reg = ""

    general_functions.writeTestResults(test_case_description, "GUI", "does the cancellation warning pop up", test_result, "", "item not found page", reg, picture)


def does_part_of_screen_exist(subject, similarity, test_case_description):

    picture = subject + '_' + locale + ".png"
    the_complete_picture = l_base_dir + 'on till regression test\\test_cases.sikuli\\' + picture

    print('hier: ' + the_complete_picture)

    # is there a localized version  of the picture, if not use the general version
    if os.path.isfile(the_complete_picture):
        print('localized file does exist: ' + picture)
    else:
        picture = subject + '.png'
        print('localized file does NOT exist: ' + picture)

    print("test picture: " + picture)

    if exists(Pattern(picture).similar(similarity)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(similarity))
    else:
        test_result = "NOK"
        reg = ""

    general_functions.writeTestResults(test_case_description, 'GUI', subject, test_result, 'similarity: ' + str(similarity), '', reg, picture)
