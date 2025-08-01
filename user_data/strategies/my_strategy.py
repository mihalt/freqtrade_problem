from freqtrade.strategy.interface import IStrategy, logger
from freqtrade.strategy import IntParameter, DecimalParameter
from freqtrade.optimize.space import SKDecimal
from pandas import DataFrame
import pandas_ta as ta
import numpy as np

class MyStrategy(IStrategy):
    timeframe = '5m'
    minimal_roi = {}
    stoploss = -0.5
    trailing_stop = False
    use_custom_roi = True
    startup_candle_count = 30
    can_short: bool = True

    position_adjustment_enable = True
    stake_amount = 'unlimited'

    def populate_indicators(self, df: DataFrame, metadata: dict) -> DataFrame:
        price_change = df['close'].pct_change()
        df['pump'] = price_change > 0.03

        return df


    def populate_entry_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        df['enter_short'] = 0
        df.loc[
            (df['pump']),
            'enter_short'] = 1

        return df

    def populate_exit_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        df['exit_short'] = 0
        return df

    def custom_roi(self, pair: str, trade, current_time, trade_duration: int,
                   entry_tag: str | None, side: str, **kwargs) -> float | None:
        profit_ratio = 1 / trade.open_rate
        return profit_ratio


