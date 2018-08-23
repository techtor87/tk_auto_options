#!/usr/bin/env python

import json

class Account():
    def __init__(self):
       self.account_num = None
       self.accountval = None
       self.fedcall = None
       self.housecall = None
       self.accruedinterest = None
       self.cash = None
       self.cashavail = None
       self.marginbalance = None
       self.mmf = None
       self.total = None
       self.uncleareddeposits = None
       self.unsettledfunds = None
       self.account_yield = None
       self.longoptions = None
       self.longstocks = None
       self.options = None
       self.shortoptions = None
       self.shortstocks = None
       self.stocks = None
       self.total = None
       self.totalsecurities = None

    def to_s(self):
       ret_str  = "account_num = " + self.account_num + "\n"
       ret_str += "accountval = " + self.accountval + "\n"
       ret_str += "fedcall = " + str(self.fedcall) + "\n"
       ret_str += "housecall = " + str(self.housecall) + "\n"
       ret_str += "accruedinterest = " + str(self.accruedinterest ) + "\n"
       ret_str += "cash = " + str(self.cash) + "\n"
       ret_str += "cashavail = " + str(self.cashavail) + "\n"
       ret_str += "marginbalance = " + str(self.marginbalance) + "\n"
       ret_str += "mmf = " + str(self.mmf) + "\n"
       ret_str += "total = " + str(self.total) + "\n"
       ret_str += "uncleareddeposits = " + str(self.uncleareddeposits) + "\n"
       ret_str += "unsettledfunds = " + str(self.unsettledfunds) + "\n"
       ret_str += "account_yield = " + str(self.account_yield) + "\n"
       ret_str += "longoptions = " + str(self.longoptions) + "\n"
       ret_str += "longstocks = " + str(self.longstocks) + "\n"
       ret_str += "options = " + str(self.options) + "\n"
       ret_str += "shortoptions = " + str(self.shortoptions) + "\n"
       ret_str += "shortstocks = " + str(self.shortstocks) + "\n"
       ret_str += "stocks = " + str(self.stocks) + "\n"
       ret_str += "total = " + str(self.total) + "\n"
       ret_str += "totalsecurities = " + str(self.totalsecurities) + "\n"
       return ret_str

    def parse(self, data):
       parsed_data = json.loads(data)
       self.account_num = parsed_data['response']['accountbalance']['account']
       self.accountval = parsed_data['response']['accountbalance']['accountvalue']
       self.fedcall = parsed_data['response']['accountbalance']['fedcall']
       self.housecall = parsed_data['response']['accountbalance']['housecall']
       self.accruedinterest = parsed_data['response']['accountbalance']['money']['accruedinterest']
       self.cash = parsed_data['response']['accountbalance']['money']['cash']
       self.cashavail = parsed_data['response']['accountbalance']['money']['cashavailable']
       self.marginbalance = parsed_data['response']['accountbalance']['money']['marginbalance']
       self.mmf = parsed_data['response']['accountbalance']['money']['mmf']
       self.total = parsed_data['response']['accountbalance']['money']['total']
       self.uncleareddeposits = parsed_data['response']['accountbalance']['money']['uncleareddeposits']
       self.unsettledfunds = parsed_data['response']['accountbalance']['money']['unsettledfunds']
       self.account_yield = parsed_data['response']['accountbalance']['money']['yield']
       self.longoptions = parsed_data['response']['accountbalance']['securities']['longoptions']
       self.longstocks = parsed_data['response']['accountbalance']['securities']['longstocks']
       self.options = parsed_data['response']['accountbalance']['securities']['options']
       self.shortoptions = parsed_data['response']['accountbalance']['securities']['shortoptions']
       self.shortstocks = parsed_data['response']['accountbalance']['securities']['shortstocks']
       self.stocks = parsed_data['response']['accountbalance']['securities']['stocks']
       self.total = parsed_data['response']['accountbalance']['securities']['total']
       self.totalsecurities = parsed_data['response']['accountholdings']['totalsecurities']
       # print(json.dumps( parsed_data, indent=4))

    def value(self, string, input_val):
        if(string == 'account_num'):
            self.account_num = input_val

        if(string == 'accountval'):
            self.accountval = input_val

        if(string == 'fedcall'):
            self.fedcall = input_val

        if(string == 'housecall'):
            self.housecall = input_val

        if(string == 'accruedinterest'):
            self.accruedinterest = input_val

        if(string == 'cash'):
            self.cash = input_val

        if(string == 'cashavail'):
            self.cashavail = input_val

        if(string == 'marginbalance'):
            self.marginbalance = input_val

        if(string == 'mmf'):
            self.mmf = input_val

        if(string == 'total'):
            self.total = input_val

        if(string == 'uncleareddeposits'):
            self.uncleareddeposits = input_val

        if(string == 'unsettledfunds'):
            self.unsettledfunds = input_val

        if(string == 'account_yield'):
            self.account_yield = input_val

        if(string == 'longoptions'):
            self.longoptions = input_val

        if(string == 'longstocks'):
            self.longstocks = input_val

        if(string == 'options'):
            self.options = input_val

        if(string == 'shortoptions'):
            self.shortoptions = input_val

        if(string == 'shortstocks'):
            self.shortstocks = input_val

        if(string == 'stocks'):
            self.stocks = input_val

        if(string == 'total'):
            self.total = input_val

        if(string == 'totalsecurities'):
            self.totalsecurities = input_val


