import streamlit as st
import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv('top50.csv')
print(data)
df=copy.deepcopy(data)
#Remove stablecoins and duplicate protocol coins
excluded_currencies = ['BUSD', 'DAI', 'GUSD', 'HUSD', 'PAX', 'SAI', 'TUSD', 'USDC', 'USDK', 'USDT', 'USDT_ETH', 'USDT_OMNI', 'USDT_TRX', 'XAUT', 'BNB_ETH','LEO_EOS','RENBTC', 'WNXM', 'WETH', 'WBTC']
df = df[~df['ticker'].isin(excluded_currencies)]
# convert column 'date' to datetime form
df['date'] = pd.to_datetime(df['date'])
print(df)
# calculate mom
df['mom_10'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(10)))
df['mom_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(15)))
df['mom_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(20)))
df['mom_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(25)))
#SMA factor
df['psma_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=15).mean())
df['psma_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=20).mean())
df['psma_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=25).mean())
df['psma_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=30).mean())
# SMA ratio factor
df['smaf_2_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=2).mean()/ x.rolling(window=20).mean())
df['smaf_3_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=3).mean()/ x.rolling(window=20).mean())
df['smaf_3_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=3).mean()/ x.rolling(window=25).mean())
df['smaf_5_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=5).mean()/ x.rolling(window=30).mean())
# Rolling price zscore over recent history
df['rrp_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: (x - x.rolling(window=15).mean())/ x.rolling(window=15).std())
df['rrp_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: (x - x.rolling(window=20).mean())/ x.rolling(window=20).std())
df['rrp_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: (x - x.rolling(window=25).mean())/ x.rolling(window=25).std())
df['rrp_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: (x - x.rolling(window=30).mean())/ x.rolling(window=30).std())
# Rolling_days_since_high(x)
def rolling_days_since_high(x):
    idx_of_high = np.argmax(x)
    days_since_high = len(x) - idx_of_high
    return days_since_high

# daysincehigh=-rolling
df['dsh_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: -x.rolling(window=15).apply(rolling_days_since_high, raw=True) )
df['dsh_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: -x.rolling(window=20).apply(rolling_days_since_high, raw=True) )
df['dsh_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: -x.rolling(window=25).apply(rolling_days_since_high, raw=True) )
df['dsh_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: -x.rolling(window=30).apply(rolling_days_since_high, raw=True) )
# Calculate returns
df['fwd_log_return_1'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-1) / x))
df['fwd_log_return_2'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-2) / x.shift(-1)))
df['fwd_log_return_3'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-3) / x.shift(-2)))
df['fwd_log_return_4'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-4) / x.shift(-3)))
df['fwd_log_return_5'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-5) / x.shift(-4)))
df['fwd_log_return_6'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-6) / x.shift(-5)))
df['fwd_log_return_7'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x.shift(-7) / x.shift(-6)))
df['fwd_return_1'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-1) / x - 1)
df['fwd_return_2'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-2) / x.shift(-1)-1)
df['fwd_return_3'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-3) / x.shift(-2)-1)
df['fwd_return_4'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-4) / x.shift(-3)-1)
df['fwd_return_5'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-5) / x.shift(-4)-1)
df['fwd_return_6'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-6) / x.shift(-5)-1)
df['fwd_return_7'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.shift(-7) / x.shift(-6)-1)
df=df.dropna()
fde=copy.deepcopy(df)
def create_universe(fde, n=10, min_constituents=10):
    # Get first date where we have min_constituents
    start_date = fde.groupby('date').size().reset_index(name='count') \
                      .query('count >= @min_constituents') \
                      .agg({'date': 'min'}) \
                      .values[0]
    # Flag universe constituents
    fde['cap_rank'] = fde.groupby('date')['market_cap'].rank(ascending=False)
    fde = fde.sort_values('date').groupby('ticker').apply(lambda x: x.assign(is_index=(x['cap_rank'].shift(0) <= n) & (x['date'] >= start_date))) \
                  .dropna(subset=['is_index']).reset_index(drop=True)
    fde=fde.dropna()
    return fde

fde=create_universe(fde, n=10, min_constituents=10)
filtered_data = fde[fde['is_index'] == True]
#ngày: sau ngày đạt được số quan sát tối thiểu, caprank:top10
print(filtered_data)
filtered_data_1 = filtered_data.assign(rank=filtered_data.groupby('date')['mom_20'].rank().astype(int))


filtered_data_long = pd.melt(filtered_data_1, id_vars=['date', 'rank'], value_vars=filtered_data_1.filter(like='fwd_log_return_').columns,
                   var_name='target', value_name='logreturn')

# Extract n_day_ahead from target
filtered_data_long['n_day_ahead'] = filtered_data_long['target'].apply(lambda x: x[15])
filtered_data_long.groupby('rank')

print(filtered_data_long)

grouped_data = filtered_data_long.groupby(['rank', 'n_day_ahead'])['logreturn'].mean().reset_index()
ranks = grouped_data['rank'].unique()
n_day_ahead = grouped_data['n_day_ahead'].unique()
num_ranks = len(ranks)
num_n_day_ahead = len(n_day_ahead)

# Set width and spacing for bars
bar_width = 0.8 / num_n_day_ahead
bar_spacing = 0.0005

# Set x-axis positions for each rank
x = np.arange(num_ranks)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
for i, day_ahead in enumerate(n_day_ahead):
    data = grouped_data[grouped_data['n_day_ahead'] == day_ahead]
    bar_positions = x + (bar_width + bar_spacing) * (i - (num_n_day_ahead - 1) / 2)
    ax.bar(bar_positions, data['logreturn'], width=bar_width, label=f'n_day_ahead={day_ahead}')

ax.set_xlabel('Rank')
ax.set_ylabel('Mean(logreturn)')
ax.set_title('Mean(logreturn) by Rank and n_day_ahead')
ax.set_xticks(x)
ax.set_xticklabels(ranks)
ax.legend()
st.pyplot()

# Set width and spacing for bars
bar_width = 0.8 / len(ranks)
bar_spacing = 0.1

# Plotting
fig, axs = plt.subplots(len(n_day_ahead), 1, figsize=(10, 3 * len(n_day_ahead)), sharex=True)

for i, day_ahead in enumerate(n_day_ahead):
    data = grouped_data[grouped_data['n_day_ahead'] == day_ahead]
    ax = axs[i]

    for j, rank in enumerate(ranks):
        rank_data = data[data['rank'] == rank]
        bar_positions = np.arange(len(rank_data)) + (bar_width + bar_spacing) * j
        ax.bar(bar_positions, rank_data['logreturn'], width=bar_width, label=f'rank={rank}')

    ax.set_ylabel('Mean(logreturn)')
    ax.set_title(f'Mean(logreturn) for n_day_ahead={day_ahead}')
    ax.legend()

plt.xlabel('Rank')
plt.tight_layout()
st.pyplot()

# Extract year from 'date' column
filtered_data_long['year'] = pd.to_datetime(filtered_data_long['date']).dt.year
grouped_data = filtered_data_long.groupby(['year', 'rank', 'n_day_ahead'])['logreturn'].mean().reset_index()

# Prepare data for plotting
ranks = grouped_data['rank'].unique()
n_day_ahead = grouped_data['n_day_ahead'].unique()
years = grouped_data['year'].unique()

# Set width and spacing for bars
bar_width = 0.9 / len(ranks)
bar_spacing = 0.005

# Plotting
for year in years:
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, day_ahead in enumerate(n_day_ahead):
        data = grouped_data[(grouped_data['year'] == year) & (grouped_data['n_day_ahead'] == day_ahead)]
        bar_positions = np.arange(len(data)) + (bar_width + bar_spacing) * (i - (len(n_day_ahead) - 1) / 2)
        ax.bar(bar_positions, data['logreturn'], width=bar_width, label=f'n_day_ahead={day_ahead}')

    ax.set_xlabel('Rank')
    ax.set_ylabel('Mean(logreturn)')
    ax.set_title(f'Mean(logreturn) for Year {year}')
    ax.set_xticks(np.arange(len(ranks)))
    ax.set_xticklabels(ranks)
    ax.legend()
    st.pyplot()