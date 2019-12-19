import matplotlib.pyplot as plt 
import pandas  as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup


url2019 = requests.get('https://rs.2019seagames.com/RS2019/mobiapp/MedalTally')
data1 = BeautifulSoup(url2019.content,'html.parser')

temp = []
for i in data1.find_all('small'):
    temp.append(i.text)
print(temp)

medali1 = []
for i in range(0,len(temp),5):
    a = temp[i:i+5]
    medali1.append(a)
judul1 = medali1[0]
isi1 = medali1[1:]
print(judul1)

dict_medal = []
for i in isi1:
    dict_medal.append(dict(zip(judul1,i)))

df_2019 = pd.DataFrame(dict_medal)
df_2019 = df_2019.sort_values(by=['Contingent'])
print(df_2019)

# sea games 2017
url = 'https://www2.2019seagames.com/countries/'
web = requests.get(url)
data = BeautifulSoup(web.content, 'html.parser')
# nd = data.findAll('em')
# print(nd)

lem = []
for i in data.find_all('em'):
    lem.append(i.text)
print(lem)

lembar = []
for i in range(0,len(lem),6):
    lembar.append(lem[i:i+6])
# print(lembar)
# print(len(lembar))

lembar = []
for i in range(0,len(lem),6):
    lembar.append(lem[i:i+6])
print(lembar)
lembarx = lembar[0:11]
print(lembarx)

negara = []
for i in isi1:
    negara.append(i[0])
negara = sorted(negara)
print(negara)

medali = []
for i in range(0,len(lembar),1):
    # lembar = int(lembar[i][2][6:10])
    medali.append(lembar[i][2][6:10])
print(medali)

medalidone = []
for i in range(len(medali)):
    new = int(medali[i])
    medalidone.append(new)
print(medalidone)
medald = medalidone[0:11]
print(medald)

medal_2017 = []
for i in range(len(negara)):
    medal_2017.append([negara[i],medald[i]])
print(medal_2017)
jdul2017 = ['Country','Gold']
data17 = []
for i in medal_2017:
    data17.append(dict(zip(jdul2017,i)))
# print(data17)
df_2017 = pd.DataFrame(data17)
df_2017 = df_2017.sort_values(by=['Country'])
print(df_2017)
print(df_2019)
df_2019['Gold'] = df_2019['Gold'].astype(int)

# # Plot 2017 & 2019

plt.style.use('seaborn')
plt.figure('sea games',figsize=(16,6))
plt.plot(df_2017['Country'],df_2017['Gold'],label='Gold 2017',marker='o',color='red',zorder=2)
plt.plot(df_2019['Contingent'],df_2019['Gold'],label='Gold 2019',marker='o',color='green',zorder=2)
plt.scatter([4,6],[145,149],marker='*',color='goldenrod',s=500,zorder = 4,label='Champion')
plt.yticks(range(0,161,20))
plt.xticks(size=7)
plt.title('GOLD MEDAL TALLY SEA GAMES 2017 & 2019')
plt.legend()
# plt.savefig('plot.png')
plt.show()


# # Pie chart


plt.figure(figsize=(16,8))
plt.subplot(122)
plt.title('Gold % SEA Games 2019')
plt.pie(df_2019['Gold'],labels=df_2019['Contingent'],autopct='%1.1f%%',startangle=90,colors=['cornflowerblue','mediumseagreen','indianred','slateblue','goldenrod','lightblue'])

plt.subplot(121)
plt.title('Gold % SEA Games 2017')
plt.pie(df_2017['Gold'],labels=df_2017['Country'],autopct='%1.1f%%',startangle=90,colors=['cornflowerblue','mediumseagreen','indianred','slateblue','goldenrod','lightblue'])
plt.suptitle('Gold SEA Games 2017 & 2019')
plt.savefig('pie.png')
plt.show()