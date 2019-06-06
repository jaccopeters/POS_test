from sikuli import *
import general_functions
from datetime import datetime
import time
import test_settings
import shutil

global l_general_test_settings
l_general_test_settings = test_settings.general_test_settings( )
global locale
locale = l_general_test_settings[8]
global l_base_dir
l_base_dir = l_general_test_settings[10]


# def OK_button():
#     if exists("OK.png"):
#         click("OK.png")
#         general_functions.writeTestResults("def OK_button", "data", "", "", "OK btn", "", "", "")


# def main_page_num_key_board(button, x, y):
#     picture = "main_page_num_key_board" + locale + ".png"
#     click(Pattern(picture).targetOffset(x, y))
#     general_functions.writeTestResults("def pay_out_page_amounts", "data", "", "", button, "", "", "")


def click_element(element, x, y, button):
    picture = element + '_' + locale + ".png"
    the_complete_picture = l_base_dir + 'on till regression test\\general_buttons.sikuli\\' + picture

    # is there a localized version  of the picture, if not use the general version
    if os.path.isfile(the_complete_picture):
        print('local version exists: ' + picture)
    else:
        picture = element + '.png'
        print('local version does NOT exist: ' + picture)

    print("picture we're trying to find: " + picture)

    wait(picture, 30)

    click(Pattern(picture).targetOffset(x, y).similar(0.70))
    ''' 
    else:
        similarity = 0.85
        while not (exists(Pattern(picture).targetOffset(x, y).similar(similarity))):
            similarity = similarity - 0.01
            # print("similarity: " + str(similarity))
        click(Pattern(picture).targetOffset(x, y).similar(similarity))
    '''
    general_functions.writeTestResults("def " + element, "data", "x-coordinate: " + str(x),
                                       "y-coordinate: " + str(y), button, "", "", "")


def click_element_in_region(element, x, y, button, search_area, similarity):
    picture = element + '_' + locale + ".png"
    the_complete_picture = l_base_dir + 'on till regression test\\general_buttons.sikuli\\' + picture

    print('element to click: ' + the_complete_picture)

    # is there a localized version  of the picture, if not use the general version
    if os.path.isfile(the_complete_picture):
        print('local version exists: ' + picture)
    else:
        picture = element + '.png'
        print('local version does NOT exist: ' + picture)

    # print("picture we're trying to find: " + picture)

    #search_area.highlight(3)

    search_area.wait(Pattern(picture).targetOffset(x, y).similar(similarity), 30)

    search_area.click(Pattern(picture).targetOffset(x, y).similar(similarity))

    general_functions.writeTestResults("def " + element, "data", "x-coordinate " + str(x),
                                       "y-coordinate " + str(y), button, 'similarity ' + str(similarity), "", "")


# MAIN PAGE BUTTONS

def perform_click(btns, button_name):
    for btn in btns:
        if btn[0] == button_name:

            # save picture of button
            time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S") + "-" + str(datetime.now( ).microsecond)
            file = time_stamp + "_" + button_name
            path = l_base_dir + "test_run\\test_results\\buttons\\"

            print('region: ' + btn[0] + ' ' + str(btn[1]-50) + ', ' + str(btn[2]-50) + ', ' + str(btn[1]-50 + 100)+ ', ' + str(btn[2]-50 + 100))

            r = Region(btn[1]-100, btn[2]-50, 200, 100)

            img = capture(r)  # img is an image file .png in temp folder now
            shutil.move(img, path + file + ".png")  # the target directory must exist

            # click button
            click(Location(btn[1], btn[2]))
            # write click to log
            general_functions.writeTestResults("click button", button_name, "x-coordinate: " + str(btn[1]), "y-coordinate: " + str(btn[2]), "", "", "", "")

            break


def return_reasons_click(button_name):

    btns = [['return reason 1',     430,     150],
            ['return reason 2',     430,     190],
            ['return reason 3',     430,     240],
            ['return reason 4',     430,     290],
            ['return reason 5',     430,     340],
            ['return reason 6',	    430,     390],
            ['return reason 7',     430,	 430],
            ['return reason 8',     430,     480],
            ['return reason 9',     430,     520],
            ['return reason 10',    430,     570]]

    perform_click(btns, button_name)


