'''Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
cost = 1000
discount = 10
>>> final = cost -((cost * discount))
>>> final
-9000
>>> cost = 1000
>>> discount = 0.1
>>> final = cost -((cost * discount))
>>> final
900.0
>>> price = 1000
>>> gst = 5
>>> final = price +((price*gst))
>>> final
6000
>>> price = 1000
>>> gst = 0.05
>>> final = price +((price * gst))
>>> final
1050.0
>>> price = 2000
>>> gst = 0.05
>>> discount = 0.05
>>> final = price - ((price * discount))+ price((price*gst))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    final = price - ((price * discount))+ price((price*gst))
TypeError: 'int' object is not callable
>>> price = 2000
>>> gst = 0.05
>>> discount = 0.05
>>> final = price -((price * discount))+gst
>>> final
1900.05
>>> final = final + (final * gst)
>>> final
1995.0525
>>> profit = 7000-5000
>>> profit
2000
>>> profit_percentage = ((7000-5000)/(5000))*100
>>> profit_percentage
40.0'''
s = input("Enter a string:")
words = s.split()

result = ""

for word in words:
    result = word + " " + result

print(result.strip())

































