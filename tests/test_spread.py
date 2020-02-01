from spread import spread
from unittest import mock


@mock.patch("spread.spread.mql5")
def test_pega_precos_do_ativo_em_um_periodo(mql5):
    mql5.CopyClose.return_value = [46.69, 46.7, 46.6]
    assert spread.prices("ccmk20", 3) == [46.69, 46.70, 46.60]


def test_obtem_lista_de_diferencas_entre_dois_precos():
    prices1 = [1.00, 2.00, 3.00]
    prices2 = [4.50, 5.50, 6.50]
    assert spread.diferencas(prices1, prices2) == [3.5, 3.5, 3.5]


def test_calcula_media_das_diferencas_de_precos():
    diferencas = [2.50, 4.50, 1.00]
    assert spread.average(diferencas) == 2.67
