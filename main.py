'''
主模块，用于启动和管理交易系统。
'''
from trading_bot import TradingBot
import time


def main():
    bot = TradingBot()
    print("交易机器人已启动")
    bot.run()
    while True:
        # 等待10秒
        time.sleep(10)
        bot.run()


if __name__ == "__main__":
    main()