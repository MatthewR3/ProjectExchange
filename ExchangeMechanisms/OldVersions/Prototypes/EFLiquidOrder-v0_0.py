#-------------------------------------------------------------------------------
# Name:        EFLiquidOrder-v0.0
# Purpose:
#
# Author:      Matthew
#
# Created:     05/04/2014
# Copyright:   (c) Matthew 2014
# Licence:     <your licence>
# Modified:    11/04/2014
#-------------------------------------------------------------------------------

import time

transaction_count = 1

buy_book = {}

sell_book = {}

class Order(object):

    def __init__(self, useraccount, x, y):
        self.useraccount = useraccount
        self.x = x
        self.y = y

    def add_buy_book_order(self): #Adds buy order to buy_book
        order_count = 0
        for i in buy_book:
            order_count += 1
        for i in sell_book:
            order_count += 1
        #print "order_count: " + str(order_count)
        order_number = order_count + 1 #Counts current number of orders and adds 1
        #print "order_number: " + str(order_number)
        order = "Order" + str(order_number) #Assigns order number to string as "Order#"
        #print "order: " + order
        buy_book[order] = [self.useraccount, self.x, self.y] #Adds to buy_book

    def add_sell_book_order(self): #Adds sell order to sell_book
        order_count = 0
        for i in buy_book:
            order_count += 1
        for i in sell_book:
            order_count += 1
        #print "order_count: " + str(order_count)
        order_number = order_count + 1 #Counts current number of orders and adds 1
        #print "order_number: " + str(order_number)
        order = "Order" + str(order_number) #Assigns order number to string as "Order#"
        #print "order: " + order
        sell_book[order] = [self.useraccount, self.x, self.y] #Adds to sell_book

#All items above this line are for testing



