from sikuli import *


def general_test_settings():
    #                               ENV    STORE   CASHIER PASSW   MANAGERPASSW    BRAND TILL   LOCALE  #DENOMINATIONS BASE DIR                      GUI TEST
    #   l_general_test_settings = ["TST", "A424", "101", "11111", "100", "50055", "CK", "101", "en_GB", 5, "C:\\Users\\31000pos\\Desktop\\Sikuli\\", False, "FP", "TH"]
    l_general_test_settings = ["TST", "AN08", "101", "30033", "100", "30033", "TH", "101", "en_GB", 5, "C:\\Users\\31000Pos\\Desktop\\Sikuli\\", False, "FP", "BE"]
    #   l_general_test_settings = ["TST", "A233", "250", "30033", "251", "30033", "TH", "101", "en_GB", 5, "C:\\Users\\31000Pos\\Desktop\\Sikuli\\", False, "FP", "DE"]
    #l_general_test_settings = ["TST", "AL00", "101", "30033", "100", "50055", "TH", "101", "en_GB", 5, "C:\\Users\\31000Pos\\Desktop\\Sikuli\\", "NO", "FP", "NL"]
    return l_general_test_settings


def get_test_specific_settings():
    l_general_test_settings = general_test_settings( )
    test_specific_settings = []

    # (BE, DE, NL) TH FP
    if l_general_test_settings[13] in ('BE', 'DE', 'NL'):  # country is Belgium, Germany ??
        if l_general_test_settings[6] == 'TH':  # brand is TH
            if l_general_test_settings[12] == 'FP':  # store type is Full Price
                #                          NORMAL ARTICLE      PROMOTION           BONUS BUY          # OF DIVISIONS
                test_specific_settings = ['AM0AM03329901001', 'C827830495422001', 'C827830508480004', 11]

    # (BE, DE, NL) TH FP
    if l_general_test_settings[13] in ('BE', 'DE', 'NL'):  # country is Belgium, Germany ??
        if l_general_test_settings[6] == 'TH':  # brand is TH
            if l_general_test_settings[12] == 'OL':  # store type is Full Price
                #                          NORMAL ARTICLE      PROMOTION           BONUS BUY          # OF DIVISIONS
                test_specific_settings = ['AM0AM03329901001', 'C827830495422001', 'C827830508480004', 11]

    # (BE, DE, NL) TH FP
    if l_general_test_settings[13] in ('BE', 'DE', 'NL'):  # country is Belgium, Germany ??
        if l_general_test_settings[6] == 'CK':  # brand is TH
            if l_general_test_settings[12] == 'FP':  # store type is Full Price
                #                          NORMAL ARTICLE      PROMOTION           BONUS BUY          # OF DIVISIONS
                test_specific_settings = ['AM0AM03329901001', 'C827830495422001', 'C827830508480004', 11]

    # (BE, DE, NL) TH FP
    if l_general_test_settings[13] in ('BE', 'DE', 'NL'):  # country is Belgium, Germany ??
        if l_general_test_settings[6] == 'CK':  # brand is TH
            if l_general_test_settings[12] == 'OL':  # store type is Full Price
                #                          NORMAL ARTICLE      PROMOTION           BONUS BUY          # OF DIVISIONS
                test_specific_settings = ['AM0AM03329901001', 'C827830495422001', 'C827830508480004', 11]

    return test_specific_settings


def gui_test():
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    #                  0                          1   2
    #                  ARTICLE#                   #   TENDERS
    l_test_settings = [test_specific_settings[0], 5, [['WECHAT', 'REST']]]
    return l_test_settings


def item_not_found():
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    # get number of divisions
    l_test_settings = [test_specific_settings[3], [['AMEX', 'REST']]]
    return l_test_settings


def void_line_item_test_settings():
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    #                           0                                          2
    #                           ARTICLE#                        #   TENDERS
    l_test_settings = [test_specific_settings[0], 3, [['AMEX', 'REST']]]

    return l_test_settings


