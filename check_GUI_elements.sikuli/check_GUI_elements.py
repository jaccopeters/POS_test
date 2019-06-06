from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings
import time
import string
import returns_with_receipt

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.check_GUI_elements(locale)


def screens():
    general_functions.logon(l_general_test_settings[2], l_general_test_settings[3])
    # main page
    print('main sreen')
    test_cases.does_part_of_screen_exist('main_screen_complete', 0.7, 'does the main page have all the elements?')
    print('mag glass')

    general_buttons.click_element_in_region('magnifying_glass', 0, 0, 'MAGN GLASS btn', Region(450, 70, 192, 252), 0.7)

    # search page
    test_cases.does_part_of_screen_exist('search_page', 0.1, 'does the search page have all the elements?')

    general_buttons.click_element_in_region('article_search_form', 340, -65, 'CANCEL btn', Region(0, 0, 1023, 386), 0.7)

    general_functions.fill_basket(l_test_settings[0], l_test_settings[1])

    # basket page
    test_cases.does_part_of_screen_exist('basket_page_01', 0.7, 'does the basket page have all the elements?')
