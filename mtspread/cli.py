import click
from mtspread import spread as _spread


@click.command()
@click.argument("symbol1")
@click.argument("symbol2")
def spread(symbol1, symbol2):
    """Exibe dados do spread entre dois ativos."""
    precos1 = _spread.precos(symbol1, 610)
    precos2 = _spread.precos(symbol2, 610)
    spreads = _spread.spreads(precos1, precos2)
    click.echo("%.2f" % _spread.spread(symbol1, symbol2))
    click.echo("media %.2f" % _spread.diferenca_media(spreads))
    click.echo("maxima %.2f" % max(spreads))
    click.echo("minima %.2f" % min(spreads))
    click.echo("desvio padrao %.2f" % _spread.desvio_padrao(spreads))
    return 0
