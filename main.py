'''
主模块，用于启动和管理交易系统。
'''
from trading_bot import TradingBot
def main():
    bot = TradingBot()
    bot.run()
if __name__ == "__main__":
    main()