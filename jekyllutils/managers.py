import time
from subprocess import call

import click
from jekyllutils.helpers.configs import get_posts_path, get_editor_name
from jekyllutils.helpers.editors import get_executable_from_name
from jekyllutils.files import list_files, list_filenames_by_tag, list_unpublished_filenames, resolve_path
from jekyllutils.helpers.sorting import sort_filenames_ignoring_leading_text


@click.command()
@click.argument('keywords', nargs=-1)
def edit_post(keywords):
    if len(keywords) == 0:
        raise click.UsageError('Please supply at least one keyword as argument')

    path_to_posts_directory = resolve_path(get_posts_path())
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
@click.option('--reverse/--no-reverse', default=True,
              help="Default is to list files in reverse chronological order, just like git log")
def list_by_tag(tags, reverse):
    if len(tags) == 0:
        raise click.UsageError('Please supply at least one tag as argument')

    path_to_posts_directory = resolve_path(get_posts_path())
    filenames = list_filenames_by_tag(path_to_posts_directory, tags)

    if len(filenames) == 0:
        raise click.UsageError('No files match given tags')
    else:
        if reverse:
            click.echo_via_pager('\n'.join(sorted(filenames, reverse=True)))
        else:
            click.echo_via_pager('\n'.join(sorted(filenames)))


@click.command()
@click.option('--reverse/--no-reverse', default=True,
              help="Default is to list files in reverse chronological order, just like git log")
@click.option('--include-wip-alerts/--no-include-wip-alerts', default=True,
              help="Whether to consider WIP posts and posts with \"TODOS\" as unpublished even though they are published")
def list_unpublished(reverse, include_wip_alerts):
    path_to_posts_directory = resolve_path(get_posts_path())
    filenames = list_unpublished_filenames(path_to_posts_directory, include_wip_alerts)

    if len(filenames) == 0:
        raise click.UsageError('No files found. Well done!')
    else:

        if reverse:
            output = click.echo_via_pager('\n'.join(sort_filenames_ignoring_leading_text(filenames, reverse=True)))
        else:
            output = click.echo_via_pager('\n'.join(sort_filenames_ignoring_leading_text(filenames)))

        return output
