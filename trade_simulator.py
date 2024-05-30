'''
Module for simulating trades.
'''
class TradeSimulator:
    def execute_trade(self, price, signal):
        if signal == 'buy':
            return {'type': 'buy', 'price': price, 'quantity': 1}
        elif signal == 'sell':
            return {'type': 'sell', 'price': price, 'quantity': 1}
        return None