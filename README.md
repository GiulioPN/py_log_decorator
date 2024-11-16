# Python Decorator Example: Function Execution Time Logger

A practical example of Python decorators, demonstrated through a Monte Carlo π estimation script. This project focuses on showing how to create and use decorators for logging execution time of functions.

## Key Focus: The Decorator Pattern

The main purpose of this project is to demonstrate how to:

1. Create a parameterized decorator
2. Use it to measure and log function execution time
3. Implement proper logging practices within decorators

### Decorator Implementation

```python:decorators.py
def log_execution_time(operation_name: str, logger: logging.Logger = app_logger):
    """Decorator to log the execution time of a function."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            execution_time = end_time - start_time
            logger.info(f"{operation_name} execution time {execution_time}")
            return result
        return wrapper
    return decorator
```

Note that the `@functools.wraps(func)` decorator is used to preserve the metadata of the decorated function. For example, without it, the `__name__` attribute of the decorated function would be `wrapper`:

```python
>>> estimate_pi.__name__
'wrapper'
```

### Using the Decorator

The decorator can be applied to any function to log its execution time:

```python:script.py
@log_execution_time(operation_name="estimate_pi")
def estimate_pi(num_points: int = 1000) -> float:
    # Function implementation
    ...
```

## Project Structure

- `decorators.py` - Contains the execution time logging decorator
- `logger.py` - Logger