class Functions():

    def sell_price_check(self):
        sell_book_value_list = []
        buy_price_list = []
        for i in sell_book:
            sell_book_value_list = sell_book[i] #Creates list of orders in sell_book
            #print sell_book_value_list
            buy_price_list.append(sell_book_value_list[1]) #Creates list of prices in sell_book
        if buy_price_list == []:
            self.sell_price = "None"
            print "Buy Price: None below sell price."
        else:
            self.buy_price = max(buy_price_list) #Finds maximum price in list
            #print buy_price_list
            #print "Buy Price: " + str(self.buy_price)

    def buy_price_check(self):
        buy_book_value_list = []
        sell_price_list = []
        for i in buy_book:
            buy_book_value_list = buy_book[i] #Creates list of orders in buy_book
            #print buy_book_value_list
            sell_price_list.append(buy_book_value_list[1]) #Creates list of prices in sell_book
        if sell_price_list == []:
            self.sell_price = "None"
            print "Sell Price: None above buy price."
        else:
            self.sell_price = min(sell_price_list) #Finds minimum price in list
            #print sell_price_list
            #print "Sell Price: " + str(self.sell_price)

    def sell_volume_check(self):
        buy_price_order_volumes = []
        for i in sell_book.values():
            if i[1] == self.buy_price:
                buy_price_order_volumes.append(i[2]) #Makes a list of volumes of orders in price range
        if buy_price_order_volumes == []:
            print "Buy Order Volume: None"
        else:
            #print "Buy Price Order Volumes: " + str(buy_price_order_volumes)
            self.buy_order_volume = max(buy_price_order_volumes) #Sets maximum value in list of volumes at certain price
            #print "Buy Order Volume: " + str(self.buy_order_volume)

    def buy_volume_check(self):
        sell_price_order_volumes = []
        for i in buy_book.values():
            if i[1] == self.sell_price:
                sell_price_order_volumes.append(i[2]) #Makes a list of volumes of orders in price range
        #print "Sell Price Order Volumes: " + str(sell_price_order_volumes)
        if sell_price_order_volumes == []:
            print "Sell Order Volume: None"
        else:
            self.sell_order_volume = max(sell_price_order_volumes) #Sets maximum value in list of volumes at certain price
            #print "Sell Order Volume: " + str(self.sell_order_volume)

    def sell_top_order_check(self): #Labels account number and account of top buy order
        for i in range(len(sell_book)):
            if sell_book.values()[i][1] == self.buy_price and sell_book.values()[i][2] == self.buy_order_volume:
                self.sell_top_order_number = sell_book.keys()[i]
                self.sell_top_order_account = sell_book.values()[i][0]
            else:
                pass
        #print "Sell Top Order Number: " + str(self.sell_top_order_number)
        #print "Sell Top Order Account: " + str(self.sell_top_order_account)

    def buy_top_order_check(self): #Labels account number and account of top sell order
        for i in range(len(buy_book)):
            if buy_book.values()[i][1] == self.sell_price and buy_book.values()[i][2] == self.sell_order_volume:
                self.buy_top_order_number = buy_book.keys()[i]
                self.buy_top_order_account = buy_book.values()[i][0]
            else:
                pass
        #print "Buy Top Order Number: " + str(self.buy_top_order_number)
        #print "Buy Top Order Account: " + str(self.buy_top_order_account)

    def transaction(self): #Transaction mechanism
        if self.buy_price >= self.sell_price:
            localtime = time.localtime(time.time())
            local_time_minutes = localtime[4]
            local_time_seconds = localtime[5]
            if local_time_minutes < 10:
                local_time_minutes = "0" + str(local_time_minutes)
            if local_time_seconds < 10:
                local_time_seconds = "0" + str(local_time_seconds)
            self.formatted_date = str(localtime[1]) + "/" +  str(localtime[2]) + "/" +  str(localtime[0])
            self.formatted_time = str(localtime[3]) + ":" +  str(local_time_minutes) + ":" +  str(local_time_seconds)
            print "Transaction Date: " + self.formatted_date
            print "Transaction Time: " + self.formatted_time
            print "Transaction Number: " + str(transaction_count)
            print "Transacted Sell Order: " + str(self.sell_top_order_number)
            print "Transacted Buy Order: " + str(self.buy_top_order_number)
            self.transaction_price = max(self.buy_price, self.sell_price) #Assigns price at which transaction occurs with maximum profit
            print "Transaction Price: " + str(self.transaction_price)
            self.spread_profit_per_btc = self.buy_price - self.sell_price #Calculates profit gained by Bid/Ask spread
            print "Spread Profit Per BTC: " + str(self.spread_profit_per_btc)
            if self.buy_order_volume == self.sell_order_volume: #Performs volume calculations and reassignment
                self.spread_profit = self.spread_profit_per_btc * self.sell_order_volume
                del_sell_book_order(self.sell_top_order_number)
                del_buy_book_order(self.buy_top_order_number)
                self.transaction_volume = self.sell_order_volume
                print "Transaction Volume: " + str(self.transaction_volume)
                self.transaction_total = self.transaction_price * self.transaction_volume
                print "Transaction Total: " + str(self.transaction_total)
            elif self.buy_order_volume > self.sell_order_volume:
                new_buy_order_volume = self.buy_order_volume - self.sell_order_volume
                del_sell_book_order(self.sell_top_order_number)
                self.transaction_volume = self.sell_order_volume
                print "Transaction Volume: " + str(self.transaction_volume)
                self.spread_profit = self.spread_profit_per_btc * self.transaction_volume
                buy_book[str(self.buy_top_order_number)][2] = new_buy_order_volume
                self.transaction_total = self.transaction_price * self.transaction_volume
                print "Transaction Total: " + str(self.transaction_total)
            elif self.buy_order_volume < self.sell_order_volume:
                new_sell_order_volume = self.sell_order_volume - self.buy_order_volume
                del_buy_book_order(self.buy_top_order_number)
                self.transaction_volume = self.buy_order_volume
                print "Transaction Volume: " + str(self.transaction_volume)
                self.spread_profit = self.spread_profit_per_btc * self.transaction_volume
                sell_book[str(self.sell_top_order_number)][2] = new_sell_order_volume
                self.transaction_total = self.transaction_price * self.transaction_volume
                print "Transaction Total: " + str(self.transaction_total)
            print "Spread Profit: " + str(self.spread_profit)
            Function1.transaction_log()
        else:
            print "No orders within price match index."

    def transaction_log(self):
        log = open("Transaction" + str(transaction_count) + ".txt", "a") #Defines log file open variable
        log.write("----------" + "\n" + "Transaction Details:" + "\n" + "\n")
        log.write("Transaction Number: " + str(transaction_count) + "\n")
        log.write("Transaction Date: " + self.formatted_date + "\n")
        log.write("Transaction Time: " + self.formatted_time + "\n")
        log.write("Sell Account: " + self.sell_top_order_account + " - " + self.sell_top_order_number + "\n")
        log.write("Buy Account: " + self.buy_top_order_account + " - " + self.buy_top_order_number + "\n")
        log.write("Transaction Price: " + str(self.transaction_price) + "\n")
        log.write("Transaction Volume: " + str(self.transaction_volume) + "\n")
        log.write("Transaction Total: " + str(self.transaction_total) + "\n")
        log.write("Spread Profit: " + str(self.spread_profit) + "\n" + "\n")
        log.write("Account Crediting:" + "\n" + "\n")
        log.write(self.sell_top_order_account + ": +$" + str(self.transaction_total) + " and -" + str(self.transaction_volume) + " BTC" + "\n")
        log.write(self.buy_top_order_account + ": -$" + str(self.transaction_total) + " and +" + str(self.transaction_volume) + " BTC" + "\n")
        log.close()

def del_sell_book_order(order):
    del sell_book[order]

def del_buy_book_order(order):
    del buy_book[order]



#All items below this line are for testing

def transaction_sequence(): #Calls trading methods/functions in order
    global transaction_count
    Function1.sell_price_check()
    Function1.buy_price_check()
    while Function1.buy_price >= Function1.sell_price:
        print ""
        print "----------"
        print ""
        Function1.sell_price_check()
        Function1.buy_price_check()
        Function1.sell_volume_check()
        Function1.buy_volume_check()
        Function1.sell_top_order_check()
        Function1.buy_top_order_check()
        print ""
        Function1.transaction()
        transaction_count += 1
        print ""
        #Function1.sell_book_print()
        #Function1.buy_book_print()
        #buy_book_log()
        #sell_book_log()

UserOrder1 = Order("Account1", 520, 3)
UserOrder2 = Order("Account2", 580, 5)
UserOrder3 = Order("Account3", 720, 8)
UserOrder4 = Order("Account4", 410, 2)
UserOrder5 = Order("Account5", 600, 7)
Function1 = Functions()
UserOrder1.add_sell_book_order()
UserOrder2.add_sell_book_order()
UserOrder3.add_buy_book_order()
UserOrder4.add_buy_book_order()
UserOrder5.add_sell_book_order()

#collaborative()
transaction_sequence()