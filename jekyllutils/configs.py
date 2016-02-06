import click
import toml

from jekyllutils.helpers import files, configs
from jekyllutils.helpers.messages import wrap_success


@click.command()
@click.argument('path')
def set_path_to_posts_dir(path):
    absolute_path = files.resolve_path(path)
    configs.set_path_to_posts_dir(absolute_path)
    click.echo(wrap_success(
        """Config key "path-to-jekyll-posts" was set to "{0}" """.format(path)))


@click.command()
@click.argument('name')
def set_editor(name):
    configs.set_editor_name(name)
    click.echo(
        wrap_success("""Config key "editor" was set to "{0}" """.format(name)))


@click.command()
def dump_configs():
    configs.dump_configs()


@click.command()
def clear_configs():
    configs.clear_configs()
    click.echo(wrap_success("Configs cleared"))
