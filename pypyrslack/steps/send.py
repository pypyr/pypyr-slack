"""pypyr step that sends a message to slack."""
import logging
from pypyrslack.errors import SlackSendError
from slack import WebClient
from slack.errors import SlackApiError

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
        "Sending to %s: %s", context['slackChannel'], context['slackText'])

    sc = WebClient(context.get_formatted('slackToken'))

    try:
        sc.chat_postMessage(
            channel=context.get_formatted('slackChannel'),
            text=context.get_formatted('slackText')
        )
        logger.info("Sent message to slack %s.", context['slackChannel'])
    except SlackApiError as err:
        raise SlackSendError(err.response['error']) from err

    logger.debug("done")
