import matplotlib.pyplot as plt
import pandas as pd
import math

data = pd.read_csv("cgpa.csv")
cgpa = data["cgpa"]
package = data['package']

''' TRAINING
Calculating slope 'm'
 x axis = cgpa
 y axis = package'''
sum_of_x = 0
sum_of_y = 0
total_elements = 0

for line in cgpa:
    sum_of_x += cgpa[total_elements]
    sum_of_y += package[total_elements]
    total_elements += 1


xmean = sum_of_x/total_elements
ymean = sum_of_y/total_elements

numerator = 0
denoinator = 0

for i in range(total_elements):
    numerator += (cgpa[i]-xmean)*(package[i]-ymean)
    #denoinator += (i['cgpa']-xmean) * (i['cgpa']-xmean)
    denoinator += pow((cgpa[i]-xmean),2)

m = numerator/denoinator

#calculating b or c(y intercept)

b = ymean-(m*xmean)

# TESTING
x = [1,2,3,4,5,6,7,8,9,10]#cgpa
y = []#package
for i in x:
    y.append(m*i+b)

# print("m = ",m)
# print("b = ",b)
# print(m*8.58+b)

plt.scatter(cgpa,package) #for scatter plot
plt.plot(x,y,color = 'red') #for the line graph
plt.xlabel('CGPA')
plt.ylabel('PACKAGE')
plt.show()