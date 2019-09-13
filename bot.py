from os import path

import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    # say & echo
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    nonebot.run()