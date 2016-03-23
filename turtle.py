#!/usr/bin/python
import csv
import sys
import oandapy
class fx_csv_parser:
    def __init__(self,filename):
        self.date = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        reader = csv.reader(open(filename,"r"))
        b_first = True
        for row in reader:
            if not b_first:
                price = {}
                self.date.append(row[1])
                self.open.append(float(row[2]))
                self.high.append(float(row[3]))
                self.low.append(float(row[4]))
                self.close.append(float(row[5]))
            else:
                b_first = False
    def is_breakout(self,bid,ask,period_day):
        max     = self.get_max(period_day)
        min     = self.get_min(period_day)
        print "bid=%f,ask=%f,max=%f,min=%f" % (bid,ask,max,min)
        if ask > max  or bid < min:
            print "breakout"
        else:
            print "not breakout"
    def print_current_date(self):
        print self.date[0]
    def get_max(self,period_day):
        return max(self.high[0:period_day])
    def get_min(self,period_day):
        return min(self.low[0:period_day])


if __name__=="__main__":
    ACCESS_TOKEN = "325acc2db6bea755e773ed47ee4f5680-3dee3d060998281810c5dbf1dde3f5ec"
    oanda = oandapy.API(environment="practice", access_token=ACCESS_TOKEN)

    print "getting current prices..."
    response = oanda.get_prices(instruments="USD_JPY")
    prices = response.get("prices")

    bid = prices[0]["bid"]
    ask = prices[0]["ask"]

    parser = fx_csv_parser(sys.argv[1])
    parser.print_current_date() 
    parser.is_breakout(bid,ask,14) 


