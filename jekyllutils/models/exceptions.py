import click


class MyClickException(click.ClickException):
    """
    Just to wrap click's default exception with a red message, this makes
    it easier for users to see there's an error
    """

    def __init__(self, msg):
        click.ClickException.__init__(self, click.style(msg, fg="red"))


class MyUsageError(click.UsageError):
    def __init__(self, msg):
        click.UsageError.__init__(self, click.style(msg, fg="red"))
