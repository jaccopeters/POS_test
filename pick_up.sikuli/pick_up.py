from sikuli import *
import general_functions
import general_buttons
import test_cases
import test_settings

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global brand
brand = l_general_test_settings[6]
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]
global l_test_settings
l_test_settings = test_settings.pick_up(locale)


def pick_up():
    general_functions.errorhandling("ABORT")
    general_functions.start_of_test_case('TC pick up')
    l_general_test_settings = test_settings.general_test_settings()

    general_buttons.main_page_footer_menu_btns_click('OTHER')

    general_buttons.main_page_other_menu_btns_click('PICK UP')

    general_functions.four_eyes(l_general_test_settings[4], l_general_test_settings[5])

    time.sleep(6)
    for x in range(0, l_general_test_settings[9]):
        time.sleep(0.5)

        number_of_items = l_test_settings

        type(str(number_of_items[x]))
        time.sleep(0.5)
        type(Key.ENTER)
        time.sleep(0.5)
        general_functions.writeTestResults("def pick up", "GUI", "data", str(x), "", "number of denominations", "", "")
        x += 1

    general_buttons.pick_up_page_click('TAKE OVER')

    type(Key.ENTER)

    general_functions.close_drawer_msg()