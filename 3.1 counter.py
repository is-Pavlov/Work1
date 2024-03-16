import time
from functools import wraps
times = int()
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} Функция была вызвана:{1}x" . format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
def hi(n):
  print("Привет", n, "раз" )

hi(5)
hi(5)
hi(5)

# Функция была вызвана:1 раз
# Функция была вызвана:2 раз
# Функция была вызвана:3 раз