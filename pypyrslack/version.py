"""Version information."""

import platform

__version__ = '0.0.0'


def get_version():
    return (f'pypyr-slack {__version__} '
            f'python {platform.python_version()}')
