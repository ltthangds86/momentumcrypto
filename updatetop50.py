import numpy as np
import pandas as pd
import requests
import json
import datetime
import time

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
response = cg.get_coins_markets(vs_currency="USD")
response[0]
coins_list = [coin["id"] for coin in response[:40]]
coins_list
n_days = (datetime.date.today() - datetime.date(2018,12,31)).days
def get_date_information(value):
    """Function to get the datetime from epoch time"""
    return datetime.datetime.fromtimestamp(value[0]/1000)

def get_value_from_list(value):
    """Fucntion to get the value from response"""
    return value[1]

def get_historical_data_for_coin(coin_name, n_days):
    """Function to get the hisrotical data for one single coin"""
    coin_data = cg.get_coin_market_chart_by_id(id=coin_name, vs_currency='usd', days=n_days)
    coin_df = pd.DataFrame(coin_data)
    coin_df = coin_df.iloc[:-1] # Remove today
    coin_df["ticker"] = coin_name
    coin_df["date"] = coin_df["prices"].apply(lambda x: get_date_information(x))
    coin_df["price_usd"] = coin_df["prices"].apply(lambda x: get_value_from_list(x))
    coin_df["total_volume"] = coin_df["total_volumes"].apply(lambda x: get_value_from_list(x))
    coin_df["market_cap"] = coin_df["market_caps"].apply(lambda x: get_value_from_list(x))
    coin_df.drop(["prices", "total_volumes", "market_caps"], axis=1, inplace=True)
    return coin_df
dataframes_list = [get_historical_data_for_coin(coin_name, n_days) for coin_name in coins_list]
time.sleep(10)  # Not to overload API

# Gộp tất cả các DataFrame trong danh sách thành một DataFrame duy nhất
result_df = pd.concat(dataframes_list, ignore_index=True)
result_df['date'] = pd.to_datetime(result_df['date'])
result_df['date'] = result_df['date'].dt.strftime('%Y-%m-%d')

# Ghi DataFrame kết quả thành một tệp CSV duy nhất
output_file = "top50.csv"
result_df.to_csv(output_file, index=False)
