from typing import Callable
import functools


def check_permission(user: str) -> Callable:
    def permission(func: Callable) -> Callable:
        
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError - у пользователя недостаточно прав, '
                      f'чтобы выполнить функцию {func.__name__}')
            return func
        return wrapped
    return permission


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
