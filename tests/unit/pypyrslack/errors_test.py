"""errors.py unit tests."""
from pypyr.errors import Error as PypyrError
from pypyr.errors import PlugInError
from pypyrslack.errors import Error as PypyrSlackError
from pypyrslack.errors import SlackSendError
import pytest


def test_base_error_raises():
    """Pypyr root Error raises with correct message."""
    with pytest.raises(PypyrSlackError) as err_info:
        raise PypyrSlackError("this is error text right here")

    assert str(err_info.value) == "this is error text right here"


def test_slack_send_error_raises():
    """Slack send error raises with correct message."""
    with pytest.raises(SlackSendError) as err_info:
        raise SlackSendError("this is error text right here")

    assert str(err_info.value) == "this is error text right here"


def test_slack_send_error_inheritance():
    """SlackSendError should inherit all the way up to pypyr Error."""
    # confirm subclassed from pypyr root error
    err = SlackSendError()
    assert isinstance(err, PypyrSlackError)
    assert isinstance(err, PlugInError)
    assert isinstance(err, PypyrError)
