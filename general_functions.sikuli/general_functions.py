# general modules
from sikuli import *
from datetime import datetime
import general_buttons
import time
import test_settings
import shutil
import re
import pick_up
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
l_test_settings = test_settings.basic_sale_off_line_card_test_settings()

global tr_file
tr_file = l_general_test_settings[10] + "test_run\\test_results\\test_results.csv"


# START

def start_of_test_run():
    print('remove: ' + l_base_dir + 'test_run')
    shutil.rmtree(l_base_dir + 'test_run')
    src = l_base_dir + 'utils\\test_run'
    dst = l_base_dir + 'test_run'
    shutil.copytree(src, dst)


def start_of_test_case(test_case_description):
    writeTestResults('test case', test_case_description, "", "", "", "", "", "")
    print('test case: ' + test_case_description)


# IDENTITY

def logon(user, password):
    errorhandling("ABORT")

    writeTestResults("def logon", "GUI", "data", user, password, "", "", "")

    if exists("1534753764224.png"):
        click("1534753764224.png")
        type(user)
        writeTestResults("def logon", "GUI", "data", user, "", "user was empty", "", "")

    if exists("1535029693455.png"):
        click("1535029693455.png")
        type(user)
        writeTestResults("def logon", "GUI", "data", user, "", "user was empty", "", "")

    if exists("1534753802655.png"):
        click("1534753802655.png")
        type(password)
        writeTestResults("def logon", "GUI", "data", password, "", "password was empty", "", "")

    if exists("1535029725687.png"):
        click("1535029725687.png")
        type(password)
        writeTestResults("def logon", "GUI", "data", password, "", "password was empty", "", "")

    if exists("OK-6.png"):
        click("OK-6.png")

    sleep(2)


def four_eyes(user, password):
    errorhandling("ABORT")
    writeTestResults("def four_eyes", "GUI", "data", user, password, "", "", "")

    # general_message_with_subject('test', 'four_eyes_screen')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('four_eyes_screen')


    general_buttons.authorization_btns_click('USER')
    type(user)
    writeTestResults("def logon", "GUI", "data", user, "", "user was empty", "", "")

    general_buttons.authorization_btns_click('PASSWORD')
    type(password)
    writeTestResults("def logon", "GUI", "data", password, "", "password was empty", "", "")

    type(Key.ENTER)

	
def cancel_receipt():
        general_buttons.main_page_key_pad_btns_click('CANCEL')
        four_eyes(l_general_test_settings[4], l_general_test_settings[5])
        type(Key.ENTER)
        type(Key.ENTER)
        extended_wait('main_page_key_pad', 30)	


def do_break():
    errorhandling("")
    writeTestResults("def dobreak", "GUI", "", "", "", "", "", "")

    # click the button for the BREAK menu
    general_buttons.click_element('main_page', -470, -280, 'hamburger btn')
    # click the BRWAK button
    general_buttons.click_element('hamburger_menu', 0, -40, 'BREAK btn')


def errorhandling(action):
    max(0, 1)
    # setFindFailedResponse("ABORT")


def writeTestResults(business_process, test_area, test_case, test_result, test_result_value, test_result_description, reg, picture):
    time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S") + "-" + str(datetime.now( ).microsecond)
    file = ""
    path = ""

    if test_result == "NOK":
        screen = Screen( )
        file = test_result + "_" + time_stamp + "_" + test_case
        path = l_base_dir + "test_run\\test_results\\nok\\"
        src = l_base_dir + "on till regression test\\gui_screens.sikuli\\" + picture
        shutil.copy(src, path + file + "_search_object.png")
        reg = Region(screen)
        img = capture(reg)  # img is an image file .png in temp folder now
        shutil.move(img, path + file + "_screen.png")  # the target directory must exist
        test_result_value = "=HYPERLINK(\"" + path + file + "\")"

    if test_result == "OK":
        # screen = Screen()
        file = test_result + "_" + time_stamp + "_" + test_case
        path = l_base_dir + "test_run\\test_results\\ok\\"
        img = capture(reg)  # img is an image file .png in temp folder now
        shutil.move(img, path + file + ".png")  # the target directory must exist
        test_result_value = "=HYPERLINK(\"" + path + file + "\")"
    f = open(tr_file, "a")
    f.write(str(time_stamp) + "," + str(business_process) + "," + str(test_area) + "," + str(test_case) + "," + str(
        test_result) + "," + str(test_result_value) + "," + str(test_result_description) + "," + str(reg) + "," + str(picture) + "\n")
    f.close( )


