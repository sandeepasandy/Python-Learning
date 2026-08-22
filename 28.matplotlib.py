'''matplotlib:
--This is an python library used to create graphs and charts

plot:
--The function can create a line graphs with the given data

xlabel:
--Used to represent the X-axis values

ylabel:
--Used to represent the Y-axis values

title
--To define the title of the graph

line graphs:
eg:
import matplotlib.pyplot as plt

marks = [55,90,56,70,100]
stu_=['Sandy','Prudhvi','Shalini','Priya','Sonu']
plt.plot(stu_,marks,color='pink')
plt.title('Students_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

bar graph:
--For horizontal graphs we can use--barh--
ex:
import matplotlib.pyplot as plt

sales = [55,90,56,70]
cars =['BMW','Nano','Swipf','Toyato']
plt.barh(cars,sales,color='pink')
plt.title('Car_sales')
plt.xlabel('Company names')
plt.ylabel('Number of sales')
plt.show()

Piechart:
ex:
import matplotlib.pyplot as plt
subjects=['Python','Java','C']
students=[55,36,25]
plt.pie(students,labels=subjects)
plt.title('Total students')
plt.legend(subjects)
plt.show()

Scatter graph:
--representing graph with dots
import matplotlib.pyplot as plt

stu_ = ['Sandy','Prudhvi','Shalini','Priya','Sonu']
marks = [55,90,56,70,100]
plt.scatter(stu_,marks,)
plt.title('Students_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

Histogram:
import matplotlib.pyplot as plt
sales = [890,150,800,1200]
plt.hist(sales)
plt.title('Sales_Hist')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

'''
import matplotlib.pyplot as plt
marks = [40,50,60,70,80,90]
plt.boxplot(marks)
plt.show()





























