# opens file in read mode
# There are 4 modes -> r-read , w-write , a-append , r+ read-write
file = open("read.txt", "r")

# Be cautious while using write mode as it will overwrite the existing contents
file2 = open("write.txt", "w")

file2.write("This is written using write mode of file. Thank you.")

# checks whether file is in read mode or not
# print(file.readable())

# reads all the contents of file
# print(file.read())

# This reads one line at a time
# print(file.readline())

# displays array of lines  ['    This file is for practicing of read and write operations\n', '    Line 1
# ...\n', '    Line 2 ...\n', '    Line 3 ....\n', '    End of contents']
# print(file.readlines())
stripped = file.readlines()

# The strip method removes any extra spaces and the newline character \n.
# readlines always produces \n in output after it finishes reading each line
print(stripped[0].strip())


# you need to close the files because when it is opened, those files are put into RAM.
# So if they are kept open, it might slow down things
# Hence need to close the files after work is done
# You will not be able to perform any of the above operation once the file is closed
file.close()
file2.close()

# To close a file automatically after you've processed it, you can open it using the with statement.

with open('./read.txt') as file2:
    file2_contents = file2.read()
    print(file2_contents)

# advantage of using with is that it closes the file automatically
# displays ValueError: I/O operation on closed file.

'''Once the statements within the `with` block are executed, the `.close` method on `file2` is automatically invoked. 
Let's verify this by trying to read from the file object again.'''
# print(file2.read())
