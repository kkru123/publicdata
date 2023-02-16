import csv
import matplotlib.pyplot as plt

f=open(r'C:\webpython\day33\naver_datalab_shoppingInsight_category_월간_data_20230215154440.csv',encoding="utf-8")
data=csv.reader(f)
next(data)
mandata=[]
womandata=[]
date=[]
for row in data:
    if row[1] !="":
        mandata.append(float(row[1]))
    if row[2] !="":
        womandata.append(float(row[2]))
    if row[0] !="":
        date.append(row[0])


plt.subplot(221)
plt.xlabel("date")
plt.ylabel("Search")
plt.plot(date,mandata,label='mandata')
plt.plot(date,womandata,label='womandata')
plt.legend()
# plt.show()
#-----------------------------------------------------------------------------------------------
f2=open(r'C:\webpython\day33\note.csv',encoding="utf-8")
data2=csv.reader(f2)
next(data2)
data17=[]
data15=[]
data13=[]
date2=[]
for row in data2:
    if row[1] !="":
        data17.append(float(row[1]))
    if row[2] !="":
        data15.append(float(row[2]))
    if row[3] !="":
        data13.append(float(row[3]))
    if row[0] !="":
        date2.append(row[0])

plt.subplot(222)
plt.xlabel("date")
plt.ylabel("Search")
plt.plot(date2,data17,label='data17')
plt.plot(date2,data15,label='data15')
plt.plot(date2,data13,label='data13')
plt.legend()
#-----------------------------------------------------------------------------------------------
f3=open(r'C:\webpython\day33\17in.csv',encoding="utf-8")
data3=csv.reader(f3)
next(data3)
mandata2=[]
womandata2=[]
date3=[]
for row in data3:
    if row[1] !="":
        mandata2.append(float(row[1]))
    if row[2] !="":
        womandata2.append(float(row[2]))
    if row[0] !="":
        date3.append(row[0])

plt.subplot(223)
plt.xlabel("date")
plt.ylabel("Search")
plt.plot(date3,mandata2,label='mandata17')
plt.plot(date3,womandata2,label='womandata17')
plt.legend()
plt.show()