"""version.py unit tests."""
import pypyrslack.version
import platform


def test_get_version():
    """Version as expected."""
    actual = pypyrslack.version.get_version()
    expected = (f'pypyrslack {pypyrslack.version.__version__} '
                f'python {platform.python_version()}')
    assert actual == expected, "version not returning correctly"
