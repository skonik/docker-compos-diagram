import click

from docker_compose_diagram.draw import draw


@click.command()
@click.option("--file", default="docker-compose.yml", help="docker-compose file")
@click.option(
    "--direction",
    default="TB",
    type=click.Choice(["TB", "BT", "LR", "RL"], case_sensitive=True),
)
@click.option("--nodesep", default="1.0", type=click.FLOAT)
def process_cli(file, direction, nodesep):
    graph_attr = {
        "nodesep": str(nodesep),
    }
    draw(file, direction, graph_attr)


if __name__ == "__main__":
    process_cli()
