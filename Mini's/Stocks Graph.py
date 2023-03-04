import matplotlib.pyplot as plt
import pandas as pd   
from matplotlib import style 
import mplcursors as mpc
df = pd.read_excel('StocksData.xlsx')

dates = []
data  = []
cumm = 0
for index,row in df.iterrows():
    if(not str(row['Trade to Wallet'])=='nan'):
        dates.append(row.Date.date())
        data.append(cumm+row['Trade to Wallet'])
        cumm = cumm+row['Trade to Wallet']

print(data)
plt.style.use('seaborn-v0_8')
plt.plot(dates, data, marker='o')
  
# naming the x axis
plt.xlabel('Dates')
# naming the y axis
plt.ylabel('Change')
  
# giving a title to my graph
plt.title('My Stocks Journey!')
# function to show the plot
plt.show()
