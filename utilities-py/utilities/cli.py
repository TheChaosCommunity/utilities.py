"""A sample CLI."""

import click

from . import library


@click.command()
@click.argument('feet')
def main(feet: str):

    meters = library.feet_to_meters(feet)

    if meters is not None:
        click.echo(meters)


if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
