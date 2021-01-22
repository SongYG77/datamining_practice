import folium
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from matplotlib import font_manager , rc
rc('font', family = 'gulim')

def locationset(location) :
    global data2
    if location == '충북' :
        rt_num = len(data2.query("주소.str.contains('충북') or 주소.str.contains('충청북도')"))
    elif location == '충남' :
        rt_num = len(data2.query("주소.str.contains('충남') or 주소.str.contains('충청남도')"))
    elif location == '전북' :
        rt_num = len(data2.query("주소.str.contains('전북') or 주소.str.contains('전라북도')"))
    elif location == '전남' :
        rt_num = len(data2.query("주소.str.contains('전남') or 주소.str.contains('전라남도')"))
    elif location == '경북' :
        rt_num = len(data2.query("주소.str.contains('경북') or 주소.str.contains('경상북도')"))
    elif location == '경남' :
        rt_num = len(data2.query("주소.str.contains('경남') or 주소.str.contains('경상남도')"))
    return rt_num

all_locations = []
optionlst = ['충북','충남','전북','전남','경북','경남']
map = folium.Map(location=[37.566651, 126.978428], zoom_start=10)
data = pd.read_csv('camping_loc.csv',  encoding='CP949')
locname = data['주소']
data2 = data.filter(['캠핑(야영)장명','위도','경도','주소'])
data2['주소'] = data2['주소'].astype(str)
for i in data2.index:
    name = data2.loc[i,'캠핑(야영)장명']
    lat = data2.loc[i,'위도']
    lng = data2.loc[i,'경도']
    location = data2.loc[i,'주소']
    temp = location.split()
    location = temp[0]
    all_locations.append(location)
    marker = folium.Marker([lat,lng],popup=name)
    marker.add_to(map)

map.save('지도표시.html')
jfile = json.load(open('TL_SCCO_CTPRVN.json',encoding='utf-8'))
print(set(all_locations))
#{'경기','전라북도', '강원도', '경남', '제주특별자치도', '경상북도', '충청북도', '충북', '경기도', '경상남도', '전북', '충남', '강원', '경북', '제주시', '전라남도','충청남도', '전남', '제주도'}
location = ['경기','강원','충북','충남','전북','전남','경북','경남','제주']
count = []
for i in location :
    if i in optionlst : tempnum = locationset(i)
    else : tempnum = len(data2.query("주소.str.contains('경남') or 주소.str.contains('경상남도')"))
    count.append(tempnum)
df = pd.DataFrame({'Location': location,'Count' : count})
sns.barplot(
    data= df,
    x= "Location",
    y= "Count"
)
plt.show()
