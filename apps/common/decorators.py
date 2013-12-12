# coding: utf-8


def attr_decorator(**attrs):
    """
        Decorator para adicionar atributos para funções.
        Um caso de uso são para metodos do admin que precisam
        de alguns atributos especiais.

        Metódo normal:

            def url(self, obj):
                ...
            url.short_description = 'show url'
            url.allow_tags = True

        Metódo decorado:

            @attr_decorator(short_description='show url', allow_tags=True)
            def url(self, obj):
                ...
    """
    def wrapper_func(func):
        def new_func(*args, **kwargs):
            return func(*args, **kwargs)
        for attr, value in attrs.items():
            setattr(new_func, attr, value)
        return new_func
    return wrapper_func
