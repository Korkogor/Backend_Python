
def add(a: int, b: int) -> int:
    return a+b

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

logged_add = log_calls(add)
x = logged_add(2, b= 3)