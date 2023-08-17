import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
# Đọc dữ liệu từ file CSV
cum10mom = pd.read_csv('cum10mom.csv')
cum15mom = pd.read_csv('cum15mom.csv')
cum20mom = pd.read_csv('cum20mom.csv')
cum25mom = pd.read_csv('cum25mom.csv')
cum15psma = pd.read_csv('cum15psma.csv')
cum20psma = pd.read_csv('cum20psma.csv')
cum25psma = pd.read_csv('cum25psma.csv')
cum30psma = pd.read_csv('cum30psma.csv')
cumrrp_15 = pd.read_csv('cumrrp_15.csv')
cumrrp_20 = pd.read_csv('cumrrp_20.csv')
cumrrp_25 = pd.read_csv('cumrrp_25.csv')
cumrrp_30 = pd.read_csv('cumrrp_30.csv')
cumsmaf_2_20 = pd.read_csv('cumsmaf_2_20.csv')
cumsmaf_3_20 = pd.read_csv('cumsmaf_3_20.csv')
cumsmaf_3_25 = pd.read_csv('cumsmaf_3_25.csv')
cumsmaf_5_30 = pd.read_csv('cumsmaf_5_30.csv')


cum10mom = cum10mom[cum10mom['n_day_ahead'].isin([1, 2, 3])]
cum10mom = cum10mom[['n_day_ahead', 'log_factor_return']]
cum10mom = cum10mom.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum10mom.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum10mom['volatility'] = volatility_series
mean_series = cum10mom.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum10mom['meanreturn'] = mean_series
cum10mom['factor investment'] = 'mom_10'
cum10mom = cum10mom[['factor investment','n_day_ahead','meanreturn','volatility']]
cum10mom = cum10mom.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum10mom['information_ratio'] = cum10mom['meanreturn'] / cum10mom['volatility']


cum15mom = cum15mom[cum15mom['n_day_ahead'].isin([1, 2, 3])]
cum15mom = cum15mom[['n_day_ahead', 'log_factor_return']]
cum15mom = cum15mom.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum15mom.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum15mom['volatility'] = volatility_series
mean_series = cum15mom.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum15mom['meanreturn'] = mean_series
cum15mom['factor investment'] = 'mom_15'
cum15mom = cum15mom[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum15mom = cum15mom.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum15mom['information_ratio'] = cum15mom['meanreturn'] / cum15mom['volatility']


cum20mom = cum20mom[cum20mom['n_day_ahead'].isin([1, 2, 3])]
cum20mom = cum20mom[['n_day_ahead', 'log_factor_return']]
cum20mom = cum20mom.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum20mom.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum20mom['volatility'] = volatility_series
mean_series = cum20mom.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum20mom['meanreturn'] = mean_series
cum20mom['factor investment'] = 'mom_20'
cum20mom = cum20mom[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum20mom = cum20mom.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum20mom['information_ratio'] = cum20mom['meanreturn'] / cum20mom['volatility']



cum25mom = cum25mom[cum25mom['n_day_ahead'].isin([1, 2, 3])]
cum25mom = cum25mom[['n_day_ahead', 'log_factor_return']]
cum25mom = cum25mom.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum25mom.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum25mom['volatility'] = volatility_series
mean_series = cum25mom.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum25mom['meanreturn'] = mean_series
cum25mom['factor investment'] = 'mom_25'
cum25mom = cum25mom[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum25mom = cum25mom.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum25mom['information_ratio'] = cum25mom['meanreturn'] / cum25mom['volatility']


cum15psma = cum15psma[cum15psma['n_day_ahead'].isin([1, 2, 3])]
cum15psma = cum15psma[['n_day_ahead', 'log_factor_return']]
cum15psma = cum15psma.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum15psma.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum15psma['volatility'] = volatility_series
mean_series = cum15psma.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum15psma['meanreturn'] = mean_series
cum15psma['factor investment'] = 'psma_15'
cum15psma = cum15psma[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum15psma = cum15psma.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum15psma['information_ratio'] = cum15psma['meanreturn'] / cum15psma['volatility']


cum20psma = cum20psma[cum20psma['n_day_ahead'].isin([1, 2, 3])]
cum20psma = cum20psma[['n_day_ahead', 'log_factor_return']]
cum20psma = cum20psma.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum20psma.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum20psma['volatility'] = volatility_series
mean_series = cum20psma.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum20psma['meanreturn'] = mean_series
cum20psma['factor investment'] = 'psma_20'
cum20psma = cum20psma[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum20psma = cum20psma.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum20psma['information_ratio'] = cum20psma['meanreturn'] / cum20psma['volatility']


cum25psma = cum25psma[cum25psma['n_day_ahead'].isin([1, 2, 3])]
cum25psma = cum25psma[['n_day_ahead', 'log_factor_return']]
cum25psma = cum25psma.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum25psma.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum25psma['volatility'] = volatility_series
mean_series = cum25psma.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum25psma['meanreturn'] = mean_series
cum25psma['factor investment'] = 'psma_25'
cum25psma = cum25psma[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum25psma = cum25psma.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum25psma['information_ratio'] = cum25psma['meanreturn'] / cum25psma['volatility']


cum30psma = cum30psma[cum30psma['n_day_ahead'].isin([1, 2, 3])]
cum30psma = cum30psma[['n_day_ahead', 'log_factor_return']]
cum30psma = cum30psma.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cum30psma.groupby('n_day_ahead')['log_factor_return'].transform('std')
cum30psma['volatility'] = volatility_series
mean_series = cum30psma.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cum30psma['meanreturn'] = mean_series
cum30psma['factor investment'] = 'psma_30'
cum30psma = cum30psma[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cum30psma = cum30psma.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cum30psma['information_ratio'] = cum30psma['meanreturn'] / cum30psma['volatility']


cumrrp_15 = cumrrp_15[cumrrp_15['n_day_ahead'].isin([1, 2, 3])]
cumrrp_15 = cumrrp_15[['n_day_ahead', 'log_factor_return']]
cumrrp_15 = cumrrp_15.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumrrp_15.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumrrp_15['volatility'] = volatility_series
mean_series = cumrrp_15.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumrrp_15['meanreturn'] = mean_series
cumrrp_15['factor investment'] = 'rrp_15'
cumrrp_15 = cumrrp_15[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumrrp_15 = cumrrp_15.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumrrp_15['information_ratio'] = cumrrp_15['meanreturn'] / cumrrp_15['volatility']


cumrrp_20 = cumrrp_20[cumrrp_20['n_day_ahead'].isin([1, 2, 3])]
cumrrp_20 = cumrrp_20[['n_day_ahead', 'log_factor_return']]
cumrrp_20 = cumrrp_20.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumrrp_20.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumrrp_20['volatility'] = volatility_series
mean_series = cumrrp_20.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumrrp_20['meanreturn'] = mean_series
cumrrp_20['factor investment'] = 'rrp_20'
cumrrp_20 = cumrrp_20[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumrrp_20 = cumrrp_20.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumrrp_20['information_ratio'] = cumrrp_20['meanreturn'] / cumrrp_20['volatility']


cumrrp_25 = cumrrp_25[cumrrp_25['n_day_ahead'].isin([1, 2, 3])]
cumrrp_25 = cumrrp_25[['n_day_ahead', 'log_factor_return']]
cumrrp_25 = cumrrp_25.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumrrp_25.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumrrp_25['volatility'] = volatility_series
mean_series = cumrrp_25.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumrrp_25['meanreturn'] = mean_series
cumrrp_25['factor investment'] = 'rrp_25'
cumrrp_25 = cumrrp_25[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumrrp_25 = cumrrp_25.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumrrp_25['information_ratio'] = cumrrp_25['meanreturn'] / cumrrp_25['volatility']

cumrrp_30 = cumrrp_30[cumrrp_30['n_day_ahead'].isin([1, 2, 3])]
cumrrp_30 = cumrrp_30[['n_day_ahead', 'log_factor_return']]
cumrrp_30 = cumrrp_30.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumrrp_30.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumrrp_30['volatility'] = volatility_series
mean_series = cumrrp_30.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumrrp_30['meanreturn'] = mean_series
cumrrp_30['factor investment'] = 'rrp_30'
cumrrp_30 = cumrrp_30[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumrrp_30 = cumrrp_30.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumrrp_30['information_ratio'] = cumrrp_30['meanreturn'] / cumrrp_30['volatility']


cumsmaf_2_20 = cumsmaf_2_20[cumsmaf_2_20['n_day_ahead'].isin([1, 2, 3])]
cumsmaf_2_20 = cumsmaf_2_20[['n_day_ahead', 'log_factor_return']]
cumsmaf_2_20 = cumsmaf_2_20.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumsmaf_2_20.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumsmaf_2_20['volatility'] = volatility_series
mean_series = cumsmaf_2_20.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumsmaf_2_20['meanreturn'] = mean_series
cumsmaf_2_20['factor investment'] = 'smaf_2_20'
cumsmaf_2_20 = cumsmaf_2_20[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumsmaf_2_20 = cumsmaf_2_20.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumsmaf_2_20['information_ratio'] = cumsmaf_2_20['meanreturn'] / cumsmaf_2_20['volatility']


cumsmaf_3_20 = cumsmaf_3_20[cumsmaf_3_20['n_day_ahead'].isin([1, 2, 3])]
cumsmaf_3_20 = cumsmaf_3_20[['n_day_ahead', 'log_factor_return']]
cumsmaf_3_20 = cumsmaf_3_20.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumsmaf_3_20.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumsmaf_3_20['volatility'] = volatility_series
mean_series = cumsmaf_3_20.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumsmaf_3_20['meanreturn'] = mean_series
cumsmaf_3_20['factor investment'] = 'smaf_3_20'
cumsmaf_3_20 = cumsmaf_3_20[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumsmaf_3_20 = cumsmaf_3_20.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumsmaf_3_20['information_ratio'] = cumsmaf_3_20['meanreturn'] / cumsmaf_3_20['volatility']


cumsmaf_3_25 = cumsmaf_3_25[cumsmaf_3_25['n_day_ahead'].isin([1, 2, 3])]
cumsmaf_3_25 = cumsmaf_3_25[['n_day_ahead', 'log_factor_return']]
cumsmaf_3_25 = cumsmaf_3_25.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumsmaf_3_25.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumsmaf_3_25['volatility'] = volatility_series
mean_series = cumsmaf_3_25.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumsmaf_3_25['meanreturn'] = mean_series
cumsmaf_3_25['factor investment'] = 'smaf_3_25'
cumsmaf_3_25 = cumsmaf_3_25[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumsmaf_3_25 = cumsmaf_3_25.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumsmaf_3_25['information_ratio'] = cumsmaf_3_25['meanreturn'] / cumsmaf_3_25['volatility']

cumsmaf_5_30 = cumsmaf_5_30[cumsmaf_5_30['n_day_ahead'].isin([1, 2, 3])]
cumsmaf_5_30 = cumsmaf_5_30[['n_day_ahead', 'log_factor_return']]
cumsmaf_5_30 = cumsmaf_5_30.drop_duplicates(subset=['n_day_ahead', 'log_factor_return'])
volatility_series = cumsmaf_5_30.groupby('n_day_ahead')['log_factor_return'].transform('std')
cumsmaf_5_30['volatility'] = volatility_series
mean_series = cumsmaf_5_30.groupby('n_day_ahead')['log_factor_return'].transform('mean')
cumsmaf_5_30['meanreturn'] = mean_series
cumsmaf_5_30['factor investment'] = 'smaf_5_30'
cumsmaf_5_30 = cumsmaf_5_30[['factor investment', 'n_day_ahead', 'meanreturn', 'volatility']]
cumsmaf_5_30 = cumsmaf_5_30.drop_duplicates(subset=['n_day_ahead', 'volatility'])
cumsmaf_5_30['information_ratio'] = cumsmaf_5_30['meanreturn'] / cumsmaf_5_30['volatility']


dataframes = [cum10mom, cum15mom, cum20mom, cum25mom, cum15psma, cum20psma, cum25psma, cum30psma, cumrrp_15, cumrrp_20, cumrrp_25, cumrrp_30, cumsmaf_2_20, cumsmaf_3_20, cumsmaf_3_25, cumsmaf_5_30]
combined_df = pd.concat(dataframes, ignore_index=True)
print(combined_df)


st.markdown('### Volatility and Information Ratio')

st.markdown('----')
st.markdown('# Volatility')
st.markdown('The higher the volatility, the greater the risk.')

st.markdown('----')
st.markdown('# Information Ratio')
st.markdown('Information ratio is directly proportional to returns and inversely proportional to volatility.')


st.dataframe(combined_df)
