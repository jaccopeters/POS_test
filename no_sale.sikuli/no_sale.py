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
l_test_settings = test_settings.no_sale()

def no_sale():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('no sale')

    wait(1)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('main_page')

    general_buttons.main_page_footer_menu_btns_click('OTHER')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('other_screen')

    general_buttons.main_page_other_menu_btns_click('NO SALE')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('open_drawer_select_reason')



    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])
    type(Key.ENTER)

    wait(2)

    general_functions.close_drawer_msg()     

    general_functions.end_of_test_case()