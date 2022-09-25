import pytest
from django.urls import reverse


# Получение статуса партнёра
@pytest.mark.django_db
def test_partner_get_status(auth_partner, shop_factory):
    shop = shop_factory(make_m2m=True)
    url = reverse("app:partner-state")
    resp = auth_partner.get(url)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert resp_json['id'] == shop.id
    assert resp_json['state'] == shop.state


# Изменение статуса партнёра
@pytest.mark.django_db
def test_partner_update_status(auth_partner, shop_factory):
    shop_factory(make_m2m=True)
    url = reverse("app:partner-state")
    resp = auth_partner.post(url, {'state': 'on'})
    resp_json = resp.json()
    print(resp_json)
    assert resp.status_code == 200
    assert resp_json['Status'] is True