def fill_basket(article, number_of_articles):
    errorhandling("ABORT")

    extended_wait('main_page_key_pad', 30)

    # click SEARCH ITEM button
    general_buttons.main_page_key_pad_btns_click('ITEM SEARCH')

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('article_search_form')

    # move to next line on search form
    type(Key.ENTER)

    # article number
    type(str(article))

    # click SEARCH button
    general_buttons.article_search_form_btns_click('SEARCH')

    wait(3)

    # add product(s)
    z = 0
    print('number of products: ' + str(number_of_articles))
    while z < number_of_articles - 1:

        general_buttons.click_element('add_or_substract_product', 100, 0, 'PLUS btn')
        z += 1
        print('z: ' + str(z))

    # TEST CASE
    if is_gui_test == 'YES':
        gui_screens.check_gui_element('basket_with_5_products')


def make_test_receipts(article, number_of_articles):

    valid_receipt = False
    while not valid_receipt:
        fill_basket(article, number_of_articles)
        receipt_meta_data_array = get_receipt_meta_data( )
        receipt_number = receipt_meta_data_array[0]
        print('invalid receipt_number: ' + receipt_number)
        valid_receipt = receipt_number.isnumeric( )
        if valid_receipt:
            # show_value__msg('Is this indeed a valid receipt number:', receipt_meta_data_array) #was marked out before in the 4.0 version of 20190306 JP put on yesterday afternoon #marked again as issue is due to basic sales are ran yesterday
            break
        general_buttons.main_page_key_pad_btns_click('CANCEL')
        four_eyes(l_general_test_settings[4], l_general_test_settings[5])
        type(Key.ENTER)
        type(Key.ENTER)
        extended_wait('main_page_key_pad', 30)

    general_buttons.main_page_key_pad_btns_click('TOTAL')

    pay_transaction_with_multiple_tenders([['VISA', 'REST']])
    return receipt_number


def get_receipt_meta_data():
    receipt_meta_data_array = ['', '', '', '', '']

    if brand == 'CK':
        r = Region(65, 96, 388, 40)
        receipt_meta_data = r.text( )
        print('receipt_meta_data: ' + receipt_meta_data)
        # r.highlight(1)
        # get receipt number with E
        receipt_number1 = re.search(r'[E]\d+', receipt_meta_data).group( )
        # strip E
        receipt_number1 = re.search(r'\d+', receipt_number1).group( )
        print('receipt number1: ' + receipt_number1)

    r = Region(91, 90, 30, 40)  # receipt number
    receipt_number2 = sanitize_ocr_result(r.text( ))
    # r.highlight(1)
    print('receipt number2: ' + receipt_number2)

    if brand == 'CK':
        receipt_meta_data_array[0] = max(receipt_number1, receipt_number2)

    if brand == 'TH':
        receipt_meta_data_array[0] = receipt_number2

    r = Region(146, 90, 27, 40)  # number of items in basket
    receipt_meta_data_array[1] = sanitize_ocr_result(r.text( ))
    # r.highlight(1)

    r = Region(206, 90, 38, 40)  # cashier number
    receipt_meta_data_array[2] = sanitize_ocr_result(r.text( ))
    # r.highlight(1)

    r = Region(280, 90, 38, 40)  # till number
    receipt_meta_data_array[3] = sanitize_ocr_result(r.text( ))
    # r.highlight(1)

    r = Region(333, 90, 113, 40)  # date and time
    receipt_meta_data_array[4] = sanitize_ocr_result(r.text( ))
    # r.highlight(1)

    # writeTestResults('receipt data temp', '', '', str(receipt_meta_data_array), '', '', '', '')
    if len(receipt_meta_data_array) >= 5:
        writeTestResults('receipt data', '', '', str(receipt_meta_data_array[0]), str(receipt_meta_data_array[1]), str(receipt_meta_data_array[2]), str(receipt_meta_data_array[3]),
                         str(receipt_meta_data_array[4]))
    else:
        writeTestResults('receipt data', '', 'NO VALID RECEIPT DATA', '', str(receipt_meta_data_array), '', '', '')

    # receipt_meta_data_array[0] = str(receipt_number)

    return receipt_meta_data_array


