from PyMQL5 import PyMQL5
import statistics

mql5 = PyMQL5()


def prices(symbol: str, count: int, period: str = "Daily") -> list:
    """Retorna os preços de fechamento."""
    return mql5.CopyClose(symbol, period, 0, count)


def diferencas(prices1: list, prices2: list) -> list:
    """Retorna lista das diferenças entre duas séries de preços."""
    res = []
    for i in range(len(prices1)):
        res.append(prices2[i] - prices1[i])
    return res


def media(serie: list) -> float:
    """Calcula a média de uma série."""
    return round(statistics.mean(serie), 2)


def desvio_padrao(serie):
    """Calcula o desvio padrão da série."""
    return round(statistics.pstdev(serie), 2)
