import pandas as pd
import numpy as np
import copy
import streamlit as st 
import pandas as pd
from datetime import datetime

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('voldf.csv')
df['date'] = pd.to_datetime(df['date'])

# Tìm ngày lớn nhất
max_date = df['date'].max()
print(max_date)

# Tính khoảng cách ngày giữa mỗi ngày và ngày lớn nhất
df['date_diff'] = (max_date - df['date']).dt.days


# Lọc ra các hàng có khoảng cách ngày nhỏ hơn hoặc bằng 10
result_df = df[df['date_diff'] <= 9]
result_df['rankmom_10'] = result_df.groupby('date')['mom_10'].rank()
result_df['rankmom_15'] = result_df.groupby('date')['mom_15'].rank()
result_df['rankmom_20'] = result_df.groupby('date')['mom_20'].rank()
result_df['rankmom_25'] = result_df.groupby('date')['mom_25'].rank()
result_df['rankpsma_15'] = result_df.groupby('date')['psma_15'].rank()
result_df['rankpsma_20'] = result_df.groupby('date')['psma_20'].rank()
result_df['rankpsma_25'] = result_df.groupby('date')['psma_25'].rank()
result_df['rankpsma_30'] = result_df.groupby('date')['psma_30'].rank()
result_df['ranksmaf_2_20'] = result_df.groupby('date')['smaf_2_20'].rank()
result_df['ranksmaf_3_20'] = result_df.groupby('date')['smaf_3_20'].rank()
result_df['ranksmaf_3_25'] = result_df.groupby('date')['smaf_3_25'].rank()
result_df['ranksmaf_5_30'] = result_df.groupby('date')['smaf_5_30'].rank()
result_df['rankrrp_15'] = result_df.groupby('date')['rrp_15'].rank()
result_df['rankrrp_20'] = result_df.groupby('date')['rrp_20'].rank()
result_df['rankrrp_25'] = result_df.groupby('date')['rrp_25'].rank()
result_df['rankrrp_30'] = result_df.groupby('date')['rrp_30'].rank()
result_df = result_df[['ticker','date','cap_rank','rankmom_10','rankmom_15','rankmom_20','rankmom_25','rankpsma_15','rankpsma_20','rankpsma_25','rankpsma_30','ranksmaf_2_20','ranksmaf_3_20','ranksmaf_3_25','ranksmaf_5_30','rankrrp_15','rankrrp_20','rankrrp_25','rankrrp_30' ]]
# In ra DataFrame sau khi lọc
print(result_df)
result_df = result_df.reset_index(drop=True)
columns_to_convert = [
    'cap_rank', 'rankmom_10', 'rankmom_15', 'rankmom_20', 'rankmom_25',
    'rankpsma_15', 'rankpsma_20', 'rankpsma_25', 'rankpsma_30',
    'ranksmaf_2_20', 'ranksmaf_3_20', 'ranksmaf_3_25', 'ranksmaf_5_30',
    'rankrrp_15', 'rankrrp_20', 'rankrrp_25', 'rankrrp_30'
]

# Chuyển đổi các cột sang kiểu integer
result_df[columns_to_convert] = result_df[columns_to_convert].astype(int)
result_df["date"] = [
        datetime.datetime.strptime(
            str(target_date).split(" ")[0], '%Y-%m-%d').date()
        for target_date in result_df["date"]
    ]
st.dataframe(result_df)

