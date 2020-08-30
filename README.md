# pypyr slack plug-in

![pypyr task runner for automation pipelines](https://pypyr.io/images/2x1/pypyr-taskrunner-yaml-pipeline-automation-1200x600.1bd2401e4f8071d85bcb1301128e4717f0f54a278e91c9c350051191de9d22c0.png)

Send messages to [slack](https://slack.com/) from pypyr. This is useful
for sending notifications on success or failure conditions in your automation 
pipelines. Or for sending a message just because you can.

You can send slack message notifications via the cli without writing any code.

[pypyr](https://pypyr.io/) is a cli & api to run pipelines 
defined in yaml.

All documentation for the pypyr slack plugin is here: 
https://pypyr.io/docs/plugins/slack/

[![build status](https://github.com/pypyr/pypyr-slack/workflows/lint-test-build/badge.svg)](https://github.com/pypyr/pypyr-slack/actions)
[![coverage status](https://codecov.io/gh/pypyr/pypyr-slack/branch/master/graph/badge.svg)](https://codecov.io/gh/pypyr/pypyr-slack)
[![pypi version](https://badge.fury.io/py/pypyrslack.svg)](https://pypi.python.org/pypi/pypyrslack/)
[![apache 2.0 license](https://img.shields.io/github/license/pypyr/pypyr-slack)](https://opensource.org/licenses/Apache-2.0)


## installation
```bash
$ pip install --upgrade pypyrslack
```

pypyrslack depends on the pypyr core. The above `pip` will install it
for you if you don't have it already.

## usage
Example automation pipeline sending notifications to slack:

```yaml
steps:
  - name: pypyrslack.steps.send
    in:
      slackToken: supersecurevaluegoeshere
      slackChannel: "#channelnamehere"
      slackText: "pypyr is busy doing things :construction:"
```

## Help!
Don't Panic! Check the 
[pypyrslack technical docs](https://pypyr.io/docs/plugins/slack/) to begin. 
For help, community & talk, check 
[pypyr twitter](https://twitter.com/pypyrpipes/), or join the chat on 
[pypyr discord](https://discordapp.com/invite/8353JkB)!

## contribute
### developers
For information on how to help with pypyr, run tests and coverage,
please do check out the [pypyr contribution
guide](https://pypyr.io/docs/contributing/).

### bugs
Well, you know. No one's perfect. Feel free to [create an
issue](https://github.com/pypyr/pypyr-slack/issues/new).

## License
pypyr is free & open-source software distributed under the Apache 2.0 License.

Please see [LICENSE](LICENSE) in the root of the repo.

Copyright 2017 the pypyr contributors.