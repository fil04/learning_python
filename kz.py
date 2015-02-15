from __future__ import unicode_literals


def fer(data):
    def wrapped1(func):
        def wrapped2():
            if data == 'second text':
                return '<div>' + func() + '</div>'
            return func()
        return wrapped2
    return wrapped1

@fer('second')
def custom_func():
    return ' fksdh fksdh kfhsdkh f'

# print(fer('second')(custom_func)())

print(custom_func())

# custom_func('dfsdjhfkjsdh')

