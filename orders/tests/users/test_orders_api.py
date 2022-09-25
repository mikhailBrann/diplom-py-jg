import pytest
from django.urls import reverse


# Получение заказа
@pytest.mark.django_db
def test_get_orders(user, auth_client, order_factory, product_info_factory, contact_factory):
    contact = contact_factory(make_m2m=True, user=user)
    order_factory(make_m2m=True, user=user, state='new', contact=contact)
    url = reverse('app:order')
    resp = auth_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert resp_json[0]['id']
    assert resp_json[0]['dt']
    assert resp_json[0]['state']
