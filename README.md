<h1> 노트북 관련 매출 증가 및 주고객층 결정 리서치 분석 </h1>


<h3>노트북을 효율적으로 판매하고 재고를 최소화 하기 위해 네이버 데이터랩을 활용하여 분석해보았다.</h3>

 
<h4>1. 노트북 검색량이 가장 많은 시기는 언제인가?</h4>
<p> 1월부터 3월이 새학기라 남녀 노트북 검색량이 가장 많다 <br>
이 시기에 노트북을 구매하는 사람이 많을 것이라고 생각된다 <br>
 다른 월에 비해 납품을 더 많이 받아 더 많이 더 효율적으로 판매해보자</p>

 <h4>2.노트북 크기별 인기 및 선호도</h4>
<p>17인치 15인치 13인치를 비교해봤을때 17인치가 가장 인기가 많다 <br>
 그러므로 매장이나 쇼핑몰에 17인치를 가장 많이 노출시키는 것으로 하자</p>
 <h4>3. 의외의 결과</h4>
<p>여성과 남성의 노트북 검색량을 비교해봤을때 남성이 더 많이 검색한다는 결과를 얻었다<br>
 우리 매장은 온라인과 오프라인 매장을 동시에 운영할 것이기 떄문에 온라인에서는 남성을 타겟으로 잡을수 있는 게임용노트북이나 남성에게 인기가 많은 제품을
더 많이 전시하거나 판매하는 편이 나아보인다 <br>
 그러나 검색량이 많은 것 뿐이지 남성과 여성의 노트북 구매율은 비슷하다고 생각이든다 
 여성은 오프라인에서 더 많이 구매를 하는것으로 보이므로 오프라인에서는 여성에게 인기가 많은 제품을 전시하거나 판매를 하자</p>

<h4>4.노트북 악세사리 </h4>
<p>노트북 가방이나 악세사리는 7월8월9월에 비해 다른 달이 저조하므로 다른 달에는 노트북 가방을 할인해서 팔거나 이벤트를 하고
7월 8월 9월에는 노트북 가방이 검색량이 많으므로 노트북가방을 구매하는 고객에게 다른 노트북 악세사리를 판매할수 있도록 노력해보자
 노트북에 비해 노트북가방이나 악세사리 같은 경우는 남성에 비해 여성이 더 많은 검색을 한다고 보인다
 남성은 노트북만 구매하는 반면 여성은 노트북과 관련된 상품을 부가적으로 더 구매한다 이러한 점을 보았을때 남성이 좋아할만한 노트북 악세사리의 종류보다는
 여성이 선호할만한 악세사리를 더 많이 노출시키자
 
![image](https://user-images.githubusercontent.com/122436372/219250405-a5c7118a-50ab-4a8f-8c76-69216f22c4f4.png)
![image](https://user-images.githubusercontent.com/122436372/219250465-f15d9128-5f96-45e2-ab83-98c0381f51d5.png)
![image](https://user-images.githubusercontent.com/122436372/219250520-c0961d16-a156-479e-87b0-7c414e3a9f05.png) 
 
``` python
import csv
import matplotlib.pyplot as plt

#-------------------성별별 노트북 검색량----------------------------------------------------------
f=open(r'C:\webpython\day33\notebook.csv',encoding="utf-8")
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
plt.title("How many search 'Notebook'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date,mandata,label="Man, search 'Notebook'")
plt.plot(date,womandata,label="Woman, search 'Notebook'")
plt.legend()
#------------------인치별 노트북 가방 검색량------------------------------------------------------
f2=open(r'C:\webpython\day33\note.csv',encoding="utf-8")
data2=csv.reader(f2)
next(data2)
data17inch=[]
data15inch=[]
data13inch=[]
date2=[]

for row in data2:
    if row[1] !="":
        data17inch.append(float(row[1]))
    if row[2] !="":
        data15inch.append(float(row[2]))
    if row[3] !="":
        data13inch.append(float(row[3]))
    if row[0] !="":
        date2.append(row[0])

plt.subplot(222)
plt.title("How many search 'Notebookcase'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date2,data17inch,label='17inch case')
plt.plot(date2,data15inch,label='15inch case')
plt.plot(date2,data13inch,label='13inch case')
plt.legend()
#---------------------성별별 17인치 가방 검색량-------------------------------------------------
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
plt.title("How many search '17inch case'")
plt.xlabel("Date")
plt.ylabel("How many Search")
plt.plot(date3,mandata2,label="Man, search '17inch case'")
plt.plot(date3,womandata2,label="Woman, search '17inch case'")
plt.legend()
plt.show()
```
 



