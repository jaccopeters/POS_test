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