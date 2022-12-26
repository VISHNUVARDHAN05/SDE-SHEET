from _collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v,cost):
        self.graph[u].append([v,cost])
        self.graph[v].append([u, 1/cost])


'''import requests
key="AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"
url="http://www.mapquestapi.com/geocoding/v1/address?"
loc="3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008"
main_url=url+key+'&location='+loc#key=KEY&location=Washington,DC"
temp=loc.replace(" ","+")
'''
for i in loc:
    if i==" ":
        temp=temp+"+"
        continue
    temp=temp+i
'''
url="https://maps.googleapis.com/maps/api/geocode/json?address="+temp+"&key="+key
r=requests.get(url)
data=r.json()
x=data["results"][0]['geometry']['location']
print(x)
print(data)
'''


#https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=