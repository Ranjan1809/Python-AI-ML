# This is a demo of processing file before using
"""Reason for processing before use is that some data may be missing ,
data might be non-uniform,etc.
So it's good to process before using the file."""

# Example in loans2.txt file is that it has missing down_payment values

from urllib.request import urlretrieve

url1 = ('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw'
        '/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt')
url2 = ('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw'
        '/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt')
url3 = ('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw'
        '/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt')

urlretrieve(url3, 'myLoan2.txt')


def parse_headers(header_line):
    return header_line.strip().split(',')


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values


with open('./myLoan2.txt') as file2:
    file2_contents = file2.readlines()

print(file2_contents)

headers = parse_headers(file2_contents[0])
print(headers)

val = parse_values(file2_contents[2])
print(val)
