"""send.py unit tests."""
import pytest
from pypyr.context import Context
from pypyr.errors import KeyInContextHasNoValueError, KeyNotInContextError
from pypyrslack.errors import SlackSendError
from pypyrslack.steps import send
from slackclient import SlackClient
from unittest.mock import patch


@patch.object(SlackClient, 'api_call')
@patch.object(SlackClient, '__init__', return_value=None)
def test_send_pass(mock_client, mock_post):
    """Success case for slack send."""
    mock_post.return_value = {'ok': True}
    context = Context({'slackToken': 'in your dreams',
                       'slackChannel': '#blah',
                       'slackText': 'this is :boom: text'})
    send.run_step(context)

    mock_client.assert_called_once_with('in your dreams')
    mock_post.assert_called_once_with(
        'chat.postMessage',
        as_user=True,
        channel='#blah',
        text='this is :boom: text')


@patch.object(SlackClient, 'api_call')
@patch.object(SlackClient, '__init__', return_value=None)
def test_send_with_string_interpolation(mock_client, mock_post):
    """Slack send with string interpolation"""
    mock_post.return_value = {'ok': True}
    context = Context({'arbkey1': 'arb value1',
                       'arbkey2': 'arb value2',
                       'arbkey3': 'channelarb',
                       'slackToken': 'in your dreams',
                       'slackChannel': '#{arbkey3}',
                       'slackText': '{arbkey2} this is :boom: text {arbkey1}'})

    send.run_step(context)

    mock_client.assert_called_once_with('in your dreams')
    mock_post.assert_called_once_with(
        'chat.postMessage',
        as_user=True,
        channel='#channelarb',
        text='arb value2 this is :boom: text arb value1')


@patch.object(SlackClient, 'api_call')
@patch.object(SlackClient, '__init__', return_value=None)
def test_slack_error_raises(mock_client, mock_post):
    """SlackSendError on slack failure."""
    # Actual error example: {'ok': False, 'error': 'channel_not_found'}
    mock_post.return_value = {'ok': False, 'error': 'bang bang'}
    context = Context({'slackToken': 'in your dreams',
                       'slackChannel': '#blah',
                       'slackText': 'this is :boom: text'})

    with pytest.raises(SlackSendError) as err_info:
        send.run_step(context)

    assert str(err_info.value) == "bang bang"


def test_no_slack_token_raises():
    """slackToken context required."""
    with pytest.raises(KeyNotInContextError) as err_info:
        context = Context({'slackChannel': '#blah',
                           'slackText': 'this is :boom: text'})
        send.run_step(context)

    assert str(err_info.value) == (
        "context['slackToken'] doesn't exist. It must exist for "
        "pypyrslack.steps.send.")


def test_no_slack_channel_raises():
    """slackChannel context required."""
    with pytest.raises(KeyNotInContextError) as err_info:
        context = Context({'slackToken': 'in your dreams',
                           'slackText': 'this is :boom: text'})
        send.run_step(context)

    assert str(err_info.value) == (
        "context['slackChannel'] doesn't exist. It must exist for "
        "pypyrslack.steps.send.")


def test_no_slack_text_raises():
    """slackChannel context required."""
    with pytest.raises(KeyNotInContextError) as err_info:
        context = Context({'slackToken': 'in your dreams',
                           'slackChannel': '#blah'})
        send.run_step(context)

    assert str(err_info.value) == (
        "context['slackText'] doesn't exist. It must exist for "
        "pypyrslack.steps.send.")


def test_slack_token_no_value_raises():
    """slackToken context value required."""
    with pytest.raises(KeyInContextHasNoValueError) as err_info:
        context = Context({
            'slackToken': None,
            'slackChannel': '#blah',
            'slackText': 'this is :boom: text'})
        send.run_step(context)

    assert str(err_info.value) == (
        "context['slackToken'] must have a value for pypyrslack.steps.send.")


def test_slack_channel_no_value_raises():
    """slackChannel context value required."""
    with pytest.raises(KeyInContextHasNoValueError) as err_info:
        context = Context({
            'slackToken': 'token here',
            'slackChannel': None,
            'slackText': 'this is :boom: text'})
        send.run_step(context)

    assert str(err_info.value) == (
        "context['slackChannel'] must have a value for pypyrslack.steps.send.")
