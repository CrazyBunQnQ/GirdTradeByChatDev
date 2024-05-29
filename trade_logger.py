'''
交易记录模块，用于记录所有模拟交易和生成交易统计信息。
'''
import csv
import os
from datetime import datetime
class TradeLogger:
    def __init__(self):
        # 确保存储文件的文件夹存在
        self.file_name = 'trades.csv'
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                # 写入文件头
                writer.writerow(['timestamp', 'type', 'price', 'amount', 'total', 'ema12', 'ema26', 'rsi', 'balance'])
    def log_trade(self, trade):
        # 将交易记录到CSV文件
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                trade['type'],
                trade['price'],
                trade['amount'],
                trade['total'],
                trade['ema12'],
                trade['ema26'],
                trade['rsi'],
                trade['balance']
            ])
    def print_statistics(self):
        # 从CSV读取数据并打印交易统计信息
        with open(self.file_name, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # 跳过头部
            trades = list(reader)
            if not trades:
                print("No trades to analyze.")
                return
            total_profit = sum(float(trade[4]) for trade in trades)
            total_trades = len(trades)
            print(f'Total Trades: {total_trades}, Total Profit: {total_profit:.2f}')