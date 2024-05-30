'''
Module for managing trading strategies and indicators.
'''
import pandas as pd
import numpy as np
class TradingStrategy:
    def __init__(self, api):
        self.api = api
        self.last_ema_short = None
        self.last_ema_long = None
        self.rsi_period = 14
        self.rsi_overbought = 70
        self.rsi_oversold = 30
    def calculate_rsi(self, closing_prices):
        delta = closing_prices.diff()
        gains = (delta.where(delta > 0, 0)).fillna(0)
        losses = (-delta.where(delta < 0, 0)).fillna(0)
        avg_gain = gains.rolling(window=self.rsi_period, min_periods=self.rsi_period).mean()
        avg_loss = losses.rolling(window=self.rsi_period, min_periods=self.rsi_period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]
    def update_indicators(self, klines):
        closing_prices = pd.Series([float(kline[4]) for kline in klines])
        self.last_ema_short = closing_prices.ewm(span=7, adjust=False).mean().iloc[-1]
        self.last_ema_long = closing_prices.ewm(span=25, adjust=False).mean().iloc[-1]
        self.last_rsi = self.calculate_rsi(closing_prices)
    def check_signals(self):
        if self.last_ema_short > self.last_ema_long and self.last_rsi < self.rsi_oversold:
            return 'buy'
        elif self.last_ema_short < self.last_ema_long and self.last_rsi > self.rsi_overbought:
            return 'sell'
        return None