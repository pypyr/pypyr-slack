"""Custom exceptions for pypyrslack.

All pypyrslack specific exceptions derive from pypyr root Error.
"""

from pypyr.errors import Error as PypyrError


class Error(PypyrError):
    """Base class for all pypyr exceptions."""


class SlackSendError(Error):
    """Failed to send to slack."""
