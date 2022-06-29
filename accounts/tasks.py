from celery import shared_task
import time


@shared_task
def hello2():
    time.sleep(5)
    print(f"Hello, world2! - task sucess {time.time()}")


@shared_task
def hello3():
    time.sleep(8)
    print('Hello, world3!')
