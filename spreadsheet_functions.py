#!/usr/bin/env python

import numpy as np
import openpyxl as pyxl
import string

from tk_functions import *

def setup_columns( _worksheet, ticker_list ):
    _worksheet.cell(row=1, column=1, value='Date')
    for ticker_indx in xrange(0,len(ticker_list)):
        _worksheet.cell(row=1, column=2+ticker_indx, value=ticker_list[ticker_indx])
    return _worksheet


def fill_row( _worksheet, _data, _bid, _ask ):
    # new_row_index = _worksheet.row
    # if( ! _data.search_quote.empty? )
    #     for quote in _data.search_quote.sort_by { |a| [a.xdate, a.strikeprice, a.put_call ] }
    #         if quote.put_call == "call"
    #         then
    #             if ( ( _worksheet[new_row_index, 2] != quote.strikeprice ) )
    #             then
    #                 new_row_index += 1

    #                 _worksheet[new_row_index, 0] = _bid
    #                 _worksheet[new_row_index, 1] = _ask
    #                 _worksheet[new_row_index, 2] = quote.strikeprice
    #                 _worksheet[new_row_index, 3] = quote.xdate
    #                 _worksheet[new_row_index, 4] = quote.days_to_expir
                # Call
                # _worksheet[new_row_index,  6] = quote.bid
                # _worksheet[new_row_index,  7] = quote.ask
                # _worksheet[new_row_index,  8] = quote.contract_size
                # _worksheet[new_row_index,  9] = quote.put_call
                # _worksheet[new_row_index,  10] = quote.symbol
                # _worksheet[new_row_index,  11] = quote.imp_volatility
                # _worksheet[new_row_index,  12] = quote.idelta
                # _worksheet[new_row_index,  13] = quote.igamma
                # _worksheet[new_row_index,  14] = quote.itheta
                # _worksheet[new_row_index,  15] = quote.ivega
                # _worksheet[new_row_index,  16] = quote.irho
                # _worksheet[new_row_index,  17] = quote.openinterest
            # elsif quote.put_call == "put"
            # then
                # if ( ( _worksheet[new_row_index, 2] != quote.strikeprice ) ) # && !_worksheet[new_row_index, 2].to_s.empty?
                # then
                    # new_row_index += 1

                    # _worksheet[new_row_index,  0] = _bid
                    # _worksheet[new_row_index,  1] = _ask
                    # _worksheet[new_row_index,  2] = quote.strikeprice
                    # _worksheet[new_row_index,  3] = quote.xdate
                    # _worksheet[new_row_index,  4] = quote.days_to_expiration

                # Puts
                # _worksheet[new_row_index,  6] = quote.bid
                # _worksheet[new_row_index,  7] = quote.ask
                # _worksheet[new_row_index,  8] = quote.contract_size
                # _worksheet[new_row_index,  9] = quote.put_call
                # _worksheet[new_row_index,  10] = quote.symbol
                # _worksheet[new_row_index,  11] = quote.imp_volatility
                # _worksheet[new_row_index,  12] = quote.idelta
                # _worksheet[new_row_index,  13] = quote.igamma
                # _worksheet[new_row_index,  14] = quote.itheta
                # _worksheet[new_row_index,  15] = quote.ivega
                # _worksheet[new_row_index,  16] = quote.irho
                # _worksheet[new_row_index,  17] = quote.openinterest

                # new_row_index += 1
    return
