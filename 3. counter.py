import time
from functools import wraps
times = int()
def counter(func):
    def wrapper(*args, **kwargs):
      global times
      times+=1
      print(f'Функция была вызвана:{times} раз')
    return wrapper
