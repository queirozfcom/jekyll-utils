import time
from subprocess import call

import click
from jekyllutils.helpers.configs import get_path_to_posts_dir, get_editor_name
from jekyllutils.helpers.editors import get_executable_from_name
from jekyllutils.helpers.files import list_files, list_filenames_by_tag, list_unpublished_filenames, resolve_path


@click.command()
@click.argument('keywords', nargs=-1)
def edit_post(keywords):
    if len(keywords) == 0:
        raise click.UsageError('Please supply at least one keyword as argument')

    path_to_posts_directory = resolve_path(get_path_to_posts_dir())
    post_files = list_files(path_to_posts_directory, keywords)

    if len(post_files) == 0:
        raise click.UsageError('No files match the given keywords')
    elif len(post_files) > 1:

        exception = click.UsageError('Multiple files match the given keywords')
        exception.show()

        for file in sorted(post_files[:10]):
            click.echo(file)

        raise exception

    else:
        path_to_file = path_to_posts_directory + "/" + post_files[0]
        editor = get_editor_name()
        editor_executable = get_executable_from_name(editor)
        call([editor_executable, path_to_file])
        time.sleep(2)  # just to give the os time for the editor to load


@click.command()
@click.argument('tags', nargs=-1)
def list_by_tag(tags):
    if len(tags) == 0:
        raise click.UsageError('Please supply at least one tag as argument')

    path_to_posts_directory = resolve_path(get_path_to_posts_dir())
    filenames = list_filenames_by_tag(path_to_posts_directory, tags)

    for filename in sorted(filenames):
        click.echo(filename)


@click.command()
def list_unpublished():
    path_to_posts_directory = resolve_path(get_path_to_posts_dir())
    filenames = list_unpublished_filenames(path_to_posts_directory)

    # show older stuff first, so that it forces me to make a decision on those
    for filename in sorted(filenames, reverse=True):
        click.echo(filename)