class Quote():
    def __init__(self):
        self.adp_100 = None
        self.adp_200 = None
        self.adp_50 = None
        self.adv_21 = None
        self.adv_30 = None
        self.adv_90 = None
        self.ask = None
        self.ask_time = None
        self.asksz = None
        self.basis = None
        self.beta = None
        self.bid = None
        self.bid_time = None
        self.bidsz = None
        self.bidtick = None
        self.chg = None
        self.chg_sign = None
        self.chg_t = None
        self.cl = None
        self.contract_size = None
        self.cusip = None
        self.date = None
        self.datetime = None
        self.days_to_expiration = None
        self.div = None
        self.divexdate = None
        self.divfreq = None
        self.divpaydt = None
        self.dollar_value = None
        self.eps = None
        self.exch = None
        self.exch_desc = None
        self.hi = None
        self.iad = None
        self.idelta = None
        self.igamma = None
        self.imp_volatility = None
        self.incr_vl = None
        self.irho = None
        self.issue_desc = None
        self.itheta = None
        self.ivega = None
        self.last = None
        self.lo = None
        self.name = None
        self.op_delivery = None
        self.op_flag = None
        self.op_style = None
        self.op_subclass = None
        self.openinterest = None
        self.opn = None
        self.opt_val = None
        self.pchg = None
        self.pchg_sign = None
        self.pcls = None
        self.pe = None
        self.phi = None
        self.plo = None
        self.popn = None
        self.pr_adp_100 = None
        self.pr_adp_200 = None
        self.pr_adp_50 = None
        self.pr_date = None
        self.pr_openinterest = None
        self.prbook = None
        self.prchg = None
        self.prem_mult = None
        self.put_call = None
        self.pvol = None
        self.qcond = None
        self.rootsymbol = None
        self.secclass = None
        self.sesn = None
        self.sho = None
        self.strikeprice = None
        self.symbol = None
        self.tcond = None
        self.timestamp = None
        self.tr_num = None
        self.tradetick = None
        self.trend = None
        self.under_cusip = None
        self.undersymbol = None
        self.vl = None
        self.volatility12 = None
        self.vwap = None
        self.wk52hi = None
        self.wk52hidate = None
        self.wk52lo = None
        self.wk52lodate = None
        self.xdate = None
        self.xday = None
        self.xmonth = None
        self.xyear = None
        self.account_yield = None

    def to_s(self):
        ret_str = "adp_100 = " + str(self.adp_100) + "\n"
        ret_str += "adp_200 = " + str(self.adp_200) + "\n"
        ret_str += "adp_50 = " + str(self.adp_50) + "\n"
        ret_str += "adv_21 = " + str(self.adv_21) + "\n"
        ret_str += "adv_30 = " + str(self.adv_30) + "\n"
        ret_str += "adv_90 = " + str(self.adv_90) + "\n"
        ret_str += "ask = " + str(self.ask) + "\n"
        ret_str += "ask_time = " + str(self.ask_time) + "\n"
        ret_str += "asksz = " + str(self.asksz) + "\n"
        ret_str += "basis = " + str(self.basis) + "\n"
        ret_str += "beta = " + str(self.beta) + "\n"
        ret_str += "bid = " + str(self.bid) + "\n"
        ret_str += "bid_time = " + str(self.bid_time) + "\n"
        ret_str += "bidsz = " + str(self.bidsz) + "\n"
        ret_str += "bidtick = " + str(self.bidtick) + "\n"
        ret_str += "chg = " + str(self.chg) + "\n"
        ret_str += "chg_sign = " + str(self.chg_sign) + "\n"
        ret_str += "chg_t = " + str(self.chg_t) + "\n"
        ret_str += "cl = " + str(self.cl) + "\n"
        ret_str += "contract_size = " + str(self.contract_size) + "\n"
        ret_str += "cusip = " + str(self.cusip) + "\n"
        ret_str += "date = " + str(self.date) + "\n"
        ret_str += "datetime = " + str(self.datetime) + "\n"
        ret_str += "days_to_expiration = " + str(self.days_to_expiration) + "\n"
        ret_str += "div = " + str(self.div) + "\n"
        ret_str += "divexdate = " + str(self.divexdate) + "\n"
        ret_str += "divfreq = " + str(self.divfreq) + "\n"
        ret_str += "divpaydt = " + str(self.divpaydt) + "\n"
        ret_str += "dollar_value = " + str(self.dollar_value) + "\n"
        ret_str += "eps = " + str(self.eps) + "\n"
        ret_str += "exch = " + str(self.exch) + "\n"
        ret_str += "exch_desc = " + str(self.exch_desc) + "\n"
        ret_str += "hi = " + str(self.hi) + "\n"
        ret_str += "iad = " + str(self.iad) + "\n"
        ret_str += "idelta = " + str(self.idelta) + "\n"
        ret_str += "igamma = " + str(self.igamma) + "\n"
        ret_str += "imp_volatility = " + str(self.imp_volatility) + "\n"
        ret_str += "incr_vl = " + str(self.incr_vl) + "\n"
        ret_str += "irho = " + str(self.irho) + "\n"
        ret_str += "issue_desc = " + str(self.issue_desc) + "\n"
        ret_str += "itheta = " + str(self.itheta) + "\n"
        ret_str += "ivega = " + str(self.ivega) + "\n"
        ret_str += "last = " + str(self.last) + "\n"
        ret_str += "lo = " + str(self.lo) + "\n"
        ret_str += "name = " + str(self.name) + "\n"
        ret_str += "op_delivery = " + str(self.op_delivery) + "\n"
        ret_str += "op_flag = " + str(self.op_flag) + "\n"
        ret_str += "op_style = " + str(self.op_style) + "\n"
        ret_str += "op_subclass = " + str(self.op_subclass) + "\n"
        ret_str += "openinterest = " + str(self.openinterest) + "\n"
        ret_str += "opn = " + str(self.opn) + "\n"
        ret_str += "opt_val = " + str(self.opt_val) + "\n"
        ret_str += "pchg = " + str(self.pchg) + "\n"
        ret_str += "pchg_sign = " + str(self.pchg_sign) + "\n"
        ret_str += "pcls = " + str(self.pcls) + "\n"
        ret_str += "pe = " + str(self.pe) + "\n"
        ret_str += "phi = " + str(self.phi) + "\n"
        ret_str += "plo = " + str(self.plo) + "\n"
        ret_str += "popn = " + str(self.popn) + "\n"
        ret_str += "pr_adp_100 = " + str(self.pr_adp_100) + "\n"
        ret_str += "pr_adp_200 = " + str(self.pr_adp_200) + "\n"
        ret_str += "pr_adp_50 = " + str(self.pr_adp_50) + "\n"
        ret_str += "pr_date = " + str(self.pr_date) + "\n"
        ret_str += "pr_openinterest = " + str(self.pr_openinterest) + "\n"
        ret_str += "prbook = " + str(self.prbook) + "\n"
        ret_str += "prchg = " + str(self.prchg) + "\n"
        ret_str += "prem_mult = " + str(self.prem_mult) + "\n"
        ret_str += "put_call = " + str(self.put_call) + "\n"
        ret_str += "pvol = " + str(self.pvol) + "\n"
        ret_str += "qcond = " + str(self.qcond) + "\n"
        ret_str += "rootsymbol = " + str(self.rootsymbol) + "\n"
        ret_str += "secclass = " + str(self.secclass) + "\n"
        ret_str += "sesn = " + str(self.sesn) + "\n"
        ret_str += "sho = " + str(self.sho) + "\n"
        ret_str += "strikeprice = " + str(self.strikeprice) + "\n"
        ret_str += "symbol = " + str(self.symbol) + "\n"
        ret_str += "tcond = " + str(self.tcond) + "\n"
        ret_str += "timestamp = " + str(self.timestamp) + "\n"
        ret_str += "tr_num = " + str(self.tr_num) + "\n"
        ret_str += "tradetick = " + str(self.tradetick) + "\n"
        ret_str += "trend = " + str(self.trend) + "\n"
        ret_str += "under_cusip = " + str(self.under_cusip) + "\n"
        ret_str += "undersymbol = " + str(self.undersymbol) + "\n"
        ret_str += "vl = " + str(self.vl) + "\n"
        ret_str += "volatility12 = " + str(self.volatility12) + "\n"
        ret_str += "vwap = " + str(self.vwap) + "\n"
        ret_str += "wk52hi = " + str(self.wk52hi) + "\n"
        ret_str += "wk52hidate = " + str(self.wk52hidate) + "\n"
        ret_str += "wk52lo = " + str(self.wk52lo) + "\n"
        ret_str += "wk52lodate = " + str(self.wk52lodate) + "\n"
        ret_str += "xdate = " + str(self.xdate) + "\n"
        ret_str += "xday = " + str(self.xday) + "\n"
        ret_str += "xmonth = " + str(self.xmonth) + "\n"
        ret_str += "xyear = " + str(self.xyear) + "\n"
        ret_str += "account_yield = " + str(self.account_yield) + "\n"
        return ret_str

    def parse(self, data):
        parsed_data = json.loads(data)
        self.adp_100 = parsed_data['response']['quotes']['quote']['adp_100']
        self.adp_200 = parsed_data['response']['quotes']['quote']['adp_200']
        self.adp_50 = parsed_data['response']['quotes']['quote']['adp_50']
        self.adv_21 = parsed_data['response']['quotes']['quote']['adv_21']
        self.adv_30 = parsed_data['response']['quotes']['quote']['adv_30']
        self.adv_90 = parsed_data['response']['quotes']['quote']['adv_90']
        self.ask = parsed_data['response']['quotes']['quote']['ask']
        self.ask_time = parsed_data['response']['quotes']['quote']['ask_time']
        self.asksz = parsed_data['response']['quotes']['quote']['asksz']
        self.basis = parsed_data['response']['quotes']['quote']['basis']
        self.beta = parsed_data['response']['quotes']['quote']['beta']
        self.bid = parsed_data['response']['quotes']['quote']['bid']
        self.bid_time = parsed_data['response']['quotes']['quote']['bid_time']
        self.bidsz = parsed_data['response']['quotes']['quote']['bidsz']
        self.bidtick = parsed_data['response']['quotes']['quote']['bidtick']
        self.chg = parsed_data['response']['quotes']['quote']['chg']
        self.chg_sign = parsed_data['response']['quotes']['quote']['chg_sign']
        self.chg_t = parsed_data['response']['quotes']['quote']['chg_t']
        self.cl = parsed_data['response']['quotes']['quote']['cl']
        self.contract_size = parsed_data['response']['quotes']['quote']['contract_size']
        self.cusip = parsed_data['response']['quotes']['quote']['cusip']
        self.date = parsed_data['response']['quotes']['quote']['date']
        self.datetime = parsed_data['response']['quotes']['quote']['datetime']
        self.days_to_expiration = parsed_data['response']['quotes']['quote']['days_to_expiration']
        self.div = parsed_data['response']['quotes']['quote']['div']
        self.divexdate = parsed_data['response']['quotes']['quote']['divexdate']
        self.divfreq = parsed_data['response']['quotes']['quote']['divfreq']
        self.divpaydt = parsed_data['response']['quotes']['quote']['divpaydt']
        self.dollar_value = parsed_data['response']['quotes']['quote']['dollar_value']
        self.eps = parsed_data['response']['quotes']['quote']['eps']
        self.exch = parsed_data['response']['quotes']['quote']['exch']
        self.exch_desc = parsed_data['response']['quotes']['quote']['exch_desc']
        self.hi = parsed_data['response']['quotes']['quote']['hi']
        self.iad = parsed_data['response']['quotes']['quote']['iad']
        self.idelta = parsed_data['response']['quotes']['quote']['idelta']
        self.igamma = parsed_data['response']['quotes']['quote']['igamma']
        self.imp_volatility = parsed_data['response']['quotes']['quote']['imp_volatility']
        self.incr_vl = parsed_data['response']['quotes']['quote']['incr_vl']
        self.irho = parsed_data['response']['quotes']['quote']['irho']
        self.issue_desc = parsed_data['response']['quotes']['quote']['issue_desc']
        self.itheta = parsed_data['response']['quotes']['quote']['itheta']
        self.ivega = parsed_data['response']['quotes']['quote']['ivega']
        self.last = parsed_data['response']['quotes']['quote']['last']
        self.lo = parsed_data['response']['quotes']['quote']['lo']
        self.name = parsed_data['response']['quotes']['quote']['name']
        self.op_delivery = parsed_data['response']['quotes']['quote']['op_delivery']
        self.op_flag = parsed_data['response']['quotes']['quote']['op_flag']
        self.op_style = parsed_data['response']['quotes']['quote']['op_style']
        self.op_subclass = parsed_data['response']['quotes']['quote']['op_subclass']
        self.openinterest = parsed_data['response']['quotes']['quote']['openinterest']
        self.opn = parsed_data['response']['quotes']['quote']['opn']
        self.opt_val = parsed_data['response']['quotes']['quote']['opt_val']
        self.pchg = parsed_data['response']['quotes']['quote']['pchg']
        self.pchg_sign = parsed_data['response']['quotes']['quote']['pchg_sign']
        self.pcls = parsed_data['response']['quotes']['quote']['pcls']
        self.pe = parsed_data['response']['quotes']['quote']['pe']
        self.phi = parsed_data['response']['quotes']['quote']['phi']
        self.plo = parsed_data['response']['quotes']['quote']['plo']
        self.popn = parsed_data['response']['quotes']['quote']['popn']
        self.pr_adp_100 = parsed_data['response']['quotes']['quote']['pr_adp_100']
        self.pr_adp_200 = parsed_data['response']['quotes']['quote']['pr_adp_200']
        self.pr_adp_50 = parsed_data['response']['quotes']['quote']['pr_adp_50']
        self.pr_date = parsed_data['response']['quotes']['quote']['pr_date']
        self.pr_openinterest = parsed_data['response']['quotes']['quote']['pr_openinterest']
        self.prbook = parsed_data['response']['quotes']['quote']['prbook']
        self.prchg = parsed_data['response']['quotes']['quote']['prchg']
        self.prem_mult = parsed_data['response']['quotes']['quote']['prem_mult']
        self.put_call = parsed_data['response']['quotes']['quote']['put_call']
        self.pvol = parsed_data['response']['quotes']['quote']['pvol']
        self.qcond = parsed_data['response']['quotes']['quote']['qcond']
        self.rootsymbol = parsed_data['response']['quotes']['quote']['rootsymbol']
        self.secclass = parsed_data['response']['quotes']['quote']['secclass']
        self.sesn = parsed_data['response']['quotes']['quote']['sesn']
        self.sho = parsed_data['response']['quotes']['quote']['sho']
        self.strikeprice = parsed_data['response']['quotes']['quote']['strikeprice']
        self.symbol = parsed_data['response']['quotes']['quote']['symbol']
        self.tcond = parsed_data['response']['quotes']['quote']['tcond']
        self.timestamp = parsed_data['response']['quotes']['quote']['timestamp']
        self.tr_num = parsed_data['response']['quotes']['quote']['tr_num']
        self.tradetick = parsed_data['response']['quotes']['quote']['tradetick']
        self.trend = parsed_data['response']['quotes']['quote']['trend']
        self.under_cusip = parsed_data['response']['quotes']['quote']['under_cusip']
        self.undersymbol = parsed_data['response']['quotes']['quote']['undersymbol']
        self.vl = parsed_data['response']['quotes']['quote']['vl']
        self.volatility12 = parsed_data['response']['quotes']['quote']['volatility12']
        self.vwap = parsed_data['response']['quotes']['quote']['vwap']
        self.wk52hi = parsed_data['response']['quotes']['quote']['wk52hi']
        self.wk52hidate = parsed_data['response']['quotes']['quote']['wk52hidate']
        self.wk52lo = parsed_data['response']['quotes']['quote']['wk52lo']
        self.wk52lodate = parsed_data['response']['quotes']['quote']['wk52lodate']
        self.xdate = parsed_data['response']['quotes']['quote']['xdate']
        self.xday = parsed_data['response']['quotes']['quote']['xday']
        self.xmonth = parsed_data['response']['quotes']['quote']['xmonth']
        self.xyear = parsed_data['response']['quotes']['quote']['xyear']
        self.account_yield = parsed_data['response']['quotes']['quote']['yield']

        # print(json.dumps( parsed_data, indent=4))

