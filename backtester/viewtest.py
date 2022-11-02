from backtest401k import Backtester
from strategies import DollarCostAverage

if __name__ == '__main__':
    backtester = Backtester(ticker='spy', start_date='2020-01-01', end_date='2022-10-31', strategy=DollarCostAverage, monthly_cash=500.0)
    backtester.run()