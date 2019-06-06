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
l_test_settings = test_settings.returns(locale)

def EOD():

    general_buttons.click_element_in_region('main_page_footer_menu', 70, 0, 'OTHER btn', general_functions.get_footer_menu_area(), 0.7)
    general_buttons.click_element_in_region('main_page_other_menu_btns', 200, -70, 'END OF DAY btn', general_functions.get_menu_buttons_area(), 0.7)
    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    general_functions.close_drawer_msg()