class Search_quote():
    def __init__(self):
        self.ask = None
        self.ask_time = None
        self.asksz = None
        self.basis = None
        self.bid = None
        self.bid_time = None
        self.bidsz = None
        self.chg = None
        self.chg_sign = None
        self.chg_t = None
        self.cl = None
        self.contract_size = None
        self.date = None
        self.datetime = None
        self.days_to_expiration = None
        self.exch = None
        self.exch_desc = None
        self.hi = None
        self.incr_vl = None
        self.issue_desc = None
        self.last = None
        self.lo = None
        self.op_delivery = None
        self.op_flag = None
        self.op_style = None
        self.op_subclass = None
        self.opn = None
        self.pchg = None
        self.pchg_sign = None
        self.pcls = None
        self.phi = None
        self.plo = None
        self.popn = None
        self.pr_date = None
        self.pr_openinterest = None
        self.prchg = None
        self.prem_mult = None
        self.put_call = None
        self.pvol = None
        self.rootsymbol = None
        self.secclass = None
        self.sesn = None
        self.strikeprice = None
        self.symbol = None
        self.tcond = None
        self.timestamp = None
        self.tr_num = None
        self.tradetick = None
        self.under_cusip = None
        self.undersymbol = None
        self.vl = None
        self.vwap = None
        self.wk52hi = None
        self.wk52hidate = None
        self.wk52lo = None
        self.wk52lodate = None
        self.xdate = None
        self.xday = None
        self.xmonth = None
        self.xyear = None
        self.imp_volatility = None
        self.idelta = None
        self.igamma = None
        self.itheta = None
        self.ivega = None
        self.irho = None
        self.openinterest = None

    def to_s(self):
        ret_str = "ask = " + str(self.ask) + "\n"
        ret_str += "ask_time = " + str(self.ask_time) + "\n"
        ret_str += "asksz = " + str(self.asksz) + "\n"
        ret_str += "basis = " + str(self.basis) + "\n"
        ret_str += "bid = " + str(self.bid) + "\n"
        ret_str += "bid_time = " + str(self.bid_time) + "\n"
        ret_str += "bidsz = " + str(self.bidsz) + "\n"
        ret_str += "chg = " + str(self.chg) + "\n"
        ret_str += "chg_sign = " + str(self.chg_sign) + "\n"
        ret_str += "chg_t = " + str(self.chg_t) + "\n"
        ret_str += "cl = " + str(self.cl) + "\n"
        ret_str += "contract_size = " + str(self.contract_size) + "\n"
        ret_str += "date = " + str(self.date) + "\n"
        ret_str += "datetime = " + str(self.datetime) + "\n"
        ret_str += "days_to_expiration = " + str(self.days_to_expiration) + "\n"
        ret_str += "exch = " + str(self.exch) + "\n"
        ret_str += "exch_desc = " + str(self.exch_desc) + "\n"
        ret_str += "hi = " + str(self.hi) + "\n"
        ret_str += "incr_vl = " + str(self.incr_vl) + "\n"
        ret_str += "issue_desc = " + str(self.issue_desc) + "\n"
        ret_str += "last = " + str(self.last) + "\n"
        ret_str += "lo = " + str(self.lo) + "\n"
        ret_str += "op_delivery = " + str(self.op_delivery) + "\n"
        ret_str += "op_flag = " + str(self.op_flag) + "\n"
        ret_str += "op_style = " + str(self.op_style) + "\n"
        ret_str += "op_subclass = " + str(self.op_subclass) + "\n"
        ret_str += "opn = " + str(self.opn) + "\n"
        ret_str += "pchg = " + str(self.pchg) + "\n"
        ret_str += "pchg_sign = " + str(self.pchg_sign) + "\n"
        ret_str += "pcls = " + str(self.pcls) + "\n"
        ret_str += "phi = " + str(self.phi) + "\n"
        ret_str += "plo = " + str(self.plo) + "\n"
        ret_str += "popn = " + str(self.popn) + "\n"
        ret_str += "pr_date = " + str(self.pr_date) + "\n"
        ret_str += "pr_openinterest = " + str(self.pr_openinterest) + "\n"
        ret_str += "prchg = " + str(self.prchg) + "\n"
        ret_str += "prem_mult = " + str(self.prem_mult) + "\n"
        ret_str += "put_call = " + str(self.put_call) + "\n"
        ret_str += "pvol = " + str(self.pvol) + "\n"
        ret_str += "rootsymbol = " + str(self.rootsymbol) + "\n"
        ret_str += "secclass = " + str(self.secclass) + "\n"
        ret_str += "sesn = " + str(self.sesn) + "\n"
        ret_str += "strikeprice = " + str(self.strikeprice) + "\n"
        ret_str += "symbol = " + str(self.symbol) + "\n"
        ret_str += "tcond = " + str(self.tcond) + "\n"
        ret_str += "timestamp = " + str(self.timestamp) + "\n"
        ret_str += "tr_num = " + str(self.tr_num) + "\n"
        ret_str += "tradetick = " + str(self.tradetick) + "\n"
        ret_str += "under_cusip = " + str(self.under_cusip) + "\n"
        ret_str += "undersymbol = " + str(self.undersymbol) + "\n"
        ret_str += "vl = " + str(self.vl) + "\n"
        ret_str += "vwap = " + str(self.vwap) + "\n"
        ret_str += "wk52hi = " + str(self.wk52hi) + "\n"
        ret_str += "wk52hidate = " + str(self.wk52hidate) + "\n"
        ret_str += "wk52lo = " + str(self.wk52lo) + "\n"
        ret_str += "wk52lodate = " + str(self.wk52lodate) + "\n"
        ret_str += "xdate = " + str(self.xdate) + "\n"
        ret_str += "xday = " + str(self.xday) + "\n"
        ret_str += "xmonth = " + str(self.xmonth) + "\n"
        ret_str += "xyear = " + str(self.xyear) + "\n"
        ret_str += "imp_volatility = " + str(self.imp_volatility) + "\n"
        ret_str += "idelta = " + str(self.idelta) + "\n"
        ret_str += "igamma = " + str(self.igamma) + "\n"
        ret_str += "itheta = " + str(self.itheta) + "\n"
        ret_str += "ivega = " + str(self.ivega) + "\n"
        ret_str += "irho = " + str(self.irho) + "\n"
        ret_str += "openinterest = " + str(self.openinterest) + "\n"
        return ret_str

    def parse(self, parsed_data):
        self.ask = parsed_data['ask']
        self.ask_time = parsed_data['ask_time']
        self.asksz = parsed_data['asksz']
        self.basis = parsed_data['basis']
        self.bid = parsed_data['bid']
        self.bid_time = parsed_data['bid_time']
        self.bidsz = parsed_data['bidsz']
        self.chg = parsed_data['chg']
        self.chg_sign = parsed_data['chg_sign']
        self.chg_t = parsed_data['chg_t']
        self.cl = parsed_data['cl']
        self.contract_size = parsed_data['contract_size']
        self.date = parsed_data['date']
        self.datetime = parsed_data['datetime']
        self.days_to_expiration = parsed_data['days_to_expiration']
        self.exch = parsed_data['exch']
        self.exch_desc = parsed_data['exch_desc']
        self.hi = parsed_data['hi']
        self.incr_vl = parsed_data['incr_vl']
        self.issue_desc = parsed_data['issue_desc']
        self.last = parsed_data['last']
        self.lo = parsed_data['lo']
        self.op_delivery = parsed_data['op_delivery']
        self.op_flag = parsed_data['op_flag']
        self.op_style = parsed_data['op_style']
        self.op_subclass = parsed_data['op_subclass']
        self.opn = parsed_data['opn']
        self.pchg = parsed_data['pchg']
        self.pchg_sign = parsed_data['pchg_sign']
        self.pcls = parsed_data['pcls']
        self.phi = parsed_data['phi']
        self.plo = parsed_data['plo']
        self.popn = parsed_data['popn']
        self.pr_date = parsed_data['pr_date']
        self.pr_openinterest = parsed_data['pr_openinterest']
        self.prchg = parsed_data['prchg']
        self.prem_mult = parsed_data['prem_mult']
        self.put_call = parsed_data['put_call']
        self.pvol = parsed_data['pvol']
        self.rootsymbol = parsed_data['rootsymbol']
        self.secclass = parsed_data['secclass']
        self.sesn = parsed_data['sesn']
        self.strikeprice = parsed_data['strikeprice']
        self.symbol = parsed_data['symbol']
        self.tcond = parsed_data['tcond']
        self.timestamp = parsed_data['timestamp']
        self.tr_num = parsed_data['tr_num']
        self.tradetick = parsed_data['tradetick']
        self.under_cusip = parsed_data['under_cusip']
        self.undersymbol = parsed_data['undersymbol']
        self.vl = parsed_data['vl']
        self.vwap = parsed_data['vwap']
        self.wk52hi = parsed_data['wk52hi']
        self.wk52hidate = parsed_data['wk52hidate']
        self.wk52lo = parsed_data['wk52lo']
        self.wk52lodate = parsed_data['wk52lodate']
        self.xdate = parsed_data['xdate']
        self.xday = parsed_data['xday']
        self.xmonth = parsed_data['xmonth']
        self.xyear = parsed_data['xyear']
        self.imp_volatility = parsed_data['imp_Volatility']
        self.idelta = parsed_data['idelta']
        self.igamma = parsed_data['igamma']
        self.itheta = parsed_data['itheta']
        self.ivega = parsed_data['ivega']
        self.irho = parsed_data['irho']
        self.openinterest = parsed_data['openinterest']
        # print(json.dumps( parsed_data, indent=4))

class Search():
    def __init__(self):
        self.search_quote = []

    def to_s(self):
        ret_str = ""
        for quote in self.search_quote:
            ret_str += quote.to_s()
            ret_str += "\n"

        return ret_str


    def parse(self, data):
        parsed_data = json.loads(data)
        self.search_quote = []
        for quote in parsed_data['response']['quotes']['quote']:
            temp_search_quote = Search_quote()
            temp_search_quote.parse(quote)
            self.search_quote.append( temp_search_quote )

