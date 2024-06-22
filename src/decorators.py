def log(filename = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, 'a') as log_file:
                        log_file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}"\n')
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
        return wrapper
    return decorator

@log(filename="log_file.txt")
# @log
def my_function(x, y):
    return x + y
print(my_function("1", "3"))