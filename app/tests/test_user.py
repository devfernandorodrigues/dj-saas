import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(email="someuser@test.com", password="foo")
    assert user.email == "someuser@test.com"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False


def test_create_superuser():
    admin_user = User.objects.create_superuser(
        email="superuser@test.com", password="foo"
    )
    assert admin_user.email == "superuser@test.com"
    assert admin_user.is_active is True
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True
