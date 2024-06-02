import pytest

@pytest.mark.api
def test_user_exists(github_api):
    username = "defunkt"
    response = github_api.get_user(username)
    assert response['login'] == username

@pytest.mark.api
def test_user_not_exists(github_api):
    username = "butenkosergii"
    response = github_api.get_user(username)
    assert response['message'] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_name = "become-qa-auto"
    response = github_api.search_repo(repo_name)
    assert response['total_count'] == 25  # Потрібно змінити на актуальне значення

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_name = "sergiibutenko_repo_non_exist"
    response = github_api.search_repo(repo_name)
    assert response['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    repo_name = "s"
    response = github_api.search_repo(repo_name)
    assert response['total_count'] != 0
