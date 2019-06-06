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
l_test_settings = test_settings.drop_off()


def drop_off():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('drop off')

    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    time.sleep(6)

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('drop_off')

    for x in range(0, l_general_test_settings[9]):
        time.sleep(0.5)

        number_of_items = l_test_settings

        type(str(number_of_items[x]))
        time.sleep(0.5)
        type(Key.ENTER)
        time.sleep(0.5)
        general_functions.writeTestResults("def drop_off", "GUI", "data", str(x), "", "number of denominations", "", "")
        x += 1

    general_buttons.drop_off_page_click('TAKE OVER')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('drop_off_overview')

    type(Key.ENTER)

    general_functions.close_drawer_msg()

    # general end of test case
    general_functions.end_of_test_case()