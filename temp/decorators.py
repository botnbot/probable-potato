# from  pathlib import Path
# from src.config import ROOT_PATH
from typing import Any
def log(filename: Any = None) -> Any:
    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                raise

        return wrapper

    return decorator


# print(f"ROOT_PATH is set to: {ROOT_PATH}")
#
@log(filename="test.log")
def my_function(x, y):
    return x / y

result = my_function(4, 2)
print(result)
