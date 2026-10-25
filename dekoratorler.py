import functools
import time 

def sure_olc(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end - start:.4f} sn")
        return result
    return wrapper




def say(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)
    wrapper.cagri =0
    return wrapper

def log_cagri(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"-> {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print (f"<- {func.__name__} = {result!r}")
        return result
    return wrapper


def sinirla(alt, ust):
    def dekorator(func):
        @functools.wraps(func)
        def wrapper(ilk_arg, *args, **kwargs):
            if not (alt <= ilk_arg <= ust):
                raise ValueError(f"{func.__name__}: {ilk_arg} değeri {alt}-{ust} aralığında değil")
            return func(ilk_arg, *args, **kwargs)
        return wrapper
    return dekorator


def hafiza(maxisize=None):
    def dekorator(func):
        cache = {}
        keys_order = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                if maxisize is not None:
                    keys_order.remove(key)
                    keys.order.append(key)
                return cache[key]
            result= func(*args, **kwargs)
            if maxsize is not None:
                if len(cache) >= maxsize:
                    oldest_key = keys_order.pop(0)
                    del cache[oldest_key]
                keys_order.append(key)
            cache[key] = result
            return result
        return wrapper
    return dekorator



    