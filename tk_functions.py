#!/usr/bin/env python

import sys
import os.path
import oauth2 as oauth
import datetime

from tk_data_classes import *

class TK_functions:

    # Your key/secrets for authentication
    CONSUMER_KEY        = '5PC6akh4z5QNFOOR33PtCMocUEpeBZ3eN3j4eN3QQOU3'
    CONSUMER_SECRET     = 'g8kphN1GwJwkk2wynq4KGHzAlyppV8Q3PH0P7IQVFcI2'
    ACCESS_TOKEN        = 'tzSCap7Eh7Jr0PsFxQslZ6HJY1dao6QIDq6e1UIpehQ7'
    ACCESS_TOKEN_SECRET = 'Bdqs6xAFayEUbyvoAehjMJ690PuSFJ98x1ajs4IPGZI4'

    SITE                = 'https://api.tradeking.com/v1'
    MY_ACCOUNT          = '/accounts/'
    GET_QUOTE           = '/market/ext/quotes'
    GET_SEARCH          = '/market/options/search'
    GET_CLOCK           = '/market/clock'

    DATE_GREATER_THAN_QUERY = '&query=xdate=gt%3A'
    DATE_LESS_THAN_EQUAL_TO_QUERY = '&query=xdate=lte%3A'
    AND_STD_SIZE        = '%20AND%20contract_size-eq%3100'
    AND_GTE_STRIKE       = '%20AND%20strikeprice-gte%3A'
    AND_LT_STRIKE       = '%20AND%20strikeprice-lt%3A'

    RETURN_TYPE_XML     = '.xml'
    RETURN_TYPE_JSON    = '.json'

    commision_flat_rate = 4.95
    commision_per_contract = 0.65
    required_success_percentage = 0.65

    def __init__(self, accountNum=38840110):
        self.accountNum = accountNum
        self.account = Account()
        self.quote = Quote()
        self.search = Search()

        self.oauth_consumer = oauth.Consumer( key = self.CONSUMER_KEY, secret = self.CONSUMER_SECRET )
        self.oauth_token = oauth.Token( key = self.ACCESS_TOKEN, secret = self.ACCESS_TOKEN_SECRET )
        self.oauth_client = oauth.Client( self.oauth_consumer, self.oauth_token )


    def refresh_account_data(self, test_account_file=None):
        if(test_account_file==None):
            response, data = self.oauth_client.request( self.SITE
                                                        + self.MY_ACCOUNT
                                                        + str(self.accountNum)
                                                        + self.RETURN_TYPE_JSON )

            self.account.parse(data)
            # print self.account.to_s()
        else:
            print("test account data")
            if(os.path.isfile(test_account_file)):
                file = open(test_account_file,'r')
                for line in file:
                    split_val = line.split()
                    self.account.value(split_val[0],split_val[2])

    def get_quote(self, symbol):
        response, data = self.oauth_client.request( self.SITE
                                                    + self.GET_QUOTE
                                                    + self.RETURN_TYPE_JSON
                                                    + '?symbols='
                                                    + symbol )
        self.quote.parse(data)
        # print self.quote.to_s()

    def get_search(self, symbol, expiration=None, strike1=None, strike2=None):
        search_string = ( self.SITE
                        + self.GET_SEARCH
                        + self.RETURN_TYPE_JSON
                        + '?symbol='
                        + symbol )

        if expiration != None:
            search_string += self.DATE_LESS_THAN_EQUAL_TO_QUERY
            search_string += expiration.strftime('%Y%m%d')
        else:
            search_string += self.DATE_GREATER_THAN_QUERY
            search_string += datetime.date.today().strftime('%Y%m%d')

        if strike1 != None and strike2 == None:
            search_string += self.AND_GTE_STRIKE + str(strike1)

        if strike1 != None and strike2 != None:
            search_string += self.AND_GTE_STRIKE + str(strike1)
            search_string += self.AND_LT_STRIKE + str(strike2)

        search_string += self.AND_STD_SIZE

        # print(search_string)
        response, data = self.oauth_client.request(search_string)

        self.search.parse(data)
        # print self.search.to_s()

