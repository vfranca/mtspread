import click
from mtspread import spread as _spread


@click.command()
@click.argument("symbol1")
@click.argument("symbol2")
@click.option("--count", "-c", type=int, default=250, help="Quantidade de períodos")
def spread(symbol1, symbol2, count):
    """Exibe dados do spread entre dois ativos."""
    precos1 = _spread.serie_precos(symbol1, count)
    precos2 = _spread.serie_precos(symbol2, count)
    spreads = _spread.serie_spreads(precos1, precos2)
    desvio = _spread.desvio_padrao(spreads)
    media = _spread.media(spreads)
    venda = media + desvio * 2
    compra = media - desvio * 2
    click.echo("%.2f" % _spread.spread(symbol1, symbol2))
    click.echo("media %.2f" % media)
    click.echo("venda %.2f" % venda)
    click.echo("compra %.2f" % compra)
    click.echo("periodos %i" % count)
    click.echo("max %.2f" % max(spreads))
    click.echo("min %.2f" % min(spreads))
    click.echo("desvio %.2f" % desvio)
    return 0
