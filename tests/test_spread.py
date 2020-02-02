from mtspread import spread
from unittest import mock, skip

spreads = [2.50, 4.50, 1.00]


@mock.patch("mtspread.spread.mql5")
def test_pega_precos_do_ativo_em_um_periodo(mql5):
    mql5.CopyClose.return_value = [46.69, 46.7, 46.6]
    assert spread.precos("ccmk20", 3) == [46.69, 46.70, 46.60]


def test_obtem_lista_de_spreads_entre_dois_precos():
    prices1 = [1.00, 2.00, 3.00]
    prices2 = [4.50, 5.50, 6.50]
    assert spread.spreads(prices1, prices2) == [3.5, 3.5, 3.5]


def test_calcula_diferenca_media_de_precos():
    assert spread.diferenca_media(spreads) == 2.67


def test_calcula_o_desvio_padrao_da_serie():
    assert spread.desvio_padrao(spreads) == 1.43


@mock.patch("mtspread.spread.mql5")
def test_obtem_o_spread_de_dois_ativos(mql5):
    mql5.iClose.return_value = 46.69
    assert spread.spread("ccmk20", "ccmh20") == 0.0
