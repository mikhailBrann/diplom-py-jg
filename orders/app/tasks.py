from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import ConfirmEmailToken, User


@shared_task()
def new_user_registered_email(user_id):
    """
    Отправляем письмо с подтверждением почты
    """
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    send_mail(
        subject=f"Password Reset Token for {token.user.email}",
        message=token.key,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[token.user.email],
    )

    return None


@shared_task()
def new_order_email(user_id):
    """
    Отправляем письмо при изменении статуса заказа
    """
    user = User.objects.get(id=user_id)

    send_mail(
        subject='Обновление статуса заказа',
        message='Заказ сформирован',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )

    return None
