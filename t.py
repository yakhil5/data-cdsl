import pandas as pd
data=pd.read_csv('data.csv',index_col='SYMBOL')
s=input("Input Symbol : ")
x=data.at[s,' ISIN NUMBER']
url="https://www.cdslindia.com/investors/popup-isin.aspx?isin_code="+x
info=pd.read_html(url,index_col=0)
print(info)