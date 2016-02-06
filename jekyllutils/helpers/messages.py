def wrap_error(msg):
    return "\033[31mERROR: \033[00m{0}".format(msg)


def wrap_success(msg):
    return "\033[32mSUCCESS: \033[00m{0}".format(msg)
