Steps to reproduce:
1. Run `docker compose up`
2. You can use already downloaded data or run `docker compose run freqtrade_dev2 freqtrade download-data --timerange=20230101-20250707`
3. Run `docker compose run freqtrade_dev2 freqtrade backtesting --config /freqtrade/user_data/config.json --strategy MyStrategy --timerange=20240101-20250707`
4. You will get a lot of errors like 
```aiignore
\PycharmProjects\freqtrade_problem> docker compose run freqtrade_dev2 freqtrade backtesting --config /freqtrade/user_data/config.json --strategy MyStrategy --timerange=20240101-20250707  
2025-08-01 18:18:24,216 - freqtrade - INFO - freqtrade docker-2025.6-dev-9f5fd574
2025-08-01 18:18:28,600 - numexpr.utils - INFO - NumExpr defaulting to 16 threads.
2025-08-01 18:18:31,061 - freqtrade.configuration.load_config - INFO - Using config: /freqtrade/user_data/config.json ...
2025-08-01 18:18:31,070 - freqtrade.loggers - INFO - Enabling colorized output.
2025-08-01 18:18:31,071 - root - INFO - Logfile configured
2025-08-01 18:18:31,072 - freqtrade.loggers - INFO - Verbosity set to 0
2025-08-01 18:18:31,073 - freqtrade.configuration.configuration - INFO - Using max_open_trades: 10 ...
2025-08-01 18:18:31,073 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20240101-20250707 ...
2025-08-01 18:18:31,166 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2025-08-01 18:18:31,169 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/gateio ...
2025-08-01 18:18:31,170 - freqtrade.configuration.configuration - INFO - Parameter --cache=day detected ...
2025-08-01 18:18:31,170 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20240101-20250707
2025-08-01 18:18:31,172 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2025-08-01 18:18:31,184 - freqtrade.exchange.check_exchange - INFO - Exchange "gateio" is officially supported by the Freqtrade development team.
2025-08-01 18:18:31,185 - freqtrade.configuration.configuration - INFO - Using pairlist from configuration.
2025-08-01 18:18:31,186 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-08-01 18:18:31,190 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2025-08-01 18:18:31,191 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2025-08-01 18:18:31,191 - freqtrade.exchange.exchange - INFO - Using CCXT 4.4.90
2025-08-01 18:18:31,192 - freqtrade.exchange.exchange - INFO - Applying additional ccxt config: {'options': {'defaultType': 'swap'}}
2025-08-01 18:18:31,203 - freqtrade.exchange.exchange - INFO - Applying additional ccxt config: {'options': {'defaultType': 'swap'}}
2025-08-01 18:18:31,216 - freqtrade.exchange.exchange - INFO - Using Exchange "Gate.io"
2025-08-01 18:18:43,612 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Gate'...
/home/ftuser/.local/lib/python3.13/site-packages/pandas_ta/__init__.py:6: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import get_distribution, DistributionNotFound
2025-08-01 18:18:43,875 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy MyStrategy from '/freqtrade/user_data/strategies/my_strategy.py'...
2025-08-01 18:18:43,877 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2025-08-01 18:18:43,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2025-08-01 18:18:43,879 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: unlimited.
2025-08-01 18:18:43,880 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}.
2025-08-01 18:18:43,881 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value in config file: 10.
2025-08-01 18:18:43,883 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.2}
2025-08-01 18:18:43,884 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 5m
2025-08-01 18:18:43,885 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.5
2025-08-01 18:18:43,886 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2025-08-01 18:18:43,887 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2025-08-01 18:18:43,888 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2025-08-01 18:18:43,889 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2025-08-01 18:18:43,890 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2025-08-01 18:18:43,891 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'limit', 'exit': 'limit', 'stoploss': 'limit', 'stoploss_on_exchange': False, 'stoploss_on_exchange_interval': 60}   
2025-08-01 18:18:43,892 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2025-08-01 18:18:43,893 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2025-08-01 18:18:43,894 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: unlimited
2025-08-01 18:18:43,895 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 30
2025-08-01 18:18:43,896 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2025-08-01 18:18:43,897 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2025-08-01 18:18:43,898 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2025-08-01 18:18:43,899 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2025-08-01 18:18:43,900 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2025-08-01 18:18:43,900 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2025-08-01 18:18:43,901 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2025-08-01 18:18:43,902 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: True
2025-08-01 18:18:43,903 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2025-08-01 18:18:43,904 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: 10
2025-08-01 18:18:43,905 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2025-08-01 18:18:43,939 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2025-08-01 18:18:43,965 - freqtrade.optimize.backtesting - INFO - Using fee 0.0008% - worst case fee from exchange (lowest tier).
2025-08-01 18:18:43,973 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 30 ...
2025-08-01 18:18:44,214 - freqtrade.optimize.backtesting - INFO - Loading data from 2023-12-31 21:30:00 up to 2025-07-07 00:00:00 (553 days).
2025-08-01 18:18:45,996 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2025-08-01 18:18:46,019 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy MyStrategy
2025-08-01 18:18:46,020 - freqtrade.strategy.hyper - INFO - No params for buy found, using default values.
2025-08-01 18:18:46,020 - freqtrade.strategy.hyper - INFO - No params for sell found, using default values.
2025-08-01 18:18:46,021 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2025-08-01 18:18:46,057 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2024-01-01 00:00:00 up to 2025-07-07 00:00:00 (553 days).
2025-08-01 18:18:46,517 - freqtrade.strategy.strategy_wrapper - ERROR - Unexpected error float division by zero calling <bound method MyStrategy.custom_roi of <my_strategy.MyStrategy object at 0x7feb807bb0e0>>
Traceback (most recent call last):
  File "/freqtrade/freqtrade/strategy/strategy_wrapper.py", line 31, in wrapper
    return f(*args, **kwargs)
  File "/freqtrade/user_data/strategies/my_strategy.py", line 97, in custom_roi
    profit_ratio = 1 / trade.open_rate
                   ~~^~~~~~~~~~~~~~~~~
ZeroDivisionError: float division by zero

```