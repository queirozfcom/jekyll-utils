import click,os,textwrap
from datetime import datetime
from slugify import slugify

@click.command()
@click.option('--tag', '-t', multiple=True)
@click.option('--category','-c',default=['technology'])
@click.option('--path-to-posts','-p',type=click.Path())
@click.argument('title')
def new(title,tag,category,path_to_posts):
    
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
    path_to_file = current_dir+"/"+path_to_posts.rstrip("/")+"/"+file_name

    with open(path_to_file,"w") as f:
        f.write(textwrap.dedent(contents).lstrip().format(title,date_str,tags,categories))

    print(path_to_file)
