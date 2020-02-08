from click.testing import CliRunner
from mtspread import cli
from unittest import mock


runner = CliRunner()


@mock.patch("mtspread.cli._spread")
def test_exibe_spread_entre_dois_ativos(spread):
    spread.spread.return_value = 2.25
    spread.spreads.return_value = [
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
    assert (
        res.output == "2.25\nmedia 1.00\nmaxima 3.55\nminima 1.55\ndesvio padrao 1.00\n"
    )
    assert res.exit_code == 0
