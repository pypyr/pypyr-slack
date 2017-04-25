"""pypyr step that sends a message to slack."""
import logging
from pypyrslack.errors import SlackSendError
from slackclient import SlackClient

logger = logging.getLogger(__name__)


def run_step(context):
    """Send slack message.

    Requires the following context items:
    slackToken - your slack api token
    slackChannel - the slack channel (include # in front)
    slackText - the body of your message. Use your usual slack formatting
                chars.

    Be `careful with your token <https://api.slack.com/docs/oauth-safety>`_

    See some details here for slackChannel options:
    https://api.slack.com/methods/chat.postMessage#channels

    Args:
        context: dictionary or dictionary-like. Mandatory. Requires these
                 keys:
                    - slackToken
                    - slackChannel
                    - slackText

    Raises:
        AssertionError: When any of slackToken, slackChannel or slackText do
                        not have values.
        SlackSendError: Something went wrong sending to slack. Be sure your
                        api token has access to the channel.
    """
    logger.debug("started")
    context.assert_keys_have_values(__name__,
                                    'slackToken',
                                    'slackChannel',
                                    'slackText')

    logger.debug(
        f"Sending to {context['slackChannel']}: {context['slackText']}")

    sc = SlackClient(context['slackToken'])

    result = sc.api_call(
        'chat.postMessage',
        as_user=True,
        channel=context.get_formatted('slackChannel'),
        text=context.get_formatted('slackText')
    )

    if result['ok']:
        logger.info(f"Sent message to slack {context['slackChannel']}.")
    else:
        raise SlackSendError(result['error'])

    logger.debug("done")
