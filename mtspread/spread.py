from PyMQL5 import PyMQL5
import statistics

mql5 = PyMQL5()


def precos(symbol: str, count: int, period: str = "Daily") -> list:
    """Retorna os preços de fechamento."""
    return mql5.CopyClose(symbol, period, 0, count)


def spread(symbol1: str, symbol2: str, period: str = "Daily") -> float:
    """Retorna o spread entre ativos."""
    preco1 = mql5.iClose(symbol1, period, 0)
    preco2 = mql5.iClose(symbol2, period, 0)
    return round(preco2 - preco1, 2)


def spreads(prices1: list, prices2: list) -> list:
    """Retorna lista das diferenças entre duas séries de preços."""
    res = []
    for i in range(len(prices1)):
        res.append(prices2[i] - prices1[i])
    return res


def diferenca_media(spreads: list) -> float:
    """Calcula a diferença média dos spreads."""
    return round(statistics.mean(spreads), 2)


def desvio_padrao(spreads: list) -> float:
    """Calcula o desvio padrão dos spreads."""
    return round(statistics.pstdev(spreads), 2)
