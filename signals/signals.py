from django.dispatch import Signal
from django.dispatch import receiver
from authentication.models import User
from django.db.models.signals import post_save

notify = Signal()


# @receiver(notify)
def user_created_log(sender, **kwargs):
    print("user created")


@receiver(post_save, sender=User)
def after_user_created(sender, **kwargs):
    User.objects.get(usernamee="arian")
    print("user created successfully")
