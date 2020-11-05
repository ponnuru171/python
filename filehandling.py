"""
file operations:
1.open a file.
2.read and write.
3.close a file.
file modes :
1.'r' open a file for reading(defalt)
2.'w' write,creates a new file if it doesn't exists
3.'x' exclesive creation,if the file already exists the operation fails
4.'a' append, creates file if doesn't exist
5.'t' textmode(default mode)
6.'b' binary
7.'+' reading and writting
"""
f=open('f1.txt','r')
print(f.read(6))
print(f.tell())
print(f.seek(0))
print(f.read())
f.close()
