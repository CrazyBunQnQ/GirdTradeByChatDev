'''
交易机器人模块，包含获取市场数据，计算技术指标和执行模拟交易的功能。
'''
import json
import pandas as pd
import requests
from binance.client import Client
from trade_logger import TradeLogger
class TradingBot:
    def __init__(self):
        # 加载配置
        with open('/training/binanceKeys.json', 'r') as f:
            config = json.load(f)
        self.client = Client(config['binance_api_key'], config['binance_api_secret'])
        self.logger = TradeLogger()
        self.message_url = "https://crazynft.top:3033/push/root"
        self.message_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    def fetch_data(self):
        # 获取BNBUSDT的4小时K线数据
        klines = self.client.get_klines(symbol='BNBUSDT', interval=Client.KLINE_INTERVAL_4HOUR)
        df = pd.DataFrame(klines, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['close'] = pd.to_numeric(df['close'])
        return df
    def calculate_ema(self, df, span):
        # 计算指数移动平均线
        return df['close'].ewm(span=span, adjust=False).mean()
    def calculate_rsi(self, df, period=14):
        # 计算相对强弱指数 (RSI)
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).ewm(com=(period - 1), min_periods=period).mean()
        loss = (-delta.where(delta < 0, 0)).ewm(com=(period - 1), min_periods=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    def run(self):
        df = self.fetch_data()
        ema_short = self.calculate_ema(df, 12)
        ema_long = self.calculate_ema(df, 26)
        rsi = self.calculate_rsi(df)
        df['ema12'] = ema_short
        df['ema26'] = ema_long
        df['rsi'] = rsi
        df['signal'] = 0
        df.loc[df['ema12'] > df['ema26'], 'signal'] = 1  # 买入信号
        df.loc[df['ema12'] < df['ema26'], 'signal'] = -1  # 卖出信号
        message = {}
        # 模拟交易逻辑
        for index, row in df.iterrows():
            if row['signal'] == 1 and row['rsi'] < 30:
                # 买入逻辑，检查RSI超卖
                self.logger.log_trade({'type': 'buy', 'price': row['close'], 'amount': 1, 'total': row['close'], 'ema12': row['ema12'], 'ema26': row['ema26'], 'rsi': row['rsi'], 'balance': 1000 - row['close']})
                message = {
                    "title": "模拟购买",
                    "description": "description",
                    "content": "价格: " + row['close'],
                    "channel": "workchat_baba",
                    "token": "7ftMW2HpggTq"
                }
                try:
                    requests.post(self.message_url, headers=self.message_headers, json=message)
                except Exception as e:
                    print(e)
            elif row['signal'] == -1 and row['rsi'] > 70:
                # 卖出逻辑，检查RSI超买
                self.logger.log_trade({'type': 'sell', 'price': row['close'], 'amount': 1, 'total': row['close'], 'ema12': row['ema12'], 'ema26': row['ema26'], 'rsi': row['rsi'], 'balance': 1000 + row['close']})
                message = {
                    "title": "模拟卖出",
                    "description": "description",
                    "content": "价格: " + row['close'],
                    "channel": "workchat_baba",
                    "token": "7ftMW2HpggTq"
                }
            try:
                requests.post(self.message_url, headers=self.message_headers, json=message)
            except Exception as e:
                print(e)
        self.logger.print_statistics()