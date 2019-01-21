
def route(**kwargs):

    # ['GET', 'POST']
    method = kwargs.method

    def wrapper(func):

        def inner_warpper(*args, **kwargs):

            return func(method, *args, **kwargs)

        return inner_warpper

    return wrapper



