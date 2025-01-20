from celery import shared_task


@shared_task
def feed_hamster():
    print("Feeding the hamster")
    return "Feeding the hamster"
