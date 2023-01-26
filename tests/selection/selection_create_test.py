import pytest


@pytest.mark.django_db
def test_selection_create(client, ad, access_token):
    data = {
        'name': 'test for selection',
        'items': [ad.pk]
    }

    response = client.post(
        '/selection/create/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Bearer ' + access_token
    )

    owner = response.data.get('owner')

    expected_data = {
        'id': 1,
        'name': 'test for selection',
        'owner': owner,
        'items': [ad.pk]
    }

    assert response.status_code == 201
    assert response.data == expected_data
