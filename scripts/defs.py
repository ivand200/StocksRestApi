import json
import csv
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import yfinance as yf
import math

now = datetime.now()
lastmonth = now - timedelta(weeks=5)
end_of_last_month = (lastmonth.replace(day=28)).strftime("%Y-%m-%d")
start_time = (now - timedelta(weeks=120)).strftime("%Y-%m-%d")


# create a class with static method for DJ30 and SP500 update
# P/E, E(4 year avg)/P, Momentum_12_2, avg_momentum, ma10, div(avg 5 year)/P

class Ep:

    @staticmethod
    def get_ep(ticker):
        """
        Calculate E/P ratio, average income for last 4 years / last price
        """
        try:
            stock = yf.Ticker(ticker)
            avg_income = (stock.earnings["Earnings"].sum())/4
            shares_outstanding = int(stock.info["sharesOutstanding"])
            price = float(stock.info["currentPrice"])
            ratio = round(((avg_income / shares_outstanding) / price), 4)
        except:
            return 0.0
        else:
            return ratio


class Pe:

    @staticmethod
    def pe(ticker):
        """
        Trailing P/E
        """
        try:
            stock = yf.Ticker(ticker)
            result = stock.info["trailingPE"]
        except:
            return 0.0
        else:
            return result


class Div_p:

    @staticmethod
    def get_div_p(ticker):
        """
        Average dividends for last 5 years / price
        """
        try:
            stock = yf.Ticker(ticker)
            avg_dividends = (stock.dividends[-20:].mean() * 4)
            avg_div = round((avg_dividends / float(stock.info["currentPrice"])), 3)
            if math.isnan(avg_div):
                avg_div = 0.0
        except:
            return 0.0
        else:
            return avg_div


class Ma10:

    @staticmethod
    def get_ma10(ticker):
        """
        1 if price higher than ma10, else 0
        """
        try:
            stock = yf.Ticker(ticker)
            stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
            stock = stock.dropna()
            stock["MA10"] = stock["Close"].rolling(10).mean()
            stock["Difference"] = (stock["Close"] / stock["MA10"]) - 1
            stock["Direction"] = [1 if stock.loc[ei, "Difference"] > 0 else 0 for ei in stock.index]
            result = int(stock["Direction"][-1])
        except:
            return 0
        else:
            return result


class Momentum_12_1:

    @staticmethod
    def get_momentum_12_1(ticker):
        """
        Momentum_12_1
        """
        try:
            stock = yf.Ticker(ticker)
            stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
            stock = stock.dropna()
            stock["Price0"] = stock["Close"].shift(12)
            stock["Price1"] = stock["Close"]
            stock["mom_12_1"] = (stock["Price1"] / stock["Price0"]) - 1
            result = round(stock["mom_12_1"][-1], 2)
        except:
            return 0.0
        else:
            return result


class Momentum_3:

    @staticmethod
    def get_momentum_3(ticker):
        """
        Momentum_3
        """
        try:
            stock = yf.Ticker(ticker)
            stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
            stock = stock.dropna()
            stock["Price0"] = stock["Close"].shift(3)
            stock["Price1"] = stock["Close"]
            stock["mom_12_1"] = (stock["Price1"] / stock["Price0"]) - 1
            result = round(stock["mom_12_1"][-1], 2)
        except:
            return 0.0
        else:
            return result


class Momentum_12_2:

    @staticmethod
    def get_momentum_12_2(ticker):
        """
        Momentum_12_2
        """
        try:
            stock = yf.Ticker(ticker)
            stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
            stock = stock.dropna()
            stock["Price0"] = stock["Close"].shift(12)
            stock["Price1"] = stock["Close"].shift(1)
            stock["mom_12_2"] = (stock["Price1"] / stock["Price0"]) - 1
            result = round(stock["mom_12_2"][-1], 2)
            if math.isnan(result):
                result = 0.0
        except:
            return 0.0
        else:
            return result


class Avg_Momentum:

    @staticmethod
    def get_avg_momentum(ticker):
        """
        Average momentum
        """
        try:
            stock = yf.Ticker(ticker)
            stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
            stock = stock.dropna()
            stock["Close0"] = stock["Close"].shift(12)
            stock["Close1"] = stock["Close"].shift(6)
            stock["Close2"] = stock["Close"].shift(3)
            stock["Mom_12"] = ((stock["Close"] / stock["Close0"]) - 1)
            stock["Mom_6"] = ((stock["Close"] / stock["Close1"]) - 1)
            stock["Mom_3"] = ((stock["Close"] / stock["Close2"]) - 1)
            stock["Avg_Mom"] = (stock["Mom_12"] + stock["Mom_6"] + stock["Mom_3"]) / 3
            result = stock["Avg_Mom"][-1].round(2)
            if math.isnan(result):
                result = 0.0
        except:
            return 0.0
        else:
            return result
print(Avg_Momentum.get_avg_momentum("OGN"))
print(Avg_Momentum.get_avg_momentum("OKE"))
class Low_range:

    def get_low_range(ticker):
        """
        1 if price at 5th year low, else 0
        """
        stock = yf.Ticker(ticker)
        stock = stock.history(start=start_time, end=end_of_last_month, interval="1mo")
        stock = stock.dropna()
        stock_low = stock["Close"][-60:].min().round(2)
        stock_i = [1 if stock["Close"][-1] <= (stock_low * 1.2) else 0]
        return stock_i[0]
