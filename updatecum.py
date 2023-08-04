import pandas as pd
import numpy as np
import copy
data = pd.read_csv('top50.csv')
print(data)
df=copy.deepcopy(data)
#Remove stablecoins and duplicate protocol coins
excluded_currencies = ['BUSD', 'DAI', 'GUSD', 'HUSD', 'PAX', 'SAI', 'TUSD', 'USDC', 'USDK', 'USDT', 'USDT_ETH', 'USDT_OMNI', 'USDT_TRX', 'XAUT', 'BNB_ETH','LEO_EOS','RENBTC', 'WNXM', 'WETH', 'WBTC']
df = df[~df['ticker'].isin(excluded_currencies)]
# convert column 'date' to datetime form

# Chuyển đổi lại về dạng chuỗi với định dạng "2015-01-01"


# Chuyển cột "date" sang dạng datetime với định dạng "%Y-%m-%d"

print(df)
# calculate mom
df['mom_10'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(10)))
df['mom_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(15)))
df['mom_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(20)))
df['mom_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: np.log(x) - np.log(x.shift(25)))
#SMA factor
df['psma_15'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=15).mean()-1)
df['psma_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=20).mean()-1)
df['psma_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=25).mean()-1)
df['psma_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: x / x.rolling(window=30).mean()-1)
# SMA ratio factor
df['smaf_2_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=2).mean()/ x.rolling(window=20).mean()-1)
df['smaf_3_20'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=3).mean()/ x.rolling(window=20).mean()-1)
df['smaf_3_25'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=3).mean()/ x.rolling(window=25).mean()-1)
df['smaf_5_30'] = df.groupby('ticker')['price_usd'].transform(lambda x: x.rolling(window=5).mean()/ x.rolling(window=30).mean()-1)
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
    fde = fde.sort_values('date').groupby('ticker').apply(lambda x: x.assign(is_index=(x['cap_rank'].shift() <= n) & (x['date'] >= start_date))) \
                  .dropna(subset=['is_index']).reset_index(drop=True)
    fde=fde.dropna()
    return fde

fde=create_universe(fde, n=10, min_constituents=10)
filtered_data = fde[fde['is_index'] == True]
#ngày: sau ngày đạt được số quan sát tối thiểu, caprank:top10
print(filtered_data)
cum20mom = pd.melt(filtered_data, id_vars=['date','mom_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum20mom['n_day_ahead'] = cum20mom['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum20mom = cum20mom.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['mom_20'].rank(),
    weight=x['mom_20'].rank() - np.mean(x['mom_20'].rank()),
    scaled_weight=(x['mom_20'].rank() - np.mean(x['mom_20'].rank())) / np.sum(np.abs(x['mom_20'].rank() - np.mean(x['mom_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['mom_20'].rank() - np.mean(x['mom_20'].rank())) / np.sum(np.abs(x['mom_20'].rank() - np.mean(x['mom_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['mom_20'].rank() - np.mean(x['mom_20'].rank())) / np.sum(np.abs(x['mom_20'].rank() - np.mean(x['mom_20'].rank())))) + 1)
)).reset_index(drop=True)
cum20mom = cum20mom.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum20mom.to_csv("cum20mom.csv", index=False)
cum10mom = pd.melt(filtered_data, id_vars=['date','mom_10'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum10mom['n_day_ahead'] = cum10mom['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum10mom = cum10mom.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['mom_10'].rank(),
    weight=x['mom_10'].rank() - np.mean(x['mom_10'].rank()),
    scaled_weight=(x['mom_10'].rank() - np.mean(x['mom_10'].rank())) / np.sum(np.abs(x['mom_10'].rank() - np.mean(x['mom_10'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['mom_10'].rank() - np.mean(x['mom_10'].rank())) / np.sum(np.abs(x['mom_10'].rank() - np.mean(x['mom_10'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['mom_10'].rank() - np.mean(x['mom_10'].rank())) / np.sum(np.abs(x['mom_10'].rank() - np.mean(x['mom_10'].rank())))) + 1)
)).reset_index(drop=True)
cum10mom = cum10mom.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum10mom.to_csv("cum10mom.csv", index=False)
cum15mom = pd.melt(filtered_data, id_vars=['date','mom_15'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum15mom['n_day_ahead'] = cum15mom['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum15mom = cum15mom.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['mom_15'].rank(),
    weight=x['mom_15'].rank() - np.mean(x['mom_15'].rank()),
    scaled_weight=(x['mom_15'].rank() - np.mean(x['mom_15'].rank())) / np.sum(np.abs(x['mom_15'].rank() - np.mean(x['mom_15'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['mom_15'].rank() - np.mean(x['mom_15'].rank())) / np.sum(np.abs(x['mom_15'].rank() - np.mean(x['mom_15'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['mom_15'].rank() - np.mean(x['mom_15'].rank())) / np.sum(np.abs(x['mom_15'].rank() - np.mean(x['mom_15'].rank())))) + 1)
)).reset_index(drop=True)
cum15mom = cum15mom.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum15mom.to_csv("cum15mom.csv", index=False)
cum25mom = pd.melt(filtered_data, id_vars=['date','mom_25'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum25mom['n_day_ahead'] = cum25mom['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum25mom = cum25mom.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['mom_25'].rank(),
    weight=x['mom_25'].rank() - np.mean(x['mom_25'].rank()),
    scaled_weight=(x['mom_25'].rank() - np.mean(x['mom_25'].rank())) / np.sum(np.abs(x['mom_25'].rank() - np.mean(x['mom_25'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['mom_25'].rank() - np.mean(x['mom_25'].rank())) / np.sum(np.abs(x['mom_25'].rank() - np.mean(x['mom_25'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['mom_25'].rank() - np.mean(x['mom_25'].rank())) / np.sum(np.abs(x['mom_25'].rank() - np.mean(x['mom_25'].rank())))) + 1)
)).reset_index(drop=True)
cum25mom = cum25mom.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum25mom.to_csv("cum25mom.csv", index=False)
cum15psma = pd.melt(filtered_data, id_vars=['date','psma_15'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum15psma['n_day_ahead'] = cum15psma['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum15psma = cum15psma.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['psma_15'].rank(),
    weight=x['psma_15'].rank() - np.mean(x['psma_15'].rank()),
    scaled_weight=(x['psma_15'].rank() - np.mean(x['psma_15'].rank())) / np.sum(np.abs(x['psma_15'].rank() - np.mean(x['psma_15'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['psma_15'].rank() - np.mean(x['psma_15'].rank())) / np.sum(np.abs(x['psma_15'].rank() - np.mean(x['psma_15'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['psma_15'].rank() - np.mean(x['psma_15'].rank())) / np.sum(np.abs(x['psma_15'].rank() - np.mean(x['psma_15'].rank())))) + 1)
)).reset_index(drop=True)
cum15psma = cum15psma.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum15psma.to_csv("cum15psma.csv", index=False)
cum20psma = pd.melt(filtered_data, id_vars=['date','psma_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum20psma['n_day_ahead'] = cum20psma['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum20psma = cum20psma.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['psma_20'].rank(),
    weight=x['psma_20'].rank() - np.mean(x['psma_20'].rank()),
    scaled_weight=(x['psma_20'].rank() - np.mean(x['psma_20'].rank())) / np.sum(np.abs(x['psma_20'].rank() - np.mean(x['psma_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['psma_20'].rank() - np.mean(x['psma_20'].rank())) / np.sum(np.abs(x['psma_20'].rank() - np.mean(x['psma_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['psma_20'].rank() - np.mean(x['psma_20'].rank())) / np.sum(np.abs(x['psma_20'].rank() - np.mean(x['psma_20'].rank())))) + 1)
)).reset_index(drop=True)
cum20psma = cum20psma.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum20psma.to_csv("cum20psma.csv", index=False)
cum25psma = pd.melt(filtered_data, id_vars=['date','psma_25'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum25psma['n_day_ahead'] = cum25psma['target'].apply(lambda x: x.replace('15', '25')[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum25psma = cum25psma.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['psma_25'].rank(),
    weight=x['psma_25'].rank() - np.mean(x['psma_25'].rank()),
    scaled_weight=(x['psma_25'].rank() - np.mean(x['psma_25'].rank())) / np.sum(np.abs(x['psma_25'].rank() - np.mean(x['psma_25'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['psma_25'].rank() - np.mean(x['psma_25'].rank())) / np.sum(np.abs(x['psma_25'].rank() - np.mean(x['psma_25'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['psma_25'].rank() - np.mean(x['psma_25'].rank())) / np.sum(np.abs(x['psma_25'].rank() - np.mean(x['psma_25'].rank())))) + 1)
)).reset_index(drop=True)
cum25psma = cum25psma.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum25psma.to_csv("cum25psma.csv", index=False)
cum30psma = pd.melt(filtered_data, id_vars=['date','psma_30'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cum30psma['n_day_ahead'] = cum30psma['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cum30psma = cum30psma.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['psma_30'].rank(),
    weight=x['psma_30'].rank() - np.mean(x['psma_30'].rank()),
    scaled_weight=(x['psma_30'].rank() - np.mean(x['psma_30'].rank())) / np.sum(np.abs(x['psma_30'].rank() - np.mean(x['psma_30'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['psma_30'].rank() - np.mean(x['psma_30'].rank())) / np.sum(np.abs(x['psma_30'].rank() - np.mean(x['psma_30'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['psma_30'].rank() - np.mean(x['psma_30'].rank())) / np.sum(np.abs(x['psma_30'].rank() - np.mean(x['psma_30'].rank())))) + 1)
)).reset_index(drop=True)
cum30psma = cum30psma.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cum30psma.to_csv("cum30psma.csv", index=False)
cumsmaf_2_20 = pd.melt(filtered_data, id_vars=['date','smaf_2_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumsmaf_2_20['n_day_ahead'] = cumsmaf_2_20['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumsmaf_2_20 = cumsmaf_2_20.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['smaf_2_20'].rank(),
    weight=x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank()),
    scaled_weight=(x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank())) / np.sum(np.abs(x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank())) / np.sum(np.abs(x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank())) / np.sum(np.abs(x['smaf_2_20'].rank() - np.mean(x['smaf_2_20'].rank())))) + 1)
)).reset_index(drop=True)
cumsmaf_2_20 = cumsmaf_2_20.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumsmaf_2_20.to_csv("cumsmaf_2_20.csv", index=False)
cumsmaf_3_20 = pd.melt(filtered_data, id_vars=['date','smaf_3_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumsmaf_3_20['n_day_ahead'] = cumsmaf_3_20['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumsmaf_3_20 = cumsmaf_3_20.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['smaf_3_20'].rank(),
    weight=x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank()),
    scaled_weight=(x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank())) / np.sum(np.abs(x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank())) / np.sum(np.abs(x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank())) / np.sum(np.abs(x['smaf_3_20'].rank() - np.mean(x['smaf_3_20'].rank())))) + 1)
)).reset_index(drop=True)
cumsmaf_3_20 = cumsmaf_3_20.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumsmaf_3_20.to_csv("cumsmaf_3_20.csv", index=False)
cumsmaf_3_25 = pd.melt(filtered_data, id_vars=['date','smaf_3_25'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumsmaf_3_25['n_day_ahead'] = cumsmaf_3_25['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumsmaf_3_25 = cumsmaf_3_25.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['smaf_3_25'].rank(),
    weight=x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank()),
    scaled_weight=(x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank())) / np.sum(np.abs(x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank())) / np.sum(np.abs(x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank())) / np.sum(np.abs(x['smaf_3_25'].rank() - np.mean(x['smaf_3_25'].rank())))) + 1)
)).reset_index(drop=True)
cumsmaf_3_25 = cumsmaf_3_25.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumsmaf_3_25.to_csv("cumsmaf_3_25.csv", index=False)
cumsmaf_5_30 = pd.melt(filtered_data, id_vars=['date','smaf_5_30'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumsmaf_5_30['n_day_ahead'] = cumsmaf_5_30['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumsmaf_5_30 = cumsmaf_5_30.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['smaf_5_30'].rank(),
    weight=x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank()),
    scaled_weight=(x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank())) / np.sum(np.abs(x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank())) / np.sum(np.abs(x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank())) / np.sum(np.abs(x['smaf_5_30'].rank() - np.mean(x['smaf_5_30'].rank())))) + 1)
)).reset_index(drop=True)
cumsmaf_5_30 = cumsmaf_5_30.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumsmaf_5_30.to_csv("cumsmaf_5_30.csv", index=False)
cumrrp_15 = pd.melt(filtered_data, id_vars=['date','rrp_15'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumrrp_15['n_day_ahead'] = cumrrp_15['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumrrp_15 = cumrrp_15.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['rrp_15'].rank(),
    weight=x['rrp_15'].rank() - np.mean(x['rrp_15'].rank()),
    scaled_weight=(x['rrp_15'].rank() - np.mean(x['rrp_15'].rank())) / np.sum(np.abs(x['rrp_15'].rank() - np.mean(x['rrp_15'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['rrp_15'].rank() - np.mean(x['rrp_15'].rank())) / np.sum(np.abs(x['rrp_15'].rank() - np.mean(x['rrp_15'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['rrp_15'].rank() - np.mean(x['rrp_15'].rank())) / np.sum(np.abs(x['rrp_15'].rank() - np.mean(x['rrp_15'].rank())))) + 1)
)).reset_index(drop=True)
cumrrp_15 = cumrrp_15.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumrrp_15.to_csv("cumrrp_15.csv", index=False)
cumrrp_20 = pd.melt(filtered_data, id_vars=['date','rrp_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumrrp_20['n_day_ahead'] = cumrrp_20['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumrrp_20 = cumrrp_20.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['rrp_20'].rank(),
    weight=x['rrp_20'].rank() - np.mean(x['rrp_20'].rank()),
    scaled_weight=(x['rrp_20'].rank() - np.mean(x['rrp_20'].rank())) / np.sum(np.abs(x['rrp_20'].rank() - np.mean(x['rrp_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['rrp_20'].rank() - np.mean(x['rrp_20'].rank())) / np.sum(np.abs(x['rrp_20'].rank() - np.mean(x['rrp_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['rrp_20'].rank() - np.mean(x['rrp_20'].rank())) / np.sum(np.abs(x['rrp_20'].rank() - np.mean(x['rrp_20'].rank())))) + 1)
)).reset_index(drop=True)
cumrrp_20 = cumrrp_20.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumrrp_20.to_csv("cumrrp_20.csv", index=False)
cumrrp_25 = pd.melt(filtered_data, id_vars=['date','rrp_25'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumrrp_25['n_day_ahead'] = cumrrp_25['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumrrp_25 = cumrrp_25.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['rrp_25'].rank(),
    weight=x['rrp_25'].rank() - np.mean(x['rrp_25'].rank()),
    scaled_weight=(x['rrp_25'].rank() - np.mean(x['rrp_25'].rank())) / np.sum(np.abs(x['rrp_25'].rank() - np.mean(x['rrp_25'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['rrp_25'].rank() - np.mean(x['rrp_25'].rank())) / np.sum(np.abs(x['rrp_25'].rank() - np.mean(x['rrp_25'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['rrp_25'].rank() - np.mean(x['rrp_25'].rank())) / np.sum(np.abs(x['rrp_25'].rank() - np.mean(x['rrp_25'].rank())))) + 1)
)).reset_index(drop=True)
cumrrp_25 = cumrrp_25.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumrrp_25.to_csv("cumrrp_25.csv", index=False)
cumrrp_30 = pd.melt(filtered_data, id_vars=['date','rrp_30'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumrrp_30['n_day_ahead'] = cumrrp_30['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumrrp_30 = cumrrp_30.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['rrp_30'].rank(),
    weight=x['rrp_30'].rank() - np.mean(x['rrp_30'].rank()),
    scaled_weight=(x['rrp_30'].rank() - np.mean(x['rrp_30'].rank())) / np.sum(np.abs(x['rrp_30'].rank() - np.mean(x['rrp_30'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['rrp_30'].rank() - np.mean(x['rrp_30'].rank())) / np.sum(np.abs(x['rrp_30'].rank() - np.mean(x['rrp_30'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['rrp_30'].rank() - np.mean(x['rrp_30'].rank())) / np.sum(np.abs(x['rrp_30'].rank() - np.mean(x['rrp_30'].rank())))) + 1)
)).reset_index(drop=True)
cumrrp_30 = cumrrp_30.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumrrp_30.to_csv("cumrrp_30.csv", index=False)
cumdsh_15 = pd.melt(filtered_data, id_vars=['date','dsh_15'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumdsh_15['n_day_ahead'] = cumdsh_15['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumdsh_15 = cumdsh_15.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['dsh_15'].rank(),
    weight=x['dsh_15'].rank() - np.mean(x['dsh_15'].rank()),
    scaled_weight=(x['dsh_15'].rank() - np.mean(x['dsh_15'].rank())) / np.sum(np.abs(x['dsh_15'].rank() - np.mean(x['dsh_15'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['dsh_15'].rank() - np.mean(x['dsh_15'].rank())) / np.sum(np.abs(x['dsh_15'].rank() - np.mean(x['dsh_15'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['dsh_15'].rank() - np.mean(x['dsh_15'].rank())) / np.sum(np.abs(x['dsh_15'].rank() - np.mean(x['dsh_15'].rank())))) + 1)
)).reset_index(drop=True)
cumdsh_15 = cumdsh_15.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumdsh_15.to_csv("cumdsh_15.csv", index=False)
cumdsh_20 = pd.melt(filtered_data, id_vars=['date','dsh_20'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumdsh_20['n_day_ahead'] = cumdsh_20['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumdsh_20 = cumdsh_20.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['dsh_20'].rank(),
    weight=x['dsh_20'].rank() - np.mean(x['dsh_20'].rank()),
    scaled_weight=(x['dsh_20'].rank() - np.mean(x['dsh_20'].rank())) / np.sum(np.abs(x['dsh_20'].rank() - np.mean(x['dsh_20'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['dsh_20'].rank() - np.mean(x['dsh_20'].rank())) / np.sum(np.abs(x['dsh_20'].rank() - np.mean(x['dsh_20'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['dsh_20'].rank() - np.mean(x['dsh_20'].rank())) / np.sum(np.abs(x['dsh_20'].rank() - np.mean(x['dsh_20'].rank())))) + 1)
)).reset_index(drop=True)
cumdsh_20 = cumdsh_20.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumdsh_20.to_csv("cumdsh_20.csv", index=False)
cumdsh_25 = pd.melt(filtered_data, id_vars=['date','dsh_25'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumdsh_25['n_day_ahead'] = cumdsh_25['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumdsh_25 = cumdsh_25.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['dsh_25'].rank(),
    weight=x['dsh_25'].rank() - np.mean(x['dsh_25'].rank()),
    scaled_weight=(x['dsh_25'].rank() - np.mean(x['dsh_25'].rank())) / np.sum(np.abs(x['dsh_25'].rank() - np.mean(x['dsh_25'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['dsh_25'].rank() - np.mean(x['dsh_25'].rank())) / np.sum(np.abs(x['dsh_25'].rank() - np.mean(x['dsh_25'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['dsh_25'].rank() - np.mean(x['dsh_25'].rank())) / np.sum(np.abs(x['dsh_25'].rank() - np.mean(x['dsh_25'].rank())))) + 1)
)).reset_index(drop=True)
cumdsh_25 = cumdsh_25.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumdsh_25.to_csv("cumdsh_25.csv", index=False)
cumdsh_30 = pd.melt(filtered_data, id_vars=['date','dsh_30'], value_vars=filtered_data.filter(like='fwd_return_').columns,
                   var_name='target', value_name='simplereturn')
# Extract n_day_ahead from target
cumdsh_30['n_day_ahead'] = cumdsh_30['target'].apply(lambda x: x[11])
# Group by date and n_day_ahead, and calculate rank, weight, scaled_weight, and weighted_fwd_returns
cumdsh_30 = cumdsh_30.groupby(['date', 'n_day_ahead']).apply(lambda x: x.assign(
    rank=x['dsh_30'].rank(),
    weight=x['dsh_30'].rank() - np.mean(x['dsh_30'].rank()),
    scaled_weight=(x['dsh_30'].rank() - np.mean(x['dsh_30'].rank())) / np.sum(np.abs(x['dsh_30'].rank() - np.mean(x['dsh_30'].rank()))),
    weighted_fwd_returns=x['simplereturn'] * (x['dsh_30'].rank() - np.mean(x['dsh_30'].rank())) / np.sum(np.abs(x['dsh_30'].rank() - np.mean(x['dsh_30'].rank()))),
    log_factor_return=np.log(np.sum(x['simplereturn'] * (x['dsh_30'].rank() - np.mean(x['dsh_30'].rank())) / np.sum(np.abs(x['dsh_30'].rank() - np.mean(x['dsh_30'].rank())))) + 1)
)).reset_index(drop=True)
cumdsh_30 = cumdsh_30.groupby('n_day_ahead').apply(lambda x: x.sort_values('date').assign(cumreturn=x['log_factor_return'].cumsum()))
cumdsh_30.to_csv("cumdsh_30.csv", index=False)
cummega = pd.melt(filtered_data, id_vars=['date','ticker','fwd_return_1','fwd_return_2','fwd_return_3'], value_vars=['mom_10','mom_15','mom_20','mom_25', 'psma_15','psma_20','psma_25','psma_30', 'smaf_2_20','smaf_3_20','smaf_3_25','smaf_5_30', 'rrp_15','rrp_20','rrp_25','rrp_30', 'dsh_15', 'dsh_20', 'dsh_25', 'dsh_30'],
                   var_name='feature', value_name='value')

cummega = cummega.groupby(['date', 'feature']).apply(lambda x: x.assign(
    rank=x['value'].rank(),
    weight=x['value'].rank() - np.mean(x['value'].rank()),
    scaled_weight=(x['value'].rank() - np.mean(x['value'].rank())) / np.sum(np.abs(x['value'].rank() - np.mean(x['value'].rank()))),
    weighted_fwd_return_1=x['fwd_return_1'] * (x['value'].rank() - np.mean(x['value'].rank())) / np.sum(np.abs(x['value'].rank() - np.mean(x['value'].rank()))),
    weighted_fwd_return_2=x['fwd_return_2'] * (x['value'].rank() - np.mean(x['value'].rank())) / np.sum(np.abs(x['value'].rank() - np.mean(x['value'].rank()))),
    weighted_fwd_return_3=x['fwd_return_3'] * (x['value'].rank() - np.mean(x['value'].rank())) / np.sum(np.abs(x['value'].rank() - np.mean(x['value'].rank()))),
)).reset_index(drop=True)
cummega['megafactor'] = cummega.groupby(['date', 'ticker'])['rank'].transform('mean')
cummega['weight'] = cummega['megafactor'] - np.mean(cummega['megafactor'])
scaled_weight_sum = np.sum(np.abs(cummega['weight']))
cummega['scaled_weight'] = cummega['weight'] / scaled_weight_sum
cummega['weighted_fwd_return_1'] = cummega['fwd_return_1'] * cummega['scaled_weight']
cummega['weighted_fwd_return_2'] = cummega['fwd_return_2'] * cummega['scaled_weight']
cummega['weighted_fwd_return_3'] = cummega['fwd_return_3'] * cummega['scaled_weight']
cummega = cummega.groupby('date').agg(
    log_factor_return_1=('weighted_fwd_return_1', lambda x: np.log(np.sum(x) + 1)),
    log_factor_return_2=('weighted_fwd_return_2', lambda x: np.log(np.sum(x) + 1)),
    log_factor_return_3=('weighted_fwd_return_3', lambda x: np.log(np.sum(x) + 1))
).reset_index()
cummega = cummega.sort_values(by='date')
cummega['gap_0'] = np.cumsum(cummega['log_factor_return_1'])
cummega['gap_1'] = np.cumsum(cummega['log_factor_return_2'])
cummega['gap_2'] = np.cumsum(cummega['log_factor_return_3'])
long_df = pd.melt(cummega, id_vars='date', value_vars=['gap_0', 'gap_1', 'gap_2'], var_name='gap', value_name='cumreturn')
long_df.to_csv("long_df.csv", index=False)
