from functools import wraps
def logging(func):
  def wrapper(*args, **kwargs):
    print(f'Функция вызвана с параметрами:{args}, {kwargs}')
  return wrapper

@logging
def hi(n):
  print("Привет", n, "раз" )

hi(5, 6)

# Функция вызвана с параметрами:(5, 6), {}