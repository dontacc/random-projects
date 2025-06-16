from celery import shared_task


@shared_task
def say_my_name():
    print("my name is arian")
