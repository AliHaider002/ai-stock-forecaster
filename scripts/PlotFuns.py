from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from AlphaFuns import AlphaFuns

alp = AlphaFuns()

class PlotFuns:
    def __init__(self, data, tickers):
        self.tickers = tickers
        self.data = data
        
    def plot_stocks(self):
        fig,ax = plt.subplots(figsize=(15,6), dpi=200)
        for ticker in self.tickers:
            self.data[ticker]["adj close"].plot(ax=ax, label=ticker)
        plt.xlabel("Date")
        plt.ylabel("Close")
        plt.title("Stocks Adjust Close Graph")
        plt.legend()
        return fig
    
    def invested_shares_plot(self, amount, start_date, end_date):
        fig,ax = plt.subplots(figsize=(15,6), dpi=200)
        invest_data = []
        for index , df in self.data.items():
            df = df[df.index >= pd.to_datetime(start_date)]
            df = df[df.index <= pd.to_datetime(end_date)]
            ret = df["adj close"].pct_change(1).dropna()
            cum_ret = (ret+1).cumprod()
            result = cum_ret * amount
            data = {
                "amount" : amount,
                "ticker" : index,
                "start_date" : pd.to_datetime(start_date).isoformat(),
                "end_date" : pd.to_datetime(end_date).isoformat(),
                "result" : np.round(result.iloc[-1], 2),
                "shares" : np.round(amount/df["adj close"].iloc[-1]),
                "shape_ratio" : alp.compute_sharp_ratio(df),
                "message" : f"{amount}$ Amount Investment in {index} will be resulted: {np.round(result.iloc[-1], 2)}"
            } 
            invest_data.append(data)
            result.plot(ax=ax, label=index)
        plt.xlabel("Date")
        plt.ylabel("Result")
        plt.title(f"{amount}$ Investment in {self.tickers} Result Graph")
        plt.legend()
        return invest_data
    
    def bollinger_bands_plot(self):
        for index, df in self.data.items():
            fig, ax = plt.subplots(figsize=(15,7), dpi=200)
            df["MA"] = df["adj close"].rolling(window=20).mean()
            df["STD"] = df["adj close"].rolling(window=20).std()
            df["BOL_LOWER"] = df["MA"] - 2*df["STD"]
            df["BOL_UPPER"] = df["MA"] + 2*df["STD"]
            df[["adj close", "BOL_LOWER", "BOL_UPPER"]].plot(ax=ax, label=index)
            plt.xlabel("Date")
            plt.ylabel("bands")
            plt.title(f"{index} Lower and Upper Bollinger Bands")
            plt.legend()
        return fig