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
cumdsh_15 = pd.read_csv('cumdsh_15.csv')
cumdsh_20 = pd.read_csv('cumdsh_20.csv')
cumdsh_25 = pd.read_csv('cumdsh_25.csv')
cumdsh_30 = pd.read_csv('cumdsh_30.csv')
cumrrp_15 = pd.read_csv('cumrrp_15.csv')
cumrrp_20 = pd.read_csv('cumrrp_20.csv')
cumrrp_25 = pd.read_csv('cumrrp_25.csv')
cumrrp_30 = pd.read_csv('cumrrp_30.csv')
cumsmaf_2_20 = pd.read_csv('cumsmaf_2_20.csv')
cumsmaf_3_20 = pd.read_csv('cumsmaf_3_20.csv')
cumsmaf_3_25 = pd.read_csv('cumsmaf_3_25.csv')
cumsmaf_5_30 = pd.read_csv('cumsmaf_5_30.csv')


# Lọc các ngày để hiển thị nhãn trục x
def get_year_start_dates(dates):
    year_start_dates = [date for date in dates if date.endswith('01-01')]
    return year_start_dates

# Tạo đồ thị
fig, ax = plt.subplots()
for n_day_ahead, group_data in cum10mom.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 10mom')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum10mom['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum15mom.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 15mom')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum15mom['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum20mom.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 20mom')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum20mom['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum25mom.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 25mom')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum25mom['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum15psma.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 15psma')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum15psma['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum20psma.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 20psma')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum20psma['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum25psma.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 25psma')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum25psma['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cum30psma.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 30psma')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cum30psma['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)


fig, ax = plt.subplots()
for n_day_ahead, group_data in cumdsh_15.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 15dsh')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumdsh_15['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cumdsh_20.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 20dsh')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumdsh_20['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)
fig, ax = plt.subplots()
for n_day_ahead, group_data in cumdsh_25.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 25dsh')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumdsh_25['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)
fig, ax = plt.subplots()
for n_day_ahead, group_data in cumdsh_30.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of 30dsh')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumdsh_30['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)


fig, ax = plt.subplots()
for n_day_ahead, group_data in cumrrp_15.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of rrp_15')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumrrp_15['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)


fig, ax = plt.subplots()
for n_day_ahead, group_data in cumrrp_20.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of rrp_20')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumrrp_20['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)
fig, ax = plt.subplots()
for n_day_ahead, group_data in cumrrp_25.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of rrp_25')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumrrp_25['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cumrrp_30.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of rrp_30')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumrrp_30['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cumsmaf_2_20.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of smaf_2_20')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumsmaf_2_20['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
for n_day_ahead, group_data in cumsmaf_2_20.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of smaf_2_20')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumsmaf_2_20['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)


fig, ax = plt.subplots()
for n_day_ahead, group_data in cumsmaf_3_20.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of smaf_3_20')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumsmaf_3_20['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)


fig, ax = plt.subplots()
for n_day_ahead, group_data in cumsmaf_3_25.groupby('n_day_ahead'):
    ax.plot(group_data['date'], group_data['cumreturn'], label=f'n_day_ahead={n_day_ahead}')
# Thiết lập tiêu đề và nhãn trục
ax.set_title('Top 10 coins by market cap weighted in proportion to rank of smaf_3_25')
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative Return')
# Lấy các ngày cần hiển thị trên trục x
x_ticks_values = get_year_start_dates(cumsmaf_3_25['date'])
# Thiết lập nhãn trục x chỉ hiển thị các ngày cần thiết
ax.set_xticks(x_ticks_values)
ax.set_xticklabels(x_ticks_values, rotation=45, ha='right')
# Thêm chú thích
ax.legend()
# Hiển thị đồ thị bằng Streamlit
st.pyplot(fig)

plt.clf()
long_df = pd.read_csv('long_df.csv')

# Vẽ biểu đồ sử dụng matplotlib
plt.plot(long_df[long_df['gap']=='gap_0']['date'], long_df[long_df['gap']=='gap_0']['cumreturn'], color='blue', label='gap_0')
plt.plot(long_df[long_df['gap']=='gap_1']['date'], long_df[long_df['gap']=='gap_1']['cumreturn'], color='green', label='gap_1')
plt.plot(long_df[long_df['gap']=='gap_2']['date'], long_df[long_df['gap']=='gap_2']['cumreturn'], color='red', label='gap_2')

plt.title('Cumulative Returns Long/Short MegaFactor')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()

st.pyplot()