import textwrap
import time
from datetime import datetime
from subprocess import call

import click
from jekyllutils.helpers.configs import get_path_to_posts_dir, get_editor_name
from jekyllutils.helpers.editors import get_executable_from_name
from jekyllutils.helpers.messages import wrap_success
from slugify import slugify


@click.command()
@click.option('--tag', '-t', multiple=True, help="Multiple values allowed")
@click.option('--image/--no-image', default=True,
              help="If this option is passed, include image section in the newly-created post")
@click.argument('title')
def new_post(title, tag, image):
    """Creates an empty markdown post with the given title for Jekyll in the 
    directory specified by the configs. It will include a front-matter
    with the default options and optional tags or categories.
    """

    if image:
        contents = _get_contents_img()
    else:
        contents = _get_contents_no_img()

    slug = slugify(title)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    tags = ",".join(list(map(lambda el: '"' + str(el).strip() + '"', tag)))

    file_name = date.strftime("%Y-%m-%d") + "-" + slug + ".markdown"

    path_to_file = get_path_to_posts_dir().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title, date_str, tags))

    editor = get_editor_name()
    editor_executable = get_executable_from_name(editor)
    call([editor_executable, path_to_file])
    time.sleep(2)  # just to give the os time for the editor to load

    click.echo(wrap_success("Post created at: {0}".format(path_to_file)))


@click.command()
@click.option('--tag', '-t', multiple=True, help="Multiple values allowed")
@click.argument('title')
def new_post_paper_summary(title, tag):
    """Creates an empty markdown post with the given title for Jekyll in the
    directory specified by the configs. It will include a front-matter
    with the default options and optional tags or categories.
    """

    contents = _get_contents_paper_summary()

    title_full = "Paper Summary: "+title

    slug = slugify(title_full)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    tags = ",".join(list(map(lambda el: '"' + str(el).strip() + '"', tag)))

    file_name = date.strftime("%Y-%m-%d") + "-" + slug + ".markdown"

    path_to_file = get_path_to_posts_dir().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title_full, date_str, tags, title))

    editor = get_editor_name()
    editor_executable = get_executable_from_name(editor)
    call([editor_executable, path_to_file])
    time.sleep(2)  # just to give the os time for the editor to load

    click.echo(wrap_success("Post (Paper Summary) created at: {0}".format(path_to_file)))


def _get_contents_no_img():
    return """
    ---
    layout: page
    header: no
    title: "{0}"
    date: {1}
    tags: [{2}]
    comments: true
    published: false
    ---

    """


def _get_contents_img():
    return """
    ---
    layout: page
    header: no
    title: "{0}"
    date: {1}
    tags: [{2}]
    meta_description: | 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac arcu urna. Fusce non metus massa. 
        Fusce vitae feugiat tortor. Donec ut varius dui. Phasellus condimentum, quam eu vehicula cursus, magna erat porta.
    image:
        title: landscape/icon.png
        thumb: square/icon.png
        caption: Source
        caption_url: https://www.iconfinder.com/webalys
    comments: true
    published: false
    ---

    """

def _get_contents_paper_summary():
    return """
    ---
    layout: page
    header: no
    title: "{0}"
    date: {1}
    tags: ["paper-summary",{2}]
    meta_description: | 
        Summary of the YEAR article "{3}" by AUTHORS.
    image:
        thumb: square/academia_hat.png      
    comments: true
    published: false
    ---
    
    > <span style="font-weight:bold">Please note</span> This post is mainly intended for my **personal use**. It is not peer-reviewed work and should not be taken as such.

    ## WHAT
    
    
    ## HOW
    
    
    ## CLAIMS
    
    
    ## NOTES

    -----
    
    ### References

    """