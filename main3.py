import os
import types
from datetime import datetime as dt


def logger(path):
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='utf8') as log_file:
                print(f'{dt.now()} Вызов функции {old_function.__name__}', file=log_file)
                print(f'Аргументы позиционные: {args}', file=log_file)
                print(f'Аргументы именованные: {kwargs}', file=log_file)
                result = old_function(*args, **kwargs)
                print(f'Результат: {result}', file=log_file)
            return result

        return new_function

    return __logger

@logger('generator.log')
def flat_generator(list_of_lists):

    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()