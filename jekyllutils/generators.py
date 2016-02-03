import click,os,sys,textwrap
from datetime import datetime
from slugify import slugify

from jekyllutils.lib.configs import get_posts_dir


@click.command()
@click.option('--tag', '-t', multiple=True)
@click.option('--category','-c',default=['technology'])
@click.argument('title')
def new(title,tag,category):
    """Creates an empty markdown post with the given title for Jekyll in the 
    specified path. It will include a front-matter with the default options
    and optional tags or categories."""


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
    tags = ",".join(list(map(lambda el: '"'+str(el).strip()+'"',tag)))
    categories = ",".join(list(map(lambda el: '"'+str(el).strip()+'"',category)))

    file_name = date.strftime("%Y-%m-%d")+"-"+slug+".markdown"

    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_file = current_dir+"/"+get_posts_dir().rstrip("/")+"/"+file_name

    print(path_to_file)
    sys.exit()

    with open(path_to_file,"w") as f:
        f.write(textwrap.dedent(contents).lstrip().format(title,date_str,tags,categories))

    click.echo(path_to_file)
