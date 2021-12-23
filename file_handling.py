# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will not be deleted.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.


# open() function
file = open('file.txt', 'r')

for each in file:
    print(each)

# read() function
file = open('file.txt', 'r')
print(file.read())

# <-------------------------------------->
with open("file.txt") as file:
    data = file.read()
print(data)

# write() function
file = open('file.txt', 'w')
file.write("this is write command")
file.write("it allows us to write in a particular file")
file.close()

# <------------------------------------------->

with open("file.txt", "w") as f:
    f.write("hello world")

# append()
file = open("file.txt", "a")
file.write("this will add this line")
file.close()

# split function
with open("file.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# wap to read one files and copy the content in other file
f1 = open("file.txt")
f2 = open("file1.txt", "w+")

f2.write(f1.read())
f2.seek(0, 0)
print(f2.read())

# wap to read 2 files and copy the content in 3rd file
f1 = open("file.txt")
f2 = open("file1.txt")
f3 = open("file2.txt", "w+")
f3.write(f1.read())
f3.write(f2.read())
f3.seek(0, 0)
print(f3.read())

# no of character in file

f = open("file.txt", "r")
number_of_words = 0
number_of_char = 0
number_of_lines = 0
for line in f:
    number_of_lines += 1
    line = line.strip("\n")
    number_of_char += len(line)
    list1 = line.split()
    number_of_words += len(list1)
f.close()
print(number_of_words, number_of_char, number_of_lines)
