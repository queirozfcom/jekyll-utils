jekyll-utils
=======

A small Python 3 command-line application (based upon [click](http://click.pocoo.org/6/)) to speed up some common tasks for those who blog using Jekyll.

This will be **especially** useful for people who post many short blog entries, as opposed to those who prefer to blog less frequently, with longer posts.

## Installation

- Prerequisites: `virtualenv`

 - On Ubuntu, install it via `$ sudo apt-get install python-virtualenv`

- Installing jekyll-utils using pip

 - `$ git clone https://github.com/queirozfcom/jekyll-utils`
 - `$ cd jekyll-utils`
 - `$ virtualenv -p python3 jekyll-venv`
 - `$ source jekyll-venv/bin/activate`
 - `$ pip install .`

 This will install all commands to your virtualenv. Type `jk-` and then hit `<TAB>` to see all available commands.

- Initial configs. These are needed to start using the tools:

 - `$ jk-config-set-editor <your editor name>`
 - `$ jk-config-set-posts-path <path to the _posts directory>`

## Features

> TODO

## Examples

- `$ jk-new "My new Post" --tag foo --tag bar --category general --edit`

- `$ jk-edit a couple of keywords`


