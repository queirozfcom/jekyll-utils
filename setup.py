from setuptools import setup

setup(
        name="jekyllutils",
        version='0.1',
        py_modules=['generators'],
        install_requires=[
            'click',
            'python-slugify',
            'appdirs',
            'toml'
        ],
        entry_points='''
        [console_scripts]
        jk-new = jekyllutils.generators:new_post
        jk-edit = jekyllutils.managers:edit_post
        jk-config-set-editor = jekyllutils.configs:set_editor
        jk-config-set-posts-path = jekyllutils.configs:set_path_to_posts_dir
        jk-config-dump-configs = jekyllutils.configs:dump_configs
        jk-config-clear-configs = jekyllutils.configs:clear_configs
    '''

)
