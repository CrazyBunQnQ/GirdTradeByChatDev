'''
Module for tracking statistics of trades.
'''
class StatisticsTracker:
    def __init__(self):
        self.trades = []
        self.balance = 1000  # Example starting balance
    def record_trade(self, trade):
        if trade is not None:
            self.trades.append(trade)
            if trade['type'] == 'buy':
                self.balance -= trade['price'] * trade['quantity']
            elif trade['type'] == 'sell':
                self.balance += trade['price'] * trade['quantity']
    def print_statistics(self):
        profit_loss = self.balance - 1000
        print(f"Balance: {self.balance}, Trades: {len(self.trades)}, P/L: {profit_loss}")