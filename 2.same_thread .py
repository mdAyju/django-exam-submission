# Yes, by default, Django signals run in the same thread as the caller,
# which means that signal handling occurs in the main thread unless explicitly offloaded to another thread.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

# Creating a user and observing the thread
print(f"Main thread: {threading.current_thread().name}")
User.objects.create(username='test_user')

# Output
# Main thread: MainThread
# Signal received in thread: MainThread
