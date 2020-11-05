from unittest.mock import Mock

import pytest

from lib_python_est import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/41023583?v=4'
    resp_mock.json.return_value = {
        'login': 'brutos', 'id': 402714,
        'avatar_url': url,
    }
    get_mock= mocker.patch('lib_python_est.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('brutos212')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('brutos212')
    assert 'https://avatars0.githubusercontent.com/u/41023583?v=4' == url
