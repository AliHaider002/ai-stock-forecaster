from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

class AlphaFuns:
    def __init__(
        self,
        tickers,
    ):
        self.tickers = tickers

    def wrangle(self):
        today = date.today()
        end_date = pd.to_datetime(today)
        start_date = end_date - pd.DateOffset(252 * 10)
        data = {}
        for ticker in self.tickers:
            df = yf.download(ticker, start=start_date, end=end_date)
            df.index.name = "date"
            df.columns = df.columns.str.lower()
            data[ticker] = df
        self.data = data
        return data

    def perc_calc(self, start_date, end_date):
        perc_data = {}
        for ticker in self.tickers:
            if start_date not in self.data[ticker]["adj close"].index:
                print(f"This Start Date is not available in {ticker} data.")
            if end_date not in self.data[ticker]["adj close"].index:
                print(f"This End Date is not available in {ticker} data.")
    
            adj_close_start = self.data[ticker]["adj close"][start_date]
            adj_close_end = self.data[ticker]["adj close"][end_date]
            perc = 100*(adj_close_end - adj_close_start)/adj_close_start
            perc_data[ticker] = f"Percent Change: {np.round(perc, 2)}"
        return perc_data