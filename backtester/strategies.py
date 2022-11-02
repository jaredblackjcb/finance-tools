from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import datetime
import pandas as pd

# Strategy for 401k
class DollarCostAverage(bt.Strategy):
    params = dict(
        monthly_cash=None,
        month_days=[1, 16],
    )
    
    def __init__(self, *args, **kwargs):
        self.order = None
        self.totalcost = 0
        self.shares_purchased = 0
        self.p.monthly_cash = args[0]


    def log(self, txt, datetime=None):
        datetime = datetime or self.datas[0].datetime.date()
        print(f"{datetime.isoformat()} - {txt}")

    def start(self):
        print(f"Monthly Cash: {self.p.monthly_cash}")
        self.broker.set_fundmode(fundmode=True, fundstartval=100.0)
        self.cash_start = self.broker.get_cash()
        self.fund_start_value = 100.0
        # Timer to trigger actions on closest trading day to dates in month_days
        self.add_timer(
            when= bt.timer.SESSION_START,
            monthdays=self.p.month_days,
            monthcarry=True,
        )

    # Takes place of next_start method, notify_timer contains logic to be triggered when the timer goes off
    def notify_timer(self, timer, when, *args):
        # Deposit money into the brokerage account
        cash_deposit = self.p.monthly_cash / len(self.p.month_days)
        self.broker.add_cash(cash_deposit)

        target_purchase = self.broker.get_value() + cash_deposit
        self.order_target_value(target=target_purchase)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    f"BUY EXECUTED, Price per Share ${order.executed.price:,.2f}, Shares Purchased {order.executed.size}, Total Cost ${order.executed.value:,.2f}, Commission ${order.executed.comm:.2f}"
                )
                # Add number of shares and the total cost to the running totals
                self.shares_purchased += order.executed.size
                self.totalcost += order.executed.value
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
            print(order.status, [order.Canceled, order.Margin, order.Rejected])

        self.order = None

    def stop(self):
        self.fund_roi = (self.broker.get_fundvalue() - self.fund_start_value) - 1
        end_portfolio_value = self.datas[0].close.array[0] * self.shares_purchased + self.broker.get_cash() # last closing price * units held + ending cash
        print('-'*50)
        print('DOLLAR COST AVERAGE')
        # print('Years in Market: {:.1f} years'.format((end_date - start_date).days/365))
        print(f"Shares Purchased: {self.shares_purchased:,.0f}")
        print(f"Final Closing Price: ${self.datas[0].close.array[0]}")
        print(f"Portfolio Value: ${end_portfolio_value:,.2f}")
        print(f"Cost: ${self.totalcost:,.2f}")
        print(f"Gross Return: ${end_portfolio_value - self.totalcost:,.2f}")
        print(f"Gross % Return: {((end_portfolio_value / self.totalcost - 1) * 100):.2f}%")
        print(f"Fund ROI: {self.fund_roi:.2f}%")
        # print(f"Annualized Return: {(100 * ((1 + self.fund_roi / 100) ** (365/(end_date - start_date).days - 1))):.2f}%")
        print('-'*50)



