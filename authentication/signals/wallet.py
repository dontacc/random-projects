from django.dispatch import receiver
from django.dispatch import Signal
from django.db.models.signals import pre_save, post_save, post_delete
from authentication.models import Wallet

notify = Signal()


@receiver(notify)
def wallet_notification_handler(sender, **kwargs):
    sender.update(is_active=True)
    # for wallet in sender:
    #     wallet.is_active = Truew
    # Wallet.objects.bulk_update(sender, ["is_active"])


@receiver([post_save, post_delete], sender=Wallet)
def invalidated_cache(sender, instance, **kwargs):
    print("Cache updated")
