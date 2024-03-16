from functools import wraps
def logging(func):
  def wrapper(*args, **kwargs):
    print(f'Функция вызвана с параметрами:{args}, {kwargs}')
  return wrapper