'''Exception handling:An error can be handled by try and except
1.try:
--we can check the code here which may contains the errors
ex:
try:
    print(n)
except:
    print('some error')
2.except:
--exception can handle any error that come in the try block
eg1:
try:
    num = 0
    num_2 = 8
    print(num_2/num)
except:
    print('will get the error')

num = 8
num_2 = 0
print(num / num_2)
eg2:
try:
    any_ = int(input('Enter a number: '))
    print(any_+ 9)    
except:
    print('error')
eg3:
try:
    print(9+'python')    
except:
    print('error')

3.else:
--If no error in the code were raised, then the else
block will execute
eg1:
try:
    print(9+5)    
except:
    print('error')
else:
    print('no error')
eg2:
try:
    print('python' + 9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise TypeError')
else:
    print('no error')


4.finally:
--finally will execute if error present in
the try block or not
eg1:
try:
    print('python' + 9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise TypeError')
else:
    print('no error')
finally:
    print('end')
eg2:
try:
    print('Hello')
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise TypeError')
else:
    print('no error')
finally:
    print('end')

File Handling:
--An file handler is an object used to connect with
that particular file
1.with(keyword):
By using with keyword no need to close the file,
it will close it by itself
--by file name:
syntax:
with open('file_name or path','mode') as name:
--by filepath:
syntax:
with open(r'file_path','mode') as name:
ex:
with open('textfile.txt','r') as file_:
    print(file_.read())

2.open():
By using this open() we have to close the file by
using close()
eg:
any_ = open('textfile.txt','r')
print(any_.read())
any_.close()

Modes:
1.'r'-The 'r' mode is used for functions read(),readline() and readlines()
ex:
with open('textfile.txt','r') as file:
    print(file.read())
    
2.'w'-The 'w' mode is used for write() function
with open('textfile.txt','w') as file:
    print(file.write('Python is a very good language'))
    
3.'a'-The 'a' mode is used for write() function and it
will add the text at last position
with open('textfile.txt','a') as file:
    print(file.write('Python is a very good language'))

4.'x'-creating a file
with open('textfile2.txt','x') as file:
    file.write('Python is a very good language')

function:
1.write()
2.read():
The read() function will read the file chunk by chunk
where we can specify the size
ex:
with open('textfile2.txt','r') as file:
    print(file.read(20))

3.readline():
It will only read one line at a time
ex:
with open('textfile2.txt','r') as file:
    print(file.readline())
    
4.readlines()
The readlines() will read the whole file and written it in a
list,where each line is one index in the list
ex:
with open('textfile.txt','r') as file:
    print(file.readlines())






















    
