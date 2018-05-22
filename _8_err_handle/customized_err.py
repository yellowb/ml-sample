# Sample of customized Errors


# my own error
class MyError(ValueError):
    pass


def calculate(x, y):
    if y == 0:
        raise MyError('This is a customized error with value = %d' % y)
    else:
        return x / y


def main():
    try:
        result = calculate(10, 0)
        print('result = ' + result)
    except MyError as e:
        print('Oh we encounter error!')
        print(e)
    finally:
        print('final block done!')


main()