def pre_make_receipts(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    #                    0                  1   2       3     4
    #                    ARTICLE#           #   CARD    COORDINATES
    l_test_settings = [test_specific_settings[0], 10, 'VISA', -200, -70]

    return l_test_settings


def pick_up(locale):
    l_test_settings = ''

    #                  0
    #                  DENOMINATIONS#
    l_test_settings = [6, 3, 2, 1, 1]
    return l_test_settings


def drop_off():
    # drop off settings are the same for all countries, brands and store types
    l_test_settings = ''

    #                  0
    #                  DENOMINATIONS#
    l_test_settings = [6, 3, 2, 1, 1]
    return l_test_settings


def returns():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                  0            1
        #                  ARTICLE#     #
        l_test_settings = [test_specific_settings[0], 3]
    else:
        #                  0            1
        #                  ARTICLE#     #
        l_test_settings = [test_specific_settings[0], 3]

    return l_test_settings


def basic_sale_off_line_card_test_settings():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #     0                         1   2
        #     ARTICLE#                  #   TENDERS
        l_test_settings = [
            [test_specific_settings[0], 5, [['CHINA UNION PAY', 'REST']]]
        ]
    else:
        #     0                         1   2
        #     ARTICLE#                  #   TENDERS
        l_test_settings = [
            #[test_specific_settings[0], 1, [['CASH', '1.00'], ['AMEX', 'REST']]],
            #[test_specific_settings[0], 1, [['VISA', '1.00'], ['MASTERCARD', '2.00'], ['MAESTRO', '3.00'], ['CASH', '4.00'], ['AMEX', 'REST']]],
            #[test_specific_settings[0], 1, [['MASTERCARD ON', 'REST']]],
            #[test_specific_settings[0], 1, [['MAESTRO ON', 'REST']]],
            #[test_specific_settings[0], 1, [['AMEX ON', 'REST']]],
            #[test_specific_settings[0], 1, [['VISA', '1.00'], ['MASTERCARD', '1.00'], ['MAESTRO', '1.00'], ['AMEX', '1.00'], ['CHINA UNION PAY', '1.00'], ['DINERS', '1.00'], ['ALIPAY', '1.00'], ['WECHAT', '1.00'],['CASH', 'REST']]],
            [test_specific_settings[0], 1, [['VISA', 'REST']]],
            [test_specific_settings[0], 2, [['MASTERCARD', 'REST']]],
            [test_specific_settings[0], 3, [['MAESTRO', 'REST']]],
            [test_specific_settings[0], 4, [['AMEX', 'REST']]],
            [test_specific_settings[0], 5, [['CHINA UNION PAY', 'REST']]],
            [test_specific_settings[0], 6, [['DINERS', 'REST']]],
            [test_specific_settings[0], 7, [['ALIPAY', 'REST']]],
            [test_specific_settings[0], 8, [['WECHAT', 'REST']]]
        ]

    if l_general_test_settings[13] == 'IT--':
        l_test_settings.append = [test_specific_settings[0], 9, [['BANCOMAT', 'REST']]]

    if l_general_test_settings[13] == 'DE_':
        l_test_settings = l_test_settings + [test_specific_settings[0], 9, [['BREUNINGER', 'REST']]]
        # l_test_settings.append = [test_specific_settings[0], 1, [['FRANCHISE RETOURE POST', 'REST', '1234567890']]
        # l_test_settings.append = [test_specific_settings[0], 1, [['ZALANDO', '123456789']]

    if l_general_test_settings[13] == 'CH':
        l_test_settings.append = [test_specific_settings[0], 9, [['FOREIGN CURRENCY']]]
        l_test_settings.append = [test_specific_settings[0], 9, [['POST FINANCE', 'REST']]]

    return l_test_settings

def no_sale():
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    #                           0                                          2
    #                           ARTICLE#                        #   TENDERS
    l_test_settings = []

    return l_test_settings

def basic_sale_chf_eur_test_settings(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == "en_GB":
        #                    0                  1
        l_test_settings = [test_specific_settings[0], 6]

    return l_test_settings

def tax_free_test_settings():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

	#     0                         1   2
	#     ARTICLE#                  #   TENDERS
    l_test_settings = [[test_specific_settings[0], 5, [['WECHAT', 'REST']]]]
    return l_test_settings

#tax_free_aftersales_test_settings

def tax_free_aftersales_test_settings():
    l_general_test_settings = general_test_settings( )
    tax_free_aftersales_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                  0            1
        #                  ARTICLE#     #
        tax_free_aftersales_test_settings = [test_specific_settings[0], 3]
    else:
        #                  0            1
        #                  ARTICLE#     #
        tax_free_aftersales_test_settings = [test_specific_settings[0], 3]

    return tax_free_aftersales_test_settings


def cancel_receipt_test_settings():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                    0           1  2
        #                    ARTICLE     #  before(1) or after(0)
        l_test_settings = [[test_specific_settings[0], 3, 1]]
        return l_test_settings
    else:
        #                    0           1  2
        #                    ARTICLE     #  before(1) or after(0)
        l_test_settings = [[test_specific_settings[0], 3, 1],
                           [test_specific_settings[0], 3, 0],
                           [test_specific_settings[0], 3, 0]]
        return l_test_settings


def void_tender_type_test_settings(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == "en_GB":
        #                    0                  1  2           3     4
        #                    ARTICLE            #  CARD        COORDINATES
        l_test_settings = [[test_specific_settings[0], 3, 'VISA', -200, -70],
                           [test_specific_settings[0], 3, 'AMEX', 200, -70],
                           [test_specific_settings[0], 3, 'MAESTRRO', -70, -70]]

        return l_test_settings


def non_merchandise_sale_test_settings():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        if l_general_test_settings[6] == "TH":
            if l_general_test_settings[13] in ('NL'):
                #                    1           2           
                #                    TYPE        PRICE
                l_test_settings = [['NM_ITEM_1', 1.00]]
    else:
        if l_general_test_settings[6] == "TH":
            if l_general_test_settings[13] in ('NL'):
                #                    1           2           
                #                    TYPE        PRICE
                l_test_settings = [['NM_ITEM_1', 1.00],
                                   ['NM_ITEM_2', 2.00],
                                   ['NM_ITEM_3', 3.00],
                                   ['NM_ITEM_4', 4.00],
                                   ['NM_ITEM_5', 5.00]]
    return l_test_settings



def manual_discount():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                         0                  1  2
        #                    ARTICLE            #  DISCOUNT
        l_test_settings = [[test_specific_settings[0], 1, 10]]
        return l_test_settings
    else:
        #0                  1  2
        #                    ARTICLE            #  DISCOUNT
        l_test_settings = [
                           [test_specific_settings[0], 1, 10],
                           [test_specific_settings[0], 1, 11],
                           [test_specific_settings[0], 1, 12],
                           [test_specific_settings[0], 1, 13],
                           [test_specific_settings[0], 1, 14],
                           [test_specific_settings[0], 1, 15],
                           [test_specific_settings[0], 1, 16],
                           [test_specific_settings[0], 1, 17],
                           [test_specific_settings[0], 1, 18],
                           [test_specific_settings[0], 1, 19],
                           [test_specific_settings[0], 1, 20],
                           [test_specific_settings[0], 1, 21]
                           ]
        return l_test_settings


def price_override(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == 'en_GB':
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [test_specific_settings[0], 2]

        return l_test_settings


def local_employee_discount(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == 'en_GB':
        #                    0                 1   2     3  4   5
        #                    ARTICLE           #  empl#  FN LN  %
        l_test_settings = [[test_specific_settings[0], 3, '111111', '', '', '15% 3 percentages'],
                           [test_specific_settings[0], 2, '222222', '', '', '30% 3 percentages'],
                           [test_specific_settings[0], 2, '333333', '', '', '50% 3 percentages'],
                           [test_specific_settings[0], 3, '444444', '', '', '30% 3 percentages'],
                           [test_specific_settings[0], 3, '555555', '', '', '30% 3 percentages'],
                           [test_specific_settings[0], 1, '666666', '', '', '50% 3 percentages'],
                           [test_specific_settings[0], 1, '777777', '', '', '50% 3 percentages']]

        return l_test_settings


def promotions():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [[test_specific_settings[1], 1]]
    else:
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [[test_specific_settings[1], 1],
                           [test_specific_settings[1], 2],
                           [test_specific_settings[1], 3],
                           [test_specific_settings[1], 4],
                           [test_specific_settings[1], 5]]

    return l_test_settings


def bonus_buys():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [[test_specific_settings[2], 1]]
    else:
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [[test_specific_settings[2], 1],
                           [test_specific_settings[2], 2],
                           [test_specific_settings[2], 3]
                           ]

    return l_test_settings


def pay_out():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                  0
        #                  # OF PAY OUT REASONS
        l_test_settings = [1]
    else:
        #                  0
        #                  # OF PAY OUT REASONS
        l_test_settings = [6]

    return l_test_settings


def pay_in():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                  0
        #                  # OF PAY IN REASONS
        l_test_settings = [1]
    else:
        #                  0
        #                  # OF PAY IN REASONS
        l_test_settings = [6]

    return l_test_settings


def check_GUI_elements(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == 'en_GB':
        #                    0                  1
        #                    ARTICLE            #
        l_test_settings = [test_specific_settings[0], 1]

        return l_test_settings


def loyalty_number(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == "en_GB":
        #                    0                         1   2                 3                4                                         5
        #                    ARTICLE#                  #   loyalty number    voucher_number   payment                                   type
        l_test_settings = [[test_specific_settings[0], 3, '17600562303641', '78123456780015', [['VISA', '10,00'], ['MAESTRO', 'REST']], 'BIRTHDAY'],
                           [test_specific_settings[0], 3, '17600562303641', '78123456780010', [['DINERS', 'REST']], 'WELCOME'],
                           # ['test_specific_settings[0]', 3, '17600562266083', '79400000150123', [['AMEX', 'REST']], 'Birthday 15% off'],
                           # ['test_specific_settings[0]', 3, '17600562266083', '78123456780015', [['VISA', '1,00'], ['MAESTRO', '2,00'], ['DINERS', 'REST']], 'Birthday voucher'],
                           # ['test_specific_settings[0]', 3, '17600562266083', '78123456780010', [['ALIPAY IRELAND', 'REST']], 'Welcome voucher'],
                           # ['test_specific_settings[0]', 3, '17600562266083', '79400000100128', [['WECHAT IRELAND', 'REST']], 'Welcome voucher MyTommy'],
                           # ['test_specific_settings[0]', 3, '17600562266083', '79200015000105', [['CHINA UNION PAY', 'REST']], 'Winback voucher']
                           ]

        return l_test_settings


def gift_receipt():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                  0
        #                  # OF PAY IN REASONS
        l_test_settings = [test_specific_settings[0], 4]
    else:
        #                  0
        #                  # OF PAY IN REASONS
        l_test_settings = [test_specific_settings[0], 4]


    return l_test_settings


def commission_sale():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                   0                  1
        #                   ARTICLE            #
        l_test_settings = [test_specific_settings[0], 3]
    else:
        #                   0                  1
        #                   ARTICLE            #
        l_test_settings = [test_specific_settings[0], 3]

    return l_test_settings


def remove_promotion(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == 'en_GB':
        #                   0                  1
        #                   ARTICLE            #
        l_test_settings = [test_specific_settings[1], 1]

    return l_test_settings


def gv_sale_and_redemption():
    l_general_test_settings = general_test_settings( )
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )

    if l_general_test_settings[11] == "YES":
        #                    0       1
        #                   PRICE    #
        l_test_settings = ['100.00', 1, test_specific_settings[0], 1]
    else:
        #                    0       1
        #                   PRICE    #
        l_test_settings = ['100.00', 1, test_specific_settings[0], 1]

    return l_test_settings



def custom(locale):
    l_test_settings = ''
    test_specific_settings = get_test_specific_settings( )
    if locale == 'en_GB':
        #                   0                  1
        #                   ARTICLE            #
        l_test_settings = [['DIV 1', '12345', '50,00 ', [['VISA', 'REST']]],
                           ['DIV 2', '8719112815373', '51,00 ', [['AMEX', 'REST']]]]

    return l_test_settings