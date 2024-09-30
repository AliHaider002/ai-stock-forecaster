#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install Cython fbprophet')


# In[8]:


from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from fbprophet import Prophet
from AlphaFuns import AlphaFuns
from PlotFuns import PlotFuns


# In[3]:


tickers = ["AAPL", "MSFT"]
alp = AlphaFuns(tickers = tickers)
data = alp.wrangle()
plot = PlotFuns(tickers=tickers, data=data)


# In[4]:


fig = plot.plot_stocks()


# In[5]:


percent_calc = alp.perc_calc(start_date="2017-10-13", end_date="2018-10-17")


# In[6]:


today = date.today()
end_date = pd.to_datetime(today)
start_date = end_date - pd.DateOffset(252 * 10)
invest = plot.invested_shares_plot(amount=10000, start_date=start_date, end_date=end_date)


# In[7]:


fig = plot.bollinger_bands_plot()


# In[ ]:




