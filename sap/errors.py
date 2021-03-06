"""SAP CLI error types"""


class FatalError(Exception):
    """Common base exception type for """

    # pylint: disable=unnecessary-pass
    pass


class SAPCliError(FatalError):
    """Common base exception type for runtime errors"""

    # pylint: disable=unnecessary-pass
    pass
