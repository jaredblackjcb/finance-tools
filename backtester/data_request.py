from urllib import response
import requests

def request_daily_time_series(start_date, end_date, symbol):
    requestParams = {'start_date': start_date, 'end_date': end_date, 'symbol': symbol, 'interval': '1day', 'apikey': '565663eb5ded412cbbdbe5ef49f0997b'}
    try:
        response = requests.get("https://api.twelvedata.com/time_series", params=requestParams, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(http_err)
    except requests.exceptions.ConnectionError as con_err:
        print(con_err)
    except requests.exceptions.Timeout as timeout_errt:
        print(timeout_errt)
    except requests.exceptions.RequestException as request_err:
        print(request_err)
        

if __name__ == '__main__':
    data = request_daily_time_series('2022-10-01', '2022-10-15', 'spxl')
    for entry in data['values']:
        print(f"Date: {entry['datetime']}  Open: {entry['open']}")


