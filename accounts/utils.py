from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

def delete_expired_guest_users():
    expiry_time = timezone.now() - timedelta(hours=1)

    User.objects.filter(
        is_guest=True,
        created_at__lt=expiry_time
    ).delete()
