from setuptools import setup, find_packages

setup(
        name="jekyllutils",
        version='0.2',
        py_modules=['generators'],
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'Click',
            'python-slugify',
            'appdirs',
            'toml'
        ],
        entry_points='''
        [console_scripts]
        jk-new=jekyllutils.generators:new_post
        jk-edit=jekyllutils.managers:edit_post
        jk-config-set-editor=jekyllutils.configs:set_editor
        jk-config-set-posts-path=jekyllutils.configs:set_path_to_posts_dir
        jk-config-dump-configs=jekyllutils.configs:dump_configs
        jk-config-clear-configs=jekyllutils.configs:clear_configs
        jk-list-by-tag=jekyllutils.managers:list_by_tag
        jk-list-unpublished=jekyllutils.managers:list_unpublished
    '''

)
