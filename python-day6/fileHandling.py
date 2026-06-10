#read whole file
#opening
file=open("student.csv","r")
#reading
content=file.read()
#displaying
print(content)
#closing
file.close()

#read 1 line at once as string
file=open("student.txt","r")
read_line=file.readline()
print(read_line)

#read all lines as list of string
read_lines=file.readlines()
print(read_lines)