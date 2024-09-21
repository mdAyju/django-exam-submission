from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

import time


# By default, Django signals are executed synchronously.
# This means that when a signal is sent, the receivers are called immediately within the same process flow, 
# without blocking the execution until the signal handlers are done.



@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal received.")
    time.sleep(5)  # Sleep to simulate time-consuming task
    print("Signal finished processing.")

# Creating a new user will trigger the signal
User.objects.create(username='test_user')
print("After User creation.")