def sanitize_ocr_result(ocr_result):
    # sanitize data
    # print('ocr_result: ' + ocr_result)
    resulting_text = ocr_result.replace(" ", "")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("d", "0")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("D", "0")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("c", "0")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("C", "0")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("|j", "0")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("LEI!)", "99")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("2C|", "20")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("_r:I|I", "80")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("I5", "15")
    # print('resulting_text: ' + resulting_text)
    resulting_text = resulting_text.replace("OI", "01")
    # print('resulting_text: ' + resulting_text)

    return resulting_text


# PAYMENTS

def pay_transaction_with_multiple_tenders(payment_data_items):

    '''

    payment_data_items example
      DESCRIPTION    VALUE
      1              2
    [['VISA',     '10.00' ],
     ['ZALANDO',  'REST'  ]]
    '''

    # number of tenders to pay with
    offline_cards = ['VISA', 'MASTERCARD', 'MAESTRO', 'AMEX', 'CHINA UNION PAY', 'DINERS', 'ONE4ALLVOUCHER', 'ALIPAY', 'ALIPAY IRELAND', 'WECHAT', 'WECHAT IRELAND', 'BREUNINGER', 'POSTFINANCE', 'BANCOMAT']
    online_cards = ['VISA ON', 'MASTERCARD ON', 'MAESTRO ON', 'AMEX ON', 'CHINA UNION PAY ON', 'DINERS ON', 'ALIPAY ON', 'WECHAT ON']

    receipt_meta_data_array = get_receipt_meta_data( )
    cash_included_in_payment = False

    for payment_item in payment_data_items:

        tender = payment_item[0]

        if tender in offline_cards:
            general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
            wait(0.5)
            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('other_tenders_screen')
            general_buttons.payment_page_other_tenders_menu_btns_click('OFFLINE CARD')
            wait(0.5)
            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('offline_cards_screen')
            general_buttons.payment_page_other_tenders_offline_card_menu_btns_click(tender)
            wait(0.5)
            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('offline_cards_total_amount_screen')

            # amount if mentioned
            if payment_item[1] <> 'REST':
                type(str(payment_item[1]))

            type(Key.ENTER)

            # TEST CASE
            if is_gui_test == 'YES':
                gui_screens.check_gui_element('offline_card_payment_processed_dialog')

            type(Key.ENTER)

            # do_pick_up_if_needed()

        if tender == 'GIFT VOUCHER':
            general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
            wait(0.5)
            general_buttons.payment_page_other_tenders_menu_btns_click(tender)
            wait(0.5)

            # gv number
            if brand == "CK":
                type(payment_item[1])
                general_message_with_subject('Type the GV number', 'If the found GV number was NOT correct please type the correct one here and click OK, if it is correct just click OK')
            if brand == "TH":
                type(payment_item[1])

            type(Key.ENTER)
            # type(Key.ENTER)

        if tender == 'ZALANDO':
            general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
            wait(0.5)
            general_buttons.payment_page_other_tenders_menu_btns_click(tender)
            wait(0.5)
            # zalando number
            type(payment_item[1])
            wait(0.5)
            # confirm number and close sale
            type(Key.ENTER)
            wait(0.5)

        if tender == 'FRANCHISE RETOURE POST':
            general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
            wait(0.5)
            general_buttons.payment_page_other_tenders_menu_btns_click(tender)
            wait(0.5)
            # frp_number
            type(payment_item[2])
            wait(0.5)
            type(Key.ENTER)
            wait(0.5)
            # amount
            type(payment_item[1])
            wait(0.5)
            type(Key.ENTER)
            # pay_transaction_with_tender([['tender', 'DINERS']])

        if tender in online_cards:
            general_buttons.pay_out_key_pad_click('CARD')
            wait(0.5)
            # amount if mentioned
            if payment_item[1] <> 'REST':
                type(str(payment_item[1]))
            type(Key.ENTER)

            general_message('pay manually with online ' + tender + ' card and the Adyen terminal. Click OK once your done paying to resume the automated test run')

        if tender == 'CASH':

            general_buttons.pay_out_key_pad_click('CASH')
            if payment_item[1] <> 'REST':
                type(str(payment_item[1]))
            type(Key.ENTER)
            cash_included_in_payment = True
            print('cash_included_in_payment: ' + str(cash_included_in_payment))

        if tender == 'FOREIGN CURRENCY':
            general_buttons.payment_page_footer_menu_btns_click('OTHER TENDERS')
            wait(0.5)
            general_buttons.payment_page_other_tenders_menu_btns_click(tender)
            wait(0.5)
            general_buttons.pay_out_key_pad_click('CASH')
            type(Key.ENTER)
            cash_included_in_payment = True
            print('cash_included_in_payment: ' + str(cash_included_in_payment))


    # if there is cash involved in the payment the drawer will be opened after the last tender
    if cash_included_in_payment == True:
        close_drawer_msg( )


