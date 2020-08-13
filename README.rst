###################
pypyr slack plug-in
###################

.. image:: https://pypyr.io/images/2x1/pypyr-taskrunner-yaml-pipeline-automation-1200x600.1bd2401e4f8071d85bcb1301128e4717f0f54a278e91c9c350051191de9d22c0.png
    :alt: pypyr task runner for automation pipelines
    :align: center

*pypyr*
    pronounce how you like, but I generally say *piper* as in "piping down the
    valleys wild"

Send messages to `slack <https://slack.com/>`__ from pypyr. This is useful for
sending notifications on success or failure conditions in your pipelines. Or
for sending a message just because you can.

`pypyr <https://github.com/pypyr/pypyr>`__ is a command line interface to
run pipelines defined in yaml.

|build-status| |coverage| |pypi|

.. contents::

.. section-numbering::

************
Installation
************

pip
===
.. code-block:: bash

  # pip install --upgrade pypyrslack

pypyrslack depends on the pypyr core. The above ``pip`` will install it for you 
if you don't have it already.

Python version
==============
Tested against Python >=3.6

*****
steps
*****
pypyrslack.steps.send
=====================
Send a message to slack.

Required Context
----------------

Requires the following context items:

- slackToken

  - your slack api token. Keep this secure.
- slackChannel

  - send to this slack channel (include # in front)
- slackText

  - the body of your message. Use your usual slack formatting chars.

Text substitutions
------------------
For both slackChannel and slackText you can use substitution tokens, aka string
interpolation. This substitutes anything between curly braces with the context
value for that key. For example, if your context looked like this:

.. code-block:: yaml

  arbitraryValue: pypyrchannel
  arbitraryText: down the
  moreArbText: wild
  slackChannel: "#{arbitraryValue}"
  slackText: "piping {arbitraryText} valleys {moreArbText}"

This will result in sending a message to *#pypyrchannel* with text:

*piping down the values wild*

Escape literal curly braces with doubles: {{ for {, }} for }

See a worked example `for substitutions here
<https://github.com/pypyr/pypyr-example/tree/master/pipelines/substitutions.yaml>`__.

Sample pipeline
---------------
Here is some sample yaml of what a pipeline using the pypyr-slack plug-in
could look like:

.. code-block:: yaml

  steps:
    - name: pypyrslack.steps.echo
      in:
        echoMe: "just an arb step that may or may not fail."
    - name: pypyrslack.steps.send
      in:
        slackToken: supersecurevaluegoeshere
        slackChannel: "#channelnamehere"
        slackText: "pypyr is busy doing things :construction:"

  # The slackToken and slackChannel have already been set in steps
  # on_success and on_failure are just changing the text for the message.
  on_success:
    - name: pypyrslack.steps.send
      in:
        slackText: "that went well! :hotdog:"

  on_failure:
    - name: pypyrslack.steps.send
      in:
        slackText: "whoops! :rage1:"

If you saved this yaml as ``./pipelines/hoping-for-a-hotdog.yaml``, you can run
from ./ the following:

.. code-block:: bash

  pypyr hoping-for-a-hotdog


See a worked example for `pypyr slack here
<https://github.com/pypyr/pypyr-example/tree/master/pipelines/slack.yaml>`__.

********************
slack authentication
********************
Get slack api token
===================
To authenticate against your slack, you need to create an api key. There're
various ways of going about this, using legacy tokens, test tokens or a bot.

I generally `create a bot <https://my.slack.com/services/new/bot>`__. Given
you're likely to use it just to send notifications to slack, rather than
consume events from slack, it's a pretty simple setup just to get your api key.

Remember to invite and add the bot you create to the slack channel(s) to which
you want to post. You invite the bot in like you would a normal user.


Ensure secrets stay secret
==========================
Be safe! Don't hard-code your api token, don't check it into a public repo.
Here are some tips for handling api tokens from `slack <http://slackapi.github.io/python-slackclient/auth.html#handling-tokens>`__.

Do remember not to fling the api key around as a shell argument - it could
very easily leak that way into logs or expose via a ``ps``. I generally use one
of the pypyr built-in context parsers like *pypyr.parser.jsonfile* or
*pypyr.parser.yamlfile*, see
`pypyr builtin context parsers <https://pypyr.io/docs/context-parsers/>`__.

*******
Testing
*******
Testing without worrying about dependencies
===========================================
Run from tox to test the packaging cycle inside a virtual env, plus run all
tests:

.. code-block:: bash

    # just run tests
    $ tox -e dev -- tests
    # run tests, validate README.rst, run flake8 linter
    $ tox -e stage -- tests

If tox is taking too long
=========================
The test framework is pytest. If you only want to run tests:

.. code-block:: bash

  $ pip install -e .[dev,test]

Day-to-day testing
==================
- Tests live under */tests* (surprising, eh?). Mirror the directory structure of
  the code being tested.
- Prefix a test definition with *test_* - so a unit test looks like

  .. code-block:: python

    def test_this_should_totally_work():

- To execute tests, from root directory:

  .. code-block:: bash

    pytest tests

- For a bit more info on running tests:

  .. code-block:: bash

    pytest --verbose [path]

- To execute a specific test module:

  .. code-block:: bash

    pytest tests/unit/arb_test_file.py

*****
Help!
*****
Don't Panic! For help, community or talk, join the chat on |discord|!

**********
Contribute
**********
Developers
==========
For information on how to help with pypyr, run tests and coverage, please do
check out the `pypyr contribution guide <https://pypyr.io/docs/contributing/>`_.

Bugs
====
Well, you know. No one's perfect. Feel free to `create an issue
<https://github.com/pypyr/pypyr-slack/issues/new>`_.


.. |build-status| image:: https://api.shippable.com/projects/58efdfe19755e8070035afd9/badge?branch=master
                    :alt: build status
                    :target: https://app.shippable.com/github/pypyr/pypyr-slack

.. |coverage| image:: https://api.shippable.com/projects/58efdfe19755e8070035afd9/coverageBadge?branch=master
                :alt: coverage status
                :target: https://app.shippable.com/github/pypyr/pypyr-slack

.. |pypi| image:: https://badge.fury.io/py/pypyrslack.svg
                :alt: pypi version
                :target: https://pypi.python.org/pypi/pypyrslack/
                :align: bottom

.. |discord| replace:: `discord <https://discordapp.com/invite/8353JkB>`__
