import pandas as pd
import numpy as np
import copy
import streamlit as st 
import pandas as pd

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('top50.csv')

# Chuyển đổi cột 'date' sang định dạng datetime
df['date'] = pd.to_datetime(df['date'])

# Tìm ngày cuối cùng trong dữ liệu
latest_date = df['date'].max()

# Lấy thông tin các đồng tiền có vốn hóa thị trường nằm trong top 20 ở ngày cuối cùng
top_20_tickers = df[df['date'] == latest_date].nlargest(20, 'market_cap')['ticker']

# Lọc dữ liệu ban đầu chỉ để lại các đồng tiền nằm trong top 20 ở ngày cuối cùng
filtered_data = df[df['ticker'].isin(top_20_tickers)]

# Tính ngày bắt đầu của khoảng 30 ngày gần nhất
start_date = latest_date - pd.DateOffset(days=30)

# Lọc dữ liệu đã lọc trước để chỉ lấy thông tin cho 30 ngày gần nhất
filtered_data_30_days = filtered_data[(filtered_data['date'] >= start_date) & (filtered_data['date'] <= latest_date)]

# Hiển thị kết quả
print(filtered_data_30_days)