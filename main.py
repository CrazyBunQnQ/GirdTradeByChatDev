'''
Main script for Binance auto-trading bot. This script handles initialization and starts the trading process.
'''
import os
import logging
from trading_strategy import TradingStrategy
from binance_api import BinanceAPI
def setup_logging():
    """Setup basic logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def main():
    """Main function to execute the trading bot."""
    setup_logging()
    logging.info("Starting Binance trading bot")
    api_key = os.getenv('BINANCE_API_KEY')  # Get API key from environment variables
    api_secret = os.getenv('BINANCE_API_SECRET')  # Get API secret from environment variables
    if not api_key or not api_secret:
        logging.error("API credentials are not set in the environment variables.")
        return
    api = BinanceAPI(api_key, api_secret)
    strategy = TradingStrategy(api)
    try:
        strategy.run_trading_loop()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Trading bot has stopped")
if __name__ == '__main__':
    main()