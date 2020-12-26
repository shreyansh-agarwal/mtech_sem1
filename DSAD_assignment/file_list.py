with open("inputps9.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)



text_file = open("inputps9.txt", "r")
lines = text_file.readlines()

print(lines)
print(len(lines))


mylines = []                              # Declare an empty list
with open ('inputps9.txt', 'rt') as myfile:  # Open file lorem.txt
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:               # For each element in the list,
        print(element, end='')


