# Yes, Django signals by default run in the same database transaction as the caller. This means that if the caller is involved in a database transaction and the transaction is rolled back, the signal will not be processed.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal received.")
    
try:
    with transaction.atomic():
        User.objects.create(username='test_user')
        raise Exception("Forcing rollback")
except Exception as e:
    print(e)

print("After transaction block.")
