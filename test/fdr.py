import FinanceDataReader as fdr

# Apple(AAPL), 2017-01-01 ~ Now
df = fdr.DataReader('AAPL', '2017')

# AMAZON(AMZN), 2017
df = fdr.DataReader('AMZN', '2017-01-01', '2017-12-31')

# Samsung(005930), 1992-01-01 ~ 2018-10-31
df = fdr.DataReader('068270', '1992-01-01', '2018-10-31')

# country code: ex) 000150: Doosan(KR), Yihua Healthcare(CN)
df = fdr.DataReader('000150', '2018-01-01', '2018-10-30') # default: 'KR' 
df = fdr.DataReader('000150', '2018-01-01', '2018-10-30', country='KR')
df = fdr.DataReader('000150', '2018-01-01', '2018-10-30', country='CN')

# KOSPI index, 2015~Now
df = fdr.DataReader('KS11', '2015-01-01')

# Dow Jones Industrial(DJI), 2015년~Now
df = fdr.DataReader('DJI', '2015-01-01')

# USD/KRW, 1995~Now
df = fdr.DataReader('USD/KRW', '1995-01-01')

# Bitcoin KRW price (Bithumbs), 2016 ~ Now
df = fdr.DataReader('BTC/KRW', '2016-01-01')

# KRX stock symbol list and names
df_krx = fdr.StockListing('KRX')
print('type(df_krx): ' + str(type(df_krx)))
print('df_krx.shape: ' + str(df_krx.shape))
print(df_krx.head())

# S&P 500 symbol list
df_spx = fdr.StockListing('S&P500')
print('type(df_spx): ' + str(type(df_spx)))
print('df_spx.shape: ' + str(df_spx.shape))
print(df_spx.head())
