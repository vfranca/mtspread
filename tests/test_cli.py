from click.testing import CliRunner
from mtspread import cli
from unittest import mock, skip


runner = CliRunner()


@skip("")
@mock.patch("mtspread.cli._spread")
def test_exibe_spread_entre_dois_ativos(spread):
    spread.spread.return_value = 2.25
    spread.serie_spreads.return_value = [
        1.55,
        1.84,
        1.99,
        2.05,
        2.25,
        2.44,
        2.66,
        2.69,
        2.87,
        3.06,
        3.20,
        3.55,
    ]
    res = runner.invoke(cli.spread, ["ccmk20", "ccmh20"])
    expec = "2.25\n"
    expec += "media 1.00\n"
    expec += "venda 3.00\n"
    expec += "compra -1.00\n"
    expec += "periodos 250\n"
    expec += "max 3.55\n"
    expec += "min 1.55\n"
    expec += "desvio 1.00\n"
    assert res.output == expec
    assert res.exit_code == 0
