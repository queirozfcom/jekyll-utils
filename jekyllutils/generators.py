import click, os, sys, textwrap, time

from datetime import datetime

from jekyllutils.lib.editors import get_executable_from_name
from jekyllutils.lib.messages import wrap_success
from slugify import slugify
from subprocess import call

from jekyllutils.lib.configs import get_path_to_posts_dir, get_editor_name


@click.command()
@click.option('--tag', '-t', multiple=True, help="Multiple values allowed")
@click.option('--category', '-c', default=['technology'],
              help="Multiple values allowed")
@click.option('--edit', is_flag=True,
              help="If this option is passed, open an editor to edit the newly-created post")
@click.argument('title')
def new(title, tag, category, edit):
    """Creates an empty markdown post with the given title for Jekyll in the 
    directory specified by the configs. It will include a front-matter
    with the default options and optional tags or categories.
    """

    contents = """
    ---
    layout: page
    header: no
    title: "{0}"
    date: {1}
    tags: [{2}]
    categories: [{3}]
    image:
        title: landscape/archer.png
        thumb: square/archer.png
        caption: Source
        caption_url: https://www.instagram.com/natasha_hellegouarch/
    comments: true
    ---

    """

    slug = slugify(title)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    tags = ",".join(list(map(lambda el: '"' + str(el).strip() + '"', tag)))
    categories = ",".join(
            list(map(lambda el: '"' + str(el).strip() + '"', category)))

    file_name = date.strftime("%Y-%m-%d") + "-" + slug + ".markdown"

    path_to_file = get_path_to_posts_dir().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title, date_str, tags, categories))

    if edit:
        editor = get_editor_name()
        editor_executable = get_executable_from_name(editor)
        call([editor_executable, path_to_file])
        time.sleep(2)  # just to give the os time for the editor to load

    click.echo(wrap_success("Post created at: {0}".format(path_to_file)))