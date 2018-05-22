# Sample to read numbers from a text file and write the sum into another.


def summary():
    source_path = './data/source.txt'
    dest_path = './data/dest.txt'

    with open(source_path, 'r') as source_file:
        numbers = source_file.read().split('\n')
        print(numbers)

    with open(dest_path, 'w') as dest_file:
        dest_file.write(str(sum(map(lambda x: int(x), numbers))))


summary()
