import yfinance as yf
import pandas as pd

class OptionsData:
    def get_calls(self, ticker):
        tck = yf.Ticker(ticker)
        options = tck.option_chain()
        return options.calls

    def get_puts(self, ticker):
        tck = yf.Ticker(ticker)
        options = tck.option_chain()
        return options.puts

    def get_volume_sum(self, df):
        return df['volume'].sum()

    def get_put_call_ratio(self, ticker):
        calls = self.get_calls(ticker)
        puts = self.get_puts(ticker)
        call_volume = self.get_volume_sum(calls)
        put_volume = self.get_volume_sum(puts)
        put_call_ratio = put_volume / call_volume if call_volume != 0 else float('inf')
        return put_call_ratio, put_volume, call_volume
