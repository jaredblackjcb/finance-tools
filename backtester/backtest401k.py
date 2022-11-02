import backtrader as bt
from twelvedata_requests import request_daily_time_series




class Backtester():
    def __init__(self, ticker, start_date, end_date, strategy, monthly_cash):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.strategy = strategy
        self.monthly_cash = monthly_cash

    # Run the strategy
    def run(self, plot=False):
        # Create a cerebro entity
        cerebro = bt.Cerebro(stdstats=False)

        # Get data from Twelve Data
        stock_df = request_daily_time_series(start_date=self.start_date, end_date=self.end_date, symbol=self.ticker)
        print(stock_df)

        # Create a backtrader PandasData feed and add it to the cerebro instance
        data = bt.feeds.PandasData(dataname=stock_df)
        cerebro.adddata(data)

        # Add a strategy and set monthly_cash
        cerebro.addstrategy(self.strategy, self.monthly_cash)

        # Broker Information
        broker_args = dict(coc=True)
        cerebro.broker = bt.brokers.BackBroker(**broker_args)

        # Run cerebro
        cerebro.run()
        if plot:
            cerebro.plot()

        #TODO: return results