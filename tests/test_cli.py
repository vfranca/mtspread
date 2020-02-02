from click.testing import CliRunner
from mtspread import cli
from unittest import mock


runner = CliRunner()


@mock.patch("mtspread.cli.get_spread")
def test_exibe_spread_entre_dois_ativos(get_spread):
    get_spread.return_value = 2.25
    res = runner.invoke(cli.spread, ["ccmk20", "ccmh20"])
    assert res.output == "spread medio 2.06\nspread atual 2.25\n"
    assert res.exit_code == 0