def main_page_key_pad_btns_click(button_name):

    btns = [['7',              515,     190],
            ['8',              605,     190],
            ['9',              695,     190],
            ['SALES PERSON',   805,     190],
            ['CANCEL',         940,     190],
            ['4',	           515,     280],
            ['5',              605,	    280],
            ['6',              695,     280],
            ['PRICE OVERRIDE', 805,     280],
            ['ITEM SEARCH',    940,     280],
            ['1',              515,     370],
            ['2',	           605,	    370],
            ['3',              695,     370],
            ['0',              515,     460],
            ['00',             605,     460],
            ['POINT',          695,     460],
            ['TOTAL',          875,     425]]

    perform_click(btns, button_name)


def pay_out_key_pad_click(button_name):

    btns = [['7',              515,     190],
            ['8',              605,     190],
            ['9',              695,     190],
            ['SALES PERSON',   805,     190],
            ['CANCEL',         940,     190],
            ['4',	           515,     280],
            ['5',              605,	    280],
            ['6',              695,     280],
            ['CASH',           875,     280],
            ['1',              515,     370],
            ['2',	           605,	    370],
            ['3',              695,     370],
            ['0',              515,     460],
            ['00',             605,     460],
            ['POINT',          695,     460],
            ['CARD',           875,     425]]

    perform_click(btns, button_name)


def main_page_items_gv_menu_btns_click(button_name):
    btns = [['ITEM INFO',               550,     550],
            ['RETURNS WITH RECEIPT',    675,     550],
            ['RETURNS NO RECEIPT',      825,     550],
            ['ITEM NOT FOUND',          950,     550],
            ['GIFT VOUCHER SALE',       550,     615],
            ['GIFT VOUCHER STATUS',     675,     615],
            ['NON MERCHANDISE SALE',    825,	 615],
            ['NOT IN USE',              950,     615],
            ['NOT IN USE',              550,     680],
            ['NOT IN USE',              675,     680],
            ['NOT IN USE',              825,     680],
            ['NOT IN USE',              950,     680]]

    perform_click(btns, button_name)


def main_page_items_gv_menu_returns_with_receipt_btns_click(button_name):

    btns = [['7',                   515,     190],
            ['8',                   605,     190],
            ['9',                   695,     190],
            ['ITEM SEARCH',         805,     190],
            ['NOT IN USE',          940,     190],
            ['4',	                515,     280],
            ['5',                   605,	 280],
            ['6',                   695,     280],
            ['RETURN SELECTION',    805,     280],
            ['RETURN ALL ITEMS',    940,     280],
            ['1',                   515,     370],
            ['2',	                605,	 370],
            ['3',                   695,     370],
            ['0',                   515,     460],
            ['00',                  605,     460],
            ['POINT',               695,     460],
            ['TOTAL',               880,     410]]

    perform_click(btns, button_name)


def main_page_items_gv_menu_item_not_found_btns_click(button_name):
    btns = [['DIV 1',    550,     550],
            ['DIV 2',    675,     550],
            ['DIV 3',    825,     550],
            ['DIV 4',    950,     550],
            ['DIV 5',    550,     615],
            ['DIV 6',    675,     615],
            ['DIV 7',    825,	  615],
            ['DIV 8',    950,     615],
            ['DIV 9',    550,     680],
            ['DIV 10',   675,     680],
            ['DIV 11',   825,     680],
            ['DIV 12',   950,     680]]

    perform_click(btns, button_name)


def main_page_items_gv_menu_returns_no_receipt_btns_click(button_name):
    btns = [['ITEM NOT FOUND',  550,     550],
            ['NOT IN USE',      675,     550],
            ['NOT IN USE',      825,     550],
            ['NOT IN USE',      950,     550],
            ['NOT IN USE',      550,     615],
            ['NOT IN USE',      675,     615],
            ['NOT IN USE',      825,	 615],
            ['NOT IN USE',      950,     615],
            ['NOT IN USE',      550,     680],
            ['NOT IN USE',      675,     680],
            ['NOT IN USE',      825,     680],
            ['NOT IN USE',      950,     680]]

    perform_click(btns, button_name)


def returns_page_key_pad_btns_click(button_name):

    btns = [['7',              515,    190],
            ['8',              605,     190],
            ['9',              695,     190],
            ['SALES PERSON',   805,     190],
            ['CANCEL',         940,     190],
            ['4',	           515,     280],
            ['5',              605,	    280],
            ['6',              695,     280],
            ['PRICE OVERRIDE', 805,     280],
            ['ITEM SEARCH',    940,     280],
            ['1',              515,     370],
            ['2',	           605,	    370],
            ['3',              695,     370],
            ['0',              515,     460],
            ['00',             605,     460],
            ['POINT',          695,     460],
            ['END RETURNS',    875,     425]]

    perform_click(btns, button_name)


def item_editing_key_pad_btns_click(button_name):

    btns = [['7',              515,    190],
            ['8',              605,     190],
            ['9',              695,     190],
            ['SALES PERSON',   805,     190],
            ['CANCEL',         940,     190],
            ['4',	           515,     280],
            ['5',              605,	    280],
            ['6',              695,     280],
            ['PRICE OVERRIDE', 805,     280],
            ['ITEM SEARCH',    940,     280],
            ['1',              515,     370],
            ['2',	           605,	    370],
            ['3',              695,     370],
            ['0',              515,     460],
            ['00',             605,     460],
            ['POINT',          695,     460],
            ['END EDITING',    875,     425]]

    perform_click(btns, button_name)


def main_page_items_gv_menu_non_merchandise_sale_btns_click(button_name):
    btns = [['NM_ITEM_1',    	550,    550],
            ['NM_ITEM_2',       675,    550],
            ['NM_ITEM_3',       825,    550],
            ['NM_ITEM_4',       950,    550],
            ['NM_ITEM_5',       550,    615],
            ['NOT IN USE',      675,    615],
            ['NOT IN USE',      825,    615],
            ['NOT IN USE',      950,    615],
            ['NOT IN USE',      550,    680],
            ['NOT IN USE',      675,    680],
            ['NOT IN USE',      825,    680],
            ['NOT IN USE',      950,    680]]

    perform_click(btns, button_name)


def main_page_other_menu_btns_click(button_name):
    btns = [['REPRINT RECEIPT',     550,     550],
            ['PRINT GIFT RECEIPT',  675,     550],
            ['NO SALE',             825,     550],
            ['END OF DAY',          950,     550],
            ['DROP OFF',            550,     615],
            ['PICK UP',	            675,     615],
            ['DRAWER CHECK',        825,	 615],
            ['NOT IN USE',          950,     615],
            ['PAY-IN',              550,     680],
            ['PAY-OUT',             675,     680],
            ['NOT IN USE',          825,     680],
            ['NOT IN USE',          950,     680]]

    perform_click(btns, button_name)


def main_page_customer_menu_btns_click(button_name):
    btns = [['ENTER LOYALTY NUMBER',    550,     550],
            ['LOYALTY NUMBER SEARCH',   675,     550],
            ['ENTER VOUCHER NUMBER',    825,     550],
            ['REMOVE LOYALTY',          950,     550],
            ['NOT IN USE',              550,     615],
            ['NOT IN USE',	            675,     615],
            ['NOT IN USE',              825,	 615],
            ['NOT IN USE',              950,     615],
            ['NOT IN USE',              550,     680],
            ['NOT IN USE',              675,     680],
            ['NOT IN USE',              825,     680],
            ['NOT IN USE',              950,     680]]

    perform_click(btns, button_name)


def main_page_customer_menu_btns_click_taxfree(button_name):
    btns = [['ISSUE TAX FREE',          550,     550],
            ['VOID TAX FREE',           675,     550],
            ['REPRINT TAX FREE',        825,     550],
            ['NOT IN USE',              950,     550],
            ['ENTER LOYALTY NUMBER',    550,     615],
            ['LOYALTY NUMBER SEARCH',	675,     615],
            ['ENTER VOUCHER NUMBER',    825,	 615],
            ['NOT IN USE', 		        950,     615],
            ['NOT IN USE',              550,     680],
            ['NOT IN USE',              675,     680],
            ['NOT IN USE',              825,     680],
            ['NOT IN USE',              950,     680]]

    perform_click(btns, button_name)


def main_page_footer_menu_btns_click(button_name):

    btns = [['ITEMS GV',        550,     725],
            ['DISCOUNTS',       675,     725],
            ['OTHER',           825,     725],
            ['CUSTOMER',        950,     725]]

    perform_click(btns, button_name)


def article_search_form_btns_click(button_name):

    btns = [['ITEM DESCRIPTION',    150,     100],
            ['STYLE CODE',          150,     225],
            ['SIZE',                150,     125],
            ['CANCEL',              850,     95],
            ['SEARCH',              850,     215]]

    perform_click(btns, button_name)


def sales_person_search_form_btns_click(button_name):

    btns = [['VORNAME',             150,     100],
            ['CANCEL',              850,     95],
            ['OK',                  850,     215]]

    perform_click(btns, button_name)


# payment page


def basket_page_footer_menu_btns_click(button_name):

    btns = [['ITEMS / GIFT CARD',   550,     725],
            ['DISCOUNTS',           675,     725],
            ['OTHER',               825,     725],
            ['NOT IN USE',          950,     725]]

    perform_click(btns, button_name)


