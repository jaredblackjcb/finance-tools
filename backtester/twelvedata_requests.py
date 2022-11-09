import requests
import pandas as pd

def request_daily_time_series(start_date, end_date, symbol):
    requestParams = {'start_date': start_date, 'end_date': end_date, 'symbol': symbol, 'interval': '1day', 'apikey': '565663eb5ded412cbbdbe5ef49f0997b'}
    try:
        response = requests.get("https://api.twelvedata.com/time_series", params=requestParams, timeout=15)
        response.raise_for_status()
        response_data = response.json()
        stockData = pd.DataFrame(response_data['values'])
        stockData['datetime'] = pd.to_datetime(stockData['datetime'], format='%Y-%m-%d')
        stockData['open'] = pd.to_numeric(stockData['open'])
        stockData['high'] = pd.to_numeric(stockData['high'])
        stockData['low'] = pd.to_numeric(stockData['low'])
        stockData['close'] = pd.to_numeric(stockData['close'])
        stockData['volume'] = pd.to_numeric(stockData['volume'])
        stockData.set_index('datetime', inplace=True, drop=True)
        return stockData[::-1]
    except requests.exceptions.HTTPError as http_err:
        print(http_err)
    except requests.exceptions.ConnectionError as con_err:
        print(con_err)
    except requests.exceptions.Timeout as timeout_errt:
        print(timeout_errt)
    except requests.exceptions.RequestException as request_err:
        print(request_err)