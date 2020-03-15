
import os
import sys
import functools
import create_logger
from timeit import default_timer as timer


def exception_(logger):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except:
                err = "Exception in "
                err += fn.__name__
                logger.exception(err)
            raise
        return wrapper
    return decorator


def time_(logger):
    """Decorator for logging the amount of time a function takes to run.
    :param fn: function to decorate
    """
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = timer()
            result = fn(*args, **kwargs)
            end = timer()
            duration = float(f'{((end - start) / 60.0):.2f}')
            logger.info(' %s ran for: %f minutes', fn.__name__, duration)
            return result
        return wrapper
    return decorator


def generic_log(fn):
    fn1 = log_time(fn)
    fn3 = log_exception(fn)
    return fn