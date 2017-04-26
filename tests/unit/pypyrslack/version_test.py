"""version.py unit tests."""
import pypyrslack.version
import platform


def test_get_version():
    actual = pypyrslack.version.get_version()
    expected = (f'pypyr-slack {pypyrslack.version.__version__} '
                f'python {platform.python_version()}')
    assert actual == expected, "version not returning correctly"