def get_payment_data(payment_data_items, data_item):
    for payment_data_item in payment_data_items:
        print('payment_data_item: ' + str(payment_data_item))
        if payment_data_item[0] == data_item:
            return payment_data_item[1]



def do_pick_up_if_needed():

            if exists('TH_pickup_required_screen.png', 5):
                type(Key.ENTER)
                pick_up.pick_up()


# FLOW AND TIMING

def extended_wait(element, max_sec_wait):

    picture = element + '_' + locale + '_' + brand + ".png"
    the_complete_picture = l_base_dir + 'on till regression test\\screen_prints\\' + picture

    # print('hier: ' + the_complete_picture)

    # is there a localized version  of the picture, if not use the general version
    if os.path.isfile(the_complete_picture):
        print('local version exists: ' + picture)
    else:
        picture = l_base_dir + 'on till regression test\\screen_prints\\' + element + '_' + brand + ".png"
        # print('local version does NOT exist: ' + picture)

    print("picture we're trying to find: : " + picture)

    wait(picture, max_sec_wait)


# MESSAGES

def general_message(message):
    popup(message)


def general_message_with_subject(message, subject):
    popup(message, subject)


def close_drawer_msg():
    popup("close the drawer and click OK to resume the test", "close the drawer")


def end_of_day_msg():
    popup("close the drawer, perform end of day in GK Portal and click OK to resume the test", "close the drawer")


def check_screen_msg():
    popup("click OK to resume the test", "check screen")


def end_of_test_case_msg():
    popup("test has run without problems, click OK to proceed", "test has run")


def pause_test_case_msg():
    popup("test executions is paused. You can restart by clicking OK", "test execution paused")


def show_value__msg(message, data_value):
    popup(message + ': ' + str(data_value), "test execution paused")


# END

def end_of_test_case():
    clean_up_after_test( )
    writeTestResults(" ", "", "", "", "", "", "", "")

    # save test run directory with time stamp
    time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S")
    # time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S") + "-" + str(datetime.now( ).microsecond) # time stamp with micro seconds
    src = l_base_dir + 'test_run'
    dst = l_base_dir + time_stamp + '_test_run'
    shutil.copytree(src, dst)


def clean_up_after_test():
    # f.close()
    print('test ended correctly')


def end_of_test_run():
    # save test run directory with time stamp
    time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S")
    # time_stamp = "T " + time.strftime("%Y%m%d-%H%M%S") + "-" + str(datetime.now( ).microsecond) # time stamp with micro seconds
    src = l_base_dir + 'test_run'
    dst = l_base_dir + 'total_' + time_stamp + '_test_run'
    shutil.copytree(src, dst)