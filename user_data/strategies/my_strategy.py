from freqtrade.strategy.interface import IStrategy, logger
from freqtrade.strategy import IntParameter, DecimalParameter, informative
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

    @informative('8h', candle_type='funding_rate')
    def populate_indicators_funding_rates(self, dataframe: DataFrame, metadata: dict):
        # Adding funding rates to have them in populate_indicators that are not from the box.
        dataframe['funding_rate'] = 0
        if len(dataframe) > 0:
            dataframe['funding_rate'] = dataframe['open'].shift(-1)
            dataframe['funding_rate'] = dataframe['funding_rate'].fillna(0)
        return dataframe

    def populate_indicators(self, df: DataFrame, metadata: dict) -> DataFrame:
        price_change = df['close'].pct_change().fillna(0)
        df['pump_close'] = df['close'].where(
            (price_change > 0.03) &
            (df['funding_rate_8h'] > -0.00086)
        )

        # Historical min over e.g. last 360 days (assuming 5m candles: 360d * 24h * 12):
        lookback = 360 * 24 * 12
        df['hist_min'] = df['low'].rolling(lookback, min_periods=1).min()

        return df


    def populate_entry_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        df['enter_short'] = 0
        df.loc[
            (df['pump_close'].notnull()),
            'enter_short'] = 1

        return df

    def populate_exit_trend(self, df: DataFrame, metadata: dict) -> DataFrame:
        df['exit_short'] = 0
        return df

    def custom_roi(self, pair: str, trade, current_time, trade_duration: int,
                   entry_tag: str | None, side: str, **kwargs) -> float | None:
        profit_ratio = 0.03
        return profit_ratio


