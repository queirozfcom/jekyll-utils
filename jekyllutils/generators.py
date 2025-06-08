import textwrap
import time
from datetime import datetime
from subprocess import call

import click
from slugify import slugify

from jekyllutils.helpers.colours import with_success_prefix
from jekyllutils.helpers.configs import get_posts_path, get_editor_name
from jekyllutils.helpers.editors import get_executable_from_name


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

    path_to_file = get_posts_path().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title, date_str, tags))



    editor = get_editor_name()
    editor_executable = get_executable_from_name(editor)

    command = "{0} {1}".format(editor_executable, path_to_file)
    call([command], shell=True)

    time.sleep(2)  # just to give the os time for the editor to load

    click.echo(with_success_prefix("Post created at: {0}".format(path_to_file)))


@click.command()
@click.option('--tag', '-t', multiple=True, help="Multiple values allowed")
@click.argument('title')
def new_post_paper_summary(title, tag):
    """Creates an empty markdown post with the given title for Jekyll in the
    directory specified by the configs. It will include a front-matter
    with the default options and optional tags or categories.
    """

    contents = _get_contents_paper_summary()

    title_full = "Paper Summary: " + title

    slug = slugify(title_full)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    tags = ",".join(list(map(lambda el: '"' + str(el).strip() + '"', tag)))

    file_name = date.strftime("%Y-%m-%d") + "-" + slug + ".markdown"

    path_to_file = get_posts_path().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title_full, date_str, tags, title))

    editor = get_editor_name()
    editor_executable = get_executable_from_name(editor)

    command = "{0} {1}".format(editor_executable, path_to_file)
    call([command], shell=True)

    time.sleep(2)  # just to give the os time for the editor to load

    click.echo(with_success_prefix("Post (Paper Summary) created at: {0}".format(path_to_file)))


@click.command()
@click.option('--tag', '-t', multiple=True, help="Multiple values allowed")
@click.argument('title')
def new_post_crypto_asset_overview(title, tag):
    """Creates an empty markdown post with the given title for Jekyll in the
    directory specified by the configs. It will include a front-matter
    with the default options and optional tags or categories.
    """

    contents = _get_contents_crypto_asset_overview()

    title_full = "Crypto Asset Overview: " + title

    slug = slugify(title_full)
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S %z")
    tags = ",".join(list(map(lambda el: '"' + str(el).strip() + '"', tag)))

    file_name = date.strftime("%Y-%m-%d") + "-" + slug + ".markdown"

    path_to_file = get_posts_path().rstrip("/") + "/" + file_name

    with open(path_to_file, "w") as f:
        f.write(textwrap
                .dedent(contents)
                .lstrip()
                .format(title_full, date_str, tags, title))

    editor = get_editor_name()
    editor_executable = get_executable_from_name(editor)

    command = "{0} {1}".format(editor_executable, path_to_file)
    call([command], shell=True)

    time.sleep(2)  # just to give the os time for the editor to load

    click.echo(with_success_prefix("Post (Paper Summary) created at: {0}".format(path_to_file)))


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
    toc: true
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
    toc: true
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

      <div class="paper-screenshot-img-div" markdown="1">
      ![alt-text](img-link)
      *{3} [Source](link-to-paper)*
      </div>

    ## WHAT


    ## WHY	
    
    
    ## HOW
    
    
    ## CLAIMS

    
    ## QUOTES


    ## EXTENDS/USES


    ## NOTES  


    ## MY 2¢

    -----
    
    ### References

    """


def _get_contents_crypto_asset_overview():
    return """
    ---
    layout: page
    header: no
    title: "{0}"
    date: {1}
    tags: ["cryptoassets",{2}]
    meta_description: | 
        Short overview with the least you need to know about <CRYPTO ASSET>
    image:
        thumb: square/cryptocurrency-icons/128/black/<ICON-HERE>.png      
    comments: true
    published: false
    toc: true
    ---

    > <span style="color:red; font-weight:bold">DISCLAIMER</span> This post reflects my personal opinion only; it does not constitute investment advice of any kind.

    ## Overview


    ## Currency: XXX


    ## Similar to


    ## Notes

    -----

    ### References

    """
