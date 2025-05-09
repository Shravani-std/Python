#if your tests are based on OS then u can use markers
import pytest

@pytest.mark.windows  #tag this tag as windows
def test_windows_functionality():
    assert True

@pytest.mark.windows
def test_windows_functionality():
    assert True

@pytest.mark.macos
def test_macos_1_functionality():
    assert True

@pytest.mark.macos
def test_macos_functionality():
    assert True
