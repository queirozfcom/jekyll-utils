from setuptools import setup, find_packages

setup(
        name="jekyllutils",
        version='0.5',
        py_modules=['generators'],
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'Click==8.0.2',
            'python-slugify',
            'appdirs==1.4.4',
            'toml==0.10.2'
        ],
        entry_points='''
        [console_scripts]
        jk-new=jekyllutils.generators:new_post
        jk-new-paper-summary=jekyllutils.generators:new_post_paper_summary
        jk-new-crypto-overview=jekyllutils.generators:new_post_crypto_asset_overview
        jk-edit=jekyllutils.managers:edit_post
        jk-config-set-editor=jekyllutils.configs:set_editor
        jk-config-set-posts-path=jekyllutils.configs:set_posts_path
        jk-config-dump-configs=jekyllutils.configs:dump_configs
        jk-config-clear-configs=jekyllutils.configs:clear_configs
        jk-list-by-tag=jekyllutils.managers:list_by_tag
        jk-list-unpublished=jekyllutils.managers:list_unpublished
    '''

)
