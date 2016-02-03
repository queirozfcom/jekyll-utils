import click
import toml

from jekyllutils.lib import files, configs


@click.command()
@click.argument('path')
def set_path_to_posts_dir(path):
    absolute_path = files.resolve_path(path)
    configs.set_path_to_posts_dir(absolute_path)


@click.command()
@click.argument('name')
def set_editor(name):
    configs.set_editor_name(name)


@click.command()
def dump_configs():
    configs.dump_configs()


@click.command()
def clear_configs():
    configs.clear_configs()
