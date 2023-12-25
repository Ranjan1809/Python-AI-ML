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
print(file.readlines())

file.close()
file2.close()
