class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class MyClass(metaclass=Singleton):
    def __init__(self, value):
        self.value = value


a = MyClass('23242423')
b = MyClass('sdfsfwef')

print(a.value)
print(b.value)
