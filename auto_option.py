#!/usr/bin/env python

import sys
import oauth2 as oauth
import time
import os
import os.path

from tk_functions import *
from spreadsheet_functions import *


stock_list = [ 'SPY',
                'BP',
                'DE',
                'M',
                'MSFT',
                'PG',
                'CRM', ]
num_samples = 90
file_name = 'history.xlsx'
high_rank = 85
low_rank = 15

def get_IV(tk_hook, cur_stock, strike_width):
    tk_hook.get_quote(cur_stock)
    # print(tk_hook.quote.cl)

    tk_hook.get_search(cur_stock,
                        datetime.date.today()+datetime.timedelta(days=30),
                        float(tk_hook.quote.cl)-strike_width,
                        tk_hook.quote.cl)

    itm_iv_avg = 0
    for quote in tk_hook.search.search_quote:
        itm_iv_avg += float(quote.imp_volatility)
        # print(quote.put_call, quote.strikeprice, quote.imp_volatility, quote.symbol)

    itm_iv_avg = itm_iv_avg / len(tk_hook.search.search_quote)
    # print( itm_iv_avg )
    return itm_iv_avg

def update_IV_History(tk_hook, trade_sheet):
    last_row = trade_sheet.max_row + 1
    if trade_sheet.cell(row=last_row-1, column=1).value.date() == datetime.date.today():
        print("already updated")
        return

    trade_sheet.cell(row=last_row,column=1).value = datetime.date.today()

    i = 2
    while trade_sheet.cell(row=1,column=i).value != None:
        # start_time=time.time()
        cur_stock = trade_sheet.cell(row=1,column=i).value
        strike_width = trade_sheet.cell(row=2, column=i).value

        # print(cur_stock)
        # print(strike_width)

        trade_sheet.cell(row=last_row, column=i).value = get_IV(tk_hook, cur_stock, strike_width)

        i += 1
        # print(str((time.time()-start_time)*1000) + " ms")
        # print("")
        # time.sleep(2)
    return

def get_IV_Percentile(tk_hook, trade_sheet, column_cnt):
    iv_list = []
    cur_stock = trade_sheet.cell(row=1,column=column_cnt).value
    strike_width = trade_sheet.cell(row=2, column=column_cnt).value

    cur_stock_iv = get_IV(tk_hook, cur_stock, strike_width)
    cnt = 0
    row_cnt = trade_sheet.max_row
    while cnt < 90 and row_cnt > 2:
        iv_list.append(trade_sheet.cell(row=row_cnt, column=column_cnt).value)
        row_cnt -= 1
        cnt += 1

    iv_list.sort()
    for cnt in xrange(0,len(iv_list)):
        if iv_list[cnt] < cur_stock_iv:
            next
        else:
            iv_percentile = float(cnt) / len(iv_list) * 100
            break

    return iv_percentile

def main(argv):
    tk_func = TK_functions()

    # initialize workbook
    if os.path.isfile(file_name):
        trade_workbook = pyxl.load_workbook(file_name)
        trade_sheet = trade_workbook.active
    else:
        trade_workbook = pyxl.Workbook()
        trade_sheet = trade_workbook.active
        trade_sheet.title = "Trade List"
        setup_columns(trade_sheet, stock_list)
        trade_workbook.save(file_name)

    tk_func.refresh_account_data()
    trade_size = float(tk_func.account.accountval) / 100
    print(trade_size)
    print("")

    update_IV_History(tk_func, trade_sheet)
    trade_workbook.save(file_name)

    i = 2
    while trade_sheet.cell(row=1,column=i).value != None:
        start_time=time.time()
        iv_percentile = get_IV_Percentile(tk_func, trade_sheet, i)

        if iv_percentile > high_rank:
            print(trade_sheet.cell(row=1,column=i).value + " has very high volitility")
            # check_credit_spread()
            # check_butterfly()
            # check_iron_condor()

        if iv_percentile < low_rank:
            print(trade_sheet.cell(row=1,column=i).value + " has very low volitility")
            # check_calendar()
            # check_ratio_spread()
            # check_debit_spread()


        print( iv_percentile)

        i += 1
        # print(str((time.time()-start_time)*1000) + " ms")
        print("")
        time.sleep(2)

if __name__ == '__main__':
    main(sys.argv)

