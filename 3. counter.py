import time
from functools import wraps
times = int()
def counter(func):
    def wrapper(*args, **kwargs):
      global times
      times+=1
      print(f'Функция была вызвана:{times} раз')
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