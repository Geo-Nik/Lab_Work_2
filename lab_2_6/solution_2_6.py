'''
Write the code to do following:
1. Write a script that creates a new output file called myfile.txt
2. writes the string "Hello file world!" into it
3. write another code that opens myfile.txt in w+ mode
4. read and print its contents
5. write into “Hello file” string new value “my” – “Hello my file”
6. Save changes without file object close
'''

# 1. Write a script that creates a new output file called myfile.txt
inp=open('documents\myfile.txt','w')

#2. writes the string "Hello file world!" into it
inp.write('Hello file world!')
inp.close()

#3. write another code that opens myfile.txt in w+ mode
inp=open('documents\myfile.txt','r+')

#4. read and print its contents
print(inp.read())


#5. write into “Hello file” string new value “my” – “Hello my file”
inp.seek(len('Hello '))
inp.write('my file')
inp.flush()





