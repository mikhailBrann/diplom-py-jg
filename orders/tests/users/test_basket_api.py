import pytest
from django.urls import reverse


# Получение информации корзины
@pytest.mark.django_db
def test_get_basket(user, auth_client, order_factory):
    order_factory(make_m2m=True, user=user)
    url = reverse('app:basket')
    resp = auth_client.get(url)
    assert resp.status_code == 200


# Добавление товара в корзину
@pytest.mark.django_db
def test_add_items_to_basket(user, auth_client, order_factory, product_info_factory):
    created_item = product_info_factory(make_m2m=True)
    order_factory(make_m2m=True, user=user)
    url = reverse('app:basket')
    resp = auth_client.post(
        url,
        {'items': f'[{{"product_info": {created_item.id}, "quantity": "1"}}]'}
    )

    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json['Status'] is True
