# Sample of try-except-finally usage with built-in Errors


def calculate(x, y):
    return x / y


def main():
    try:
        result = calculate(10, 0)
        print('result = ' + result)
    except ZeroDivisionError as e:
        print('Oh we encounter zero div!')
        print(e)
    finally:
        print('final block done!')


main()
