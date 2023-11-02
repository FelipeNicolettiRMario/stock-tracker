from .finance import IFinanceGateway

import yfinance as yf

class YahooFinanceGateway(IFinanceGateway):

    def get_most_recent_price(self, ticker: str) -> float:
        
        msft = yf.Ticker(ticker)

        return msft.history(period='1d')['Close'][0]
