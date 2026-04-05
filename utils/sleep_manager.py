import time
import random


def random_sleep(min_sec=1, max_sec=3):
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)

def short_sleep():
    random_sleep(0.5, 1.2)

def medium_sleep():
    random_sleep(1, 3)

def long_sleep():
    random_sleep(2, 5)