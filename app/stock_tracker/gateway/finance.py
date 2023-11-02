from abc import ABC, abstractmethod

class IFinanceGateway(ABC):

    @abstractmethod
    def get_most_recent_price(self, ticker: str) -> float:
        """
            `ticker` = Given a stock ticker, returns the most recent price
        """
        pass
