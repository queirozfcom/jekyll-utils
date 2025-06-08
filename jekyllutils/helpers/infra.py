from sys import platform


def is_linux():
    """Check if the current platform is Linux."""
    return platform.startswith("linux")


def is_mac():
    """Check if the current platform is macOS."""
    return platform == "darwin"
