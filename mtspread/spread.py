from PyMQL5 import PyMQL5
import statistics

mql5 = PyMQL5()


def serie_precos(symbol: str, count: int, period: str = "Daily") -> list:
    """Retorna os preços de fechamento."""
    return mql5.CopyClose(symbol, period, 0, count)


def spread(symbol1: str, symbol2: str, period: str = "Daily") -> float:
    """Retorna o spread entre ativos."""
    preco1 = mql5.iClose(symbol1, period, 0)
    preco2 = mql5.iClose(symbol2, period, 0)
    res = abs(preco2 - preco1)
    return round(res, 2)


def serie_spreads(prices1: list, prices2: list) -> list:
    """Retorna serie dos spreads entre duas séries de preços."""
    res = []
    for i in range(len(prices1)):
        spread = abs(prices2[i] - prices1[i])
        res.append(spread)
    return res


def media(serie: list) -> float:
    """Retorna a média de uma série."""
    return round(statistics.mean(serie), 2)


def desvio_padrao(serie: list) -> float:
    """Retorna o desvio padrão de uma série."""
    return round(statistics.pstdev(serie), 2)
