def with_error_prefix(msg):
    return f"\033[31mERROR: \033[00m{msg}"


def with_success_prefix(msg):
    return f"\033[32mSUCCESS: \033[00m{msg}"

def wrap_red(msg):
    return f"\033[31m{msg}\033[00m"

def wrap_yellow(msg):
    return f"\033[33m{msg}\033[00m"


def wrap_green(msg):
    return f"\033[32m{msg}\033[00m"


def wrap_blue(msg):
    return f"\033[34m{msg}\033[00m"
