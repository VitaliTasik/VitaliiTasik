import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""

@pytest.mark.check
def test_name(user):
    assert user.name == "Vitalii"

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Tanasiienko"
    