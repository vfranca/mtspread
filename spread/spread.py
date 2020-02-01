from PyMQL5 import PyMQL5
import statistics

mql5 = PyMQL5()


def precos(symbol: str, count: int, period: str = "Daily") -> list:
    """Retorna os preços de fechamento."""
    return mql5.CopyClose(symbol, period, 0, count)


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
