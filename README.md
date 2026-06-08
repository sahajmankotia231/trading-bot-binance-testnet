# Binance Futures Testnet Trading Bot

## Overview

This project is a Python CLI application that places MARKET and LIMIT orders on Binance Futures Demo/Testnet.

## Features

* BUY and SELL orders
* MARKET and LIMIT order support
* CLI-based user input
* Input validation
* Logging of API requests and responses
* Error handling
* Environment variable configuration

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Test Connection

```bash
python test_connection.py
```

## Run Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

## Assumptions

* Binance Futures Demo/Testnet account is available.
* API credentials are valid.
* Internet connection is available.
