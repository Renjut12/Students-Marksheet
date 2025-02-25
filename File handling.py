
'''........FILE HANDLING...........'''

# text files - txt , py , html , java
# binary files   - image files - png , jpeg , GIF , video files - mp4 , audio files - mp3, document files - pdf



'''All binary files follows a specific format we can open some binary files in the normal text editor ,
but we can't read the content present inside the file that's because all the binary files will be encoded
in the binary format which can understood only by a computer or machine, 
for handling such binary files we need a specific type of software opening.....
Text file don't have any specific encoding and it can be opened in normal text editor itself...'''

'''........Mode : what operations do want to do on a file.................'''

# Handling operation

# open()
# read()
# write()
# close()

# Other operations

# rename()
# delete()

# varname = open(filename,mode)
# r-readmode-it is used only to read data from the file (default)
# w-writemode-write data into the file
# a-append-used to append data to the file-data will append at the end of the file,create the file if it does not exists 
# x-create file
# r+ - read or write
# a+ - append or read
# rt-read text file
# rb-read binary file
# wb - write binary mode
# ab - append binary mode


'''.....Open and Read : To open the file use the built-in open function - open(), 
The read method - read() - is used for reading the content of the file,
if the file is located in a different location you will have specified the file path...........'''

# f = open("Math.py","r")        ( if the files are in same directory )
# print(f.read())
# f.close()

'''read only parts of a file : you can also specify how many characters you want to return'''

# f = open("Introduction.py","rt")    ( if the files are in same directory )
# print(f.read(5))
# f.close()

'''.....readline() : you can return one line by using this method, by calling two times you can read the two first lines....'''

# f = open("D:/Quis_works/Basic prgming Questions/Function/Odd or even.py","rt")    # ( if the files are in same directory )
# print(f.readline())
# print(f.readline())
# f.close()

'''....write - will overwrite any existing content.... '''
# f = open ("abc.txt","w")
# f.write("Good afternoon")
# f.close()

'''.....will create a file if the specified file does not exist....'''

# f = open("abcd.txt","w")
# f.write("Good evening")
# f.close()

'''......... a - append will append to the end of the file....... '''

# f = open("abc.txt","a")
# f.write("\n Good morning")
# f.close()

'''.......It will create a file if the file does not exist'''

# f = open("xyz.txt",'a')
# f.write("Malayalam")
# f.close()

'''...... x - will create a file , return an error if the file existing....'''

# f = open("vxn.py","x")   
# f.close()

# Traceback (most recent call last):
#   File "D:\Quis_works\Basic prgming Questions\Files\File handling.py", line 88, in <module>
#     f = open("vxn.py","x")
# FileExistsError: [Errno 17] File exists: 'vxn.py'


# import os

'''.......... rename - rename the file...............'''

# os.rename("four.py","fiver.py")

'''.........remove  - to delete a file..........'''

# os.remove("new.py")

'''.......rmdir......'''

# import os
# os.rmdir("hello")

