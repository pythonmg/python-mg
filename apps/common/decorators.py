# coding: utf-8


def attr_decorator(**attrs):
    def wrapper_func(func):
        def new_func(*args, **kwargs):
            return func(*args, **kwargs)
        for attr, value in attrs.items():
            setattr(new_func, attr, value)
        return new_func
    return wrapper_func
