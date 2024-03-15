import time
from functools import wraps
def benchmark(func):
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f'Время выполнения функции {func.__name__}: {end - start:.6f}')
    return result
  return wrapper

@benchmark
def hi(n):
  print("Привет", n, "раз" )

hi(5)

# Привет 5 раз
# Время выполнения функции hi: 0.007201