import click

from jekyllutils.helpers import configs
from jekyllutils import files
from jekyllutils.helpers.colours import with_success_prefix


@click.command()
@click.argument('path')
def set_posts_path(path):
    absolute_path = files.resolve_path(path)
    configs.set_posts_path_dir(absolute_path)
    click.echo(with_success_prefix(f"""Config key "posts-path" was set to "{path}" """))


@click.command()
@click.argument('name')
def set_editor(name):
    configs.set_editor_name(name)
    click.echo(with_success_prefix(f"""Config key "editor" was set to "{name}" """))


@click.command()
def dump_configs():
    configs.dump_configs()


@click.command()
def clear_configs():
    configs.clear_configs()
    click.echo(with_success_prefix("Configs cleared"))
