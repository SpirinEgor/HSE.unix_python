from datetime import datetime


def safe_history_saving(_object, attribute_name, history_value):
    if not hasattr(_object, attribute_name):
        setattr(_object, attribute_name, [])
    getattr(_object, attribute_name).append(history_value)


def spy(function):
    def wrapper(*args, **kwargs):
        setattr(wrapper, "__is_decorated", True)
        current_time = datetime.now()
        safe_history_saving(wrapper, "__call_time", current_time)
        safe_history_saving(wrapper, "__passed_args", args)
        safe_history_saving(wrapper, "__passed_kwargs", kwargs)
        wrapper.__name__ = function.__name__
        return function(*args, **kwargs)
    return wrapper


def bond(function):
    is_decorated = getattr(function, "__is_decorated", False)
    if not is_decorated:
        raise TypeError(f"{function.__name__} was not decorated with @spy decorator")
    call_time = getattr(function, "__call_time", None)
    if call_time is None:
        raise TypeError(f"You should call function at least one time")
    passed_args = getattr(function, "__passed_args", [])
    passed_kwargs = getattr(function, "__passed_kwargs", [])
    return zip(call_time, map(lambda _a, _k: f"args: {_a}; kwargs: {_k}", passed_args, passed_kwargs))


@spy
def foo(num):
    print(num)


foo(3)
foo("hello")
foo(5)
foo(num=10)

for (time, parameters) in bond(foo):
    print(time)
    print(parameters)
