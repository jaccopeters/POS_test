from sikuli import *
import general_functions
import general_buttons
import test_settings
import test_cases
import time

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
l_test_settings = test_settings.gui_test()


def check_gui_element(element):

    general_functions.start_of_test_case('GUI test ' + country + ' ' + brand + ' ' + element)

    picture = country + '_' + brand + '_' + element + '.png'

    if exists(Pattern(picture).similar(0.70)):
        test_result = "OK"
        reg = find(Pattern(picture).similar(0.70))
    else:
        test_result = "NOK"
        reg = ""

    print("test result for function: " + test_result)
    general_functions.writeTestResults('test result', "GUI", element, test_result, "", "", reg, picture)