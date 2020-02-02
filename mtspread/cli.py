import click
from mtspread.spread import (
    precos,
    spreads as get_spreads,
    diferenca_media,
    spread as get_spread,
)


@click.command()
@click.argument("symbol1")
@click.argument("symbol2")
def spread(symbol1, symbol2):
    """Exibe o spread entre ativos."""
    precos_symbol1 = precos(symbol1, 610)
    precos_symbol2 = precos(symbol2, 610)
    spreads = get_spreads(precos_symbol1, precos_symbol2)
    spread_medio = diferenca_media(spreads)
    spread_atual = get_spread(symbol1, symbol2)
    click.echo("spread medio %.2f" % spread_medio)
    click.echo("spread atual %.2f" % spread_atual)
    return 0
