'''
Main module for automated trading simulation using Binance API for BNBUSDT.
'''
import json
from binance_api import BinanceAPI
from trading_strategy import TradingStrategy
from trade_simulator import TradeSimulator
from statistics_tracker import StatisticsTracker
def main():
    # Initialize API and other components
    # Binance API 密钥
    with open('/training/binanceKeys.json', 'r') as f:
        config = json.load(f)
    api_key = config['binance_api_key']
    api_secret = config['binance_api_secret']
    api = BinanceAPI(api_key=api_key, api_secret=api_secret)
    strategy = TradingStrategy(api)
    simulator = TradeSimulator()
    tracker = StatisticsTracker()
    # Get current data and update indicators
    klines = api.fetch_klines("BNBUSDT", "4h")
    strategy.update_indicators(klines)
    # Check for trade signals
    signal = strategy.check_signals()
    if signal:
        # Simulate trade based on the current price and signal
        trade_result = simulator.execute_trade(api.get_current_price("BNBUSDT"), signal)
        tracker.record_trade(trade_result)
    # Print statistics
    tracker.print_statistics()
if __name__ == '__main__':
    main()