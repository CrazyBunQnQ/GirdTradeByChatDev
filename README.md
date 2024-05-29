下面是一个为 CrazyCodeLab Binance 自动交易软件准备的使用手册。这个手册旨在详细介绍软件的主要功能、环境安装步骤以及如何使用该软件。

```markdown
# CrazyCodeLab Binance Auto-Trading Bot

自动交易 Binance 平台上的 BNBUSDT 对，依据指数移动平均线和相对强弱指数来生成交易信号。

## 功能概述

- **自动交易**：使用 Binance API 完成自动买卖操作。
- **市场数据监测**：实时监测市场数据，根据设定的策略进行交易。
- **风险管理**：通过设置交易参数（如止损、止盈）来管理风险。
- **日志记录**：所有交易动作和重要信息都会记录在日志文件中，便于回溯和分析。

## 快速安装

首先，确保您的系统已安装 Python 3.7 或更高版本。然后，按照以下步骤设置您的交易环境：

### 1. 安装 Python 依赖

在终端中运行以下命令来安装所需的 Python 库：

```bash
pip install requests pandas
```

### 2. 配置 API 密钥

您需要在 Binance 平台上生成 API 密钥和密钥秘密，然后将它们添加到您的环境变量中：

- **Windows 用户**:
  - 打开命令行，输入：
    ```bash
    set BINANCE_API_KEY=您的API键
    set BINANCE_API_SECRET=您的API密钥秘密
    ```
- **Unix/Mac 用户**:
  - 打开终端，输入：
    ```bash
    export BINANCE_API_KEY=您的API键
    export BINANCE_API_SECRET=您的API密钥秘密
    ```

## 使用说明

### 启动交易机器人

运行主脚本开始自动交易：

```bash
python main.py
```

软件将自动开始监测市场，并根据预定的交易策略执行买卖操作。所有相关活动和输出信息将通过日志系统记录并显示在控制台上。

## 📖 文档

- **配置指南**：详细说明如何配置和优化您的交易策略。
- **常见问题解答 (FAQ)**：提供关于使用本软件和解决常见问题的指南。

感谢您选择 CrazyCodeLab 的产品，希望您交易顺利！
```

请确保遵循安装和配置指南正确设置环境，并理解交易策略以优化交易结果。