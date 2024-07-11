import pytest

@pytest.mark.macos
def test_mac1():
    assert True

@pytest.mark.macos
def test_mac2():
    assert True


@pytest.mark.windows
def test_win1():
    assert True


@pytest.mark.windows
def test_win2():
    assert True