def basket_page_discounts_menu_btns_click(button_name):

    btns = [['ITEM DISCOUNT %',                 550,    550],
            ['ITEM DISCOUNT TENDER',            675,    550],
            ['TRANSACTION DISCOUNT %',          825,    550],
            ['TRANSACTION DISCOUNT TENDER',     950,    550],
            ['ADD EMPLOYEE',                    550,    615],
            ['NOT IN USE',	                    675,    615],
            ['NOT IN USE',                      825,	615],
            ['NOT IN USE',                      950,    615],
            ['NOT IN USE',                      550,    680],
            ['NOT IN USE',                      675,    680],
            ['REMOVE ITEM DISCOUNT',            825,    680],
            ['REMOVE TRANSACTION DISCOUNT',     950,    680]]

    perform_click(btns, button_name)


def basket_page_edit_line_item_click(button_name):

    btns = [['ITEM DISCOUNT %',                 550,    550],
            ['ITEM DISCOUNT TENDER',            675,    550],
            ['REMOVE ITEM DISCOUNT',            825,    550],
            ['REMOVE PROMOTION',                950,    550],
            ['ADD EMPLOYEE',                    550,    615],
            ['NOT IN USE',	                    675,    615],
            ['NOT IN USE',                      825,	615],
            ['NOT IN USE',                      950,    615],
            ['NOT IN USE',                      550,    680],
            ['NOT IN USE',                      675,    680],
            ['NOT IN USE',                      825,    680],
            ['NOT IN USE',                      950,    680]]

    perform_click(btns, button_name)


def basket_page_employee_discounts_menu_btns_click(button_name):

    btns = [['NOT IN USE',                      550,    550],
            ['NOT IN USE',                      675,    550],
            ['NOT IN USE',                      825,    550],
            ['NOT IN USE',                      950,    550],
            ['NOT IN USE',                      550,    615],
            ['EMPLOYEE ITEM DISCOUNT',	        675,    615],
            ['EMPLOYEE TRANSACTION DISCOUNT',   825,	615],
            ['REMOVE EMPLOYEE',                 950,    615],
            ['NOT IN USE',                      550,    680],
            ['NOT IN USE',                      675,    680],
            ['REMOVE ITEM DISCOUNT',            825,    680],
            ['REMOVE TRANSACTION DISCOUNT',     950,    680]]

    perform_click(btns, button_name)


def basket_page_employee_percentage_discounts_menu_btns_click(button_name):

    btns = [['30%',             	550,     550],
            ['15% 3 percentages',   675,     550],
			['50%',             	675,     550],
			['30% 3 percentages',   675,     550],
			['50% 3 percentages',   825,     550],
            ['NOT IN USE',      	950,     550],
            ['NOT IN USE',      	550,     615],
            ['NOT IN USE',	    	675,     615],
            ['NOT IN USE',      	825,	 615],
            ['NOT IN USE',      	950,     615],
            ['NOT IN USE',      	550,     680],
            ['NOT IN USE',      	675,     680],
            ['NOT IN USE',      	825,     680],
            ['NOT IN USE',      	950,     680]]

    perform_click(btns, button_name)


def payment_page_footer_menu_btns_click(button_name):

    btns = [['CASH',                550,     725],
            ['OTHER TENDERS',       675,     725],
            ['OTHER',               825,     725],
            ['NOT IN USE',          950,     725]]

    perform_click(btns, button_name)


def payment_page_other_tenders_menu_btns_click(button_name):

    btns = [['GIFT VOUCHER',                550,    550],
            ['GIFT VOUCHER STATUS',         675,    550],
            ['FRANCHISE RETOURE POST',      825,    550],
            ['NOT IN USE',                  950,    550],
            ['ZALANDO',                     550,    615],
            ['OFFLINE CARD',	            675,    615],
            ['NOT IN USE',                  825,	615],
            ['NOT IN USE',                  950,    615],
            ['NOT IN USE',                  550,    680],
            ['NOT IN USE',                  675,    680],
            ['NOT IN USE',                  825,    680],
            ['NOT IN USE',                  950,    680]]

    perform_click(btns, button_name)


def payment_page_other_tenders_offline_card_menu_btns_click(button_name):
    btns = [['VISA',                        550,    550],
            ['MASTERCARD',                  675,    550],
            ['MAESTRO',                     825,    550],
            ['AMEX',                        950,    550],
            ['CHINA UNION PAY',             550,    615],
            ['DINERS',	                    675,    615],
            # All countries
            ['ALIPAY',                      825,	615],
            # Ireland
            ['ONE4ALLVOUCHER',              825,	615],
            # All countries
            ['WECHAT',                      950,    615],
            # Ireland
            # ['ALIPAY IRELAND',              950,    615],
            # Germany
            ['BREUNINGER',                  550,    680],
            # Switzerland
            ['POSTFINANCE',                 550,    680],            
            # Ireland
            ['WECHAT IRELAND',              550,    680],
            # Italy
            ['BANCOMAT',                    550,    680],
            ['NOT IN USE',                  675,    680],
            ['NOT IN USE',                  825,    680],
            ['NOT IN USE',                  950,    680]]

    perform_click(btns, button_name)


def payment_page_other_menu_btns_click(button_name):
    btns = [['NOT IN USE',              550,    550],
            ['ISSUE TAX FREE',              550,    550],
            ['BE ISSUE TAX FREE',           675,    550],
            ['NOT IN USE',                  825,    550],
            ['NOT IN USE',                  950,    550],
            ['NOT IN USE',                  550,    615],
            ['NOT IN USE',	                675,    615],
            ['NOT IN USE',                  825,	615],
            ['NOT IN USE',                  950,    615],
            ['NOT IN USE',                  550,    680],
            ['NOT IN USE',                  675,    680],
            ['NOT IN USE',                  825,    680],
            ['NOT IN USE',                  950,    680]]

    perform_click(btns, button_name)


def authorization_btns_click(button_name):
    btns = [['USER',                        850,    160],
            ['PASSWORD',                    850,    225],
            ['CANCEL',                      780,    650],
            ['OK',                          910,    650]]

    perform_click(btns, button_name)


def drop_off_page_click(button_name):
    btns = [['TAKE OVER', 910,    720]]

    perform_click(btns, button_name)


def pick_up_page_click(button_name):
    btns = [['TAKE OVER', 910,    720]]

    perform_click(btns, button_name)


# dit moet de remove promotions worden

def basket_page_key_pad_btns_click(button_name):

    btns = [['7',              515,    190],
            ['8',              605,     190],
            ['9',              695,     190],
            ['SALES PERSON',   805,     190],
            ['CANCEL',         940,     190],
            ['4',	           515,     280],
            ['5',              605,	    280],
            ['6',              695,     280],
            ['PRICE OVERRIDE', 805,     280],
            ['ITEM SEARCH',    940,     280],
            ['1',              515,     370],
            ['2',	           605,	    370],
            ['3',              695,     370],
            ['0',              515,     460],
            ['00',             605,     460],
            ['POINT',          695,     460],
            ['TOTAL',          875,     425]]

    perform_click(btns, button_name)


def gift_receipt_key_pad_btns_click(button_name):

    btns = [['7',               515,    190],
            ['8',               605,    190],
            ['9',               695,    190],
            ['4',	            515,    280],
            ['5',               605,	280],
            ['6',               695,    280],
            ['1',               515,    370],
            ['2',	            605,	370],
            ['3',               695,    370],
            ['SELECT ALL',      805,    370],
            ['PRINT',           940,    370],
            ['0',               515,    460],
            ['00',              605,    460],
            ['CANCEL',          875,    460]]

    perform_click(btns, button_name)


def cancel_reason(button_name):

    btns = [['Cancel reason 1', 300,    150],
            ['Cancel reason 2', 300,    195],
            ['Cancel reason 3', 300,    240]]

    perform_click(btns, button_name)


def hamburger_click(button_name):

    btns = [['HAMBURGER', 25,    25]]

    perform_click(btns, button_name)	


def hamburger_basket_menu_btns_click(button_name):

    btns = [['SUSPEND',         220, 180],
            ['SHOW DESKTOP',    520, 180]]


    perform_click(btns, button_name)


def click_in_list(button_name):
    btns =  [[   'LIST ITEM 1'	,	300	,	150	],
            [	'LIST ITEM 2'	,	300	,	196	],
            [	'LIST ITEM 3'	,	300	,	242	],
            [	'LIST ITEM 4'	,	300	,	288	],
            [	'LIST ITEM 5'	,	300	,	334	],
            [	'LIST ITEM 6'	,	300	,	380	],
            [	'LIST ITEM 7'	,	300	,	426	],
            [	'LIST ITEM 8'	,	300	,	472	],
            [	'LIST ITEM 9'	,	300	,	518	],
            [   'LIST ITEM 10'  ,   300 ,   570 ]
             ]

    perform_click(btns, button_name)