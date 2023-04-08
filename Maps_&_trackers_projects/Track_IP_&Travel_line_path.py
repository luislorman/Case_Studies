#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[1]:


import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance


# The below function is used to print the details of the IP address line City, Country, Coordinates, etc.

# In[2]:


def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


# Getting the Location from an IP Address
#  

# In[3]:


ip_add = input("Enter IP: ")  
detailedprint = printDetails(ip_add) # normal Print doesnt show all the data


# In[7]:


type(detailedprint) # dont know why it says that is NoneType


# In[8]:


detailedprint


# In[ ]:





# ### Generates string variables from the IP for Lat and Lng, which is not possible in the formula from above

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## In cities, the location is not accurate

# ### Showing map without exporting file

# In[9]:


import folium
from IPython.display import HTML

Location = "Berlin"
Lat = 52.5103817
Lng = 13.4349112

myMap= folium.Map(location= [Lat, Lng], zoom_start=9)
folium.Marker([Lat, Lng],popup=Location).add_to((myMap))

HTML(myMap._repr_html_())


# In[ ]:





# ### Export map in html file within folder 

# In[10]:


import folium
from IPython.display import HTML

Location = "Berlin"
Lat = 52.5103817
Lng = 13.4349112

myMap= folium.Map(location= [Lat, Lng], zoom_start=9)
folium.Marker([Lat, Lng],popup=Location).add_to((myMap))

myMap.save('map.html')
HTML('<iframe src=map.html width=700 height=450></iframe>')


# In[ ]:





# ## Find location with URL

# In[20]:


url = input("Enter URL: ")  # www.youtube.com, www.kdnuggets.com 
ip_add = socket.gethostbyname(url)
printDetails(ip_add) # Before input check spaces


# In[ ]:





# In[8]:


# Find IP address from phone number is not possible, but you can access through the mobile to the Wifi that is at that moment connected and in  details see IP.
#If someone gives me its IP Wifi then I can localize 


# In[ ]:





# In[ ]:





# ## Showing more than one location at the same time in maps

#  It shows firstly in a close view the Location1, to see the other locations show must move away from the original point until seeing the world

# In[15]:


import folium
from IPython.display import HTML

Yo = "yo"
Location1 = "Berlin"
Lat1 = 52.5103817
Lng1 = 13.4349112

Kdnuggets = "kdnuggets"
Location2 = "San Francisco"
Lat2 = 37.776547
Lng2 = -122.39483705092607

myMap = folium.Map(location=[Lat1, Lng1], zoom_start=9)
folium.Marker([Lat1, Lng1], popup=f"{Location1}, {Yo}").add_to(myMap)
folium.Marker([Lat2, Lng2], popup=f"{Location2}, {Kdnuggets}").add_to(myMap)

HTML(myMap._repr_html_())


# # TODO - poner disntintos puntos de direcciones y hacer un map de lines marcando las rutas de abastecimiento
# 
# ## Caso: ruta de transporte desde coruna hasta berlin

# coruna: 
# Latitude: 43.362343
# Longitude: -8.411540
# 
# leon
# Latitude: 42.605556
# Longitude: -5.570000
# 
# logrono
# Latitude: 42.465000
# Longitude: -2.445556
# 
# san sebastian
# Latitude: 43.312691
# Longitude: -1.993332
# 
# bordeux
# Latitude: 44.836151
# Longitude: -0.580816
# 
# orleans
# Longitude: 1.909000
# Latitude: 47.902500
# 
# 
# metz
# Latitude: 49.120277
# Longitude: 6.177778    
# 
# frankfurt am main
# Latitude: 50.110924
# Longitude: 8.682127
# 
# leipzig
# Latitude: 51.340199
# Longitude: 12.360103
# 
# 
# berlin
# Longitude: 13.381777
# Latitude: 52.531677

# ### Several labels across the map

# In[16]:


import folium
from IPython.display import HTML

#Yo = "yo"
Location1 = "Berlin"
Lat1 = 52.531677
Lng1 = 13.381777

#Kdnuggets = "kdnuggets"
#Location2 = "San Francisco"
#Lat2 = 37.776547
#Lng2 = -122.39483705092607

Location3 = "Coruna"
Lat3 = 43.362343
Lng3 = -8.411540

Location4 = "Leon"
Lat4 = 42.605556
Lng4 = -5.570000

Location5 = "Logrono"
Lat5 = 42.465000
Lng5 = -2.445556

Location6 = "San Sebastian"
Lat6 = 43.312691
Lng6 = -1.993332

Location7 = "Bordeaux"
Lat7 = 44.836151
Lng7 = -0.580816

Location8 = "Orleans"
Lat8 = 47.902500
Lng8 = 1.909000

Location9 = "Metz"
Lat9 = 49.120277
Lng9 = 6.177778

Location10 = "Frankfurt"
Lat10 = 50.110924
Lng10 = 8.682127

Location11 = "Leipzig"
Lat11 = 51.340199
Lng11 = 12.360103

myMap = folium.Map(location=[Lat1, Lng1], zoom_start=5)
folium.Marker([Lat1, Lng1], popup=f"{Location3}").add_to(myMap)
#folium.Marker([Lat2, Lng2], popup=f"{Location2}, {Kdnuggets}").add_to(myMap)
folium.Marker([Lat3, Lng3], popup=f"{Location3}").add_to(myMap)
folium.Marker([Lat4, Lng4], popup=f"{Location4}").add_to(myMap)
folium.Marker([Lat5, Lng5], popup=f"{Location5}").add_to(myMap)
folium.Marker([Lat6, Lng6], popup=f"{Location6}").add_to(myMap)
folium.Marker([Lat7, Lng7], popup=f"{Location7}").add_to(myMap)
folium.Marker([Lat8, Lng8], popup=f"{Location8}").add_to(myMap)
folium.Marker([Lat9, Lng9], popup=f"{Location9}").add_to(myMap)
folium.Marker([Lat10, Lng10], popup=f"{Location10}").add_to(myMap)
folium.Marker([Lat11, Lng11], popup=f"{Location11}").add_to(myMap)

HTML(myMap._repr_html_())


# In[ ]:





# ### Two different routs labelled by lines

# In[17]:


import folium
from IPython.display import HTML


#First Route
#Yo = "yo"
Location1 = "Berlin"
Lat1 = 52.531677
Lng1 = 13.381777

#Kdnuggets = "kdnuggets"
#Location2 = "San Francisco"
#Lat2 = 37.776547
#Lng2 = -122.39483705092607

Location3 = "Coruna"
Lat3 = 43.362343
Lng3 = -8.411540

Location4 = "Leon"
Lat4 = 42.605556
Lng4 = -5.570000

Location5 = "Logrono"
Lat5 = 42.465000
Lng5 = -2.445556

Location6 = "San Sebastian"
Lat6 = 43.312691
Lng6 = -1.993332

Location7 = "Bordeaux"
Lat7 = 44.836151
Lng7 = -0.580816

Location8 = "Orleans"
Lat8 = 47.902500
Lng8 = 1.909000

Location9 = "Metz"
Lat9 = 49.120277
Lng9 = 6.177778

Location10 = "Frankfurt"
Lat10 = 50.110924
Lng10 = 8.682127

Location11 = "Leipzig"
Lat11 = 51.340199
Lng11 = 12.360103


#Second Route

Location1a = "Athens"
Lat1a = 37.983810
Lng1a = 23.727539

Location2a = "Thessaloniki"
Lat2a = 40.640063
Lng2a = 22.944419

Location3a = "Skopje"
Lat3a = 41.997346
Lng3a = 21.427996

Location4a = "Leskovac"
Lat4a = 42.996812
Lng4a = 21.946463

Location5a = "Belgrade"
Lat5a = 44.786568
Lng5a = 20.448921

Location6a = "Budapest"
Lat6a = 47.497912
Lng6a = 19.040235

Location7a = "Bratislava"
Lat7a = 48.148598
Lng7a = 17.107748

Location8a = "Prague"
Lat8a = 50.075539
Lng8a = 14.437800

Location9a = "Dresden"
Lat9a = 51.050407
Lng9a = 13.737262

Location10a = "Berlin"
Lat10a = 52.520008
Lng10a = 13.404954



######## Wrapping data and display

myMap = folium.Map(location=[Lat1, Lng1], zoom_start=5)

#First route
folium.Marker([Lat1, Lng1], popup=f"{Location3}").add_to(myMap)
#folium.Marker([Lat2, Lng2], popup=f"{Location2}, {Kdnuggets}").add_to(myMap)
folium.Marker([Lat3, Lng3], popup=f"{Location3}").add_to(myMap)
folium.Marker([Lat4, Lng4], popup=f"{Location4}").add_to(myMap)
folium.Marker([Lat5, Lng5], popup=f"{Location5}").add_to(myMap)
folium.Marker([Lat6, Lng6], popup=f"{Location6}").add_to(myMap)
folium.Marker([Lat7, Lng7], popup=f"{Location7}").add_to(myMap)
folium.Marker([Lat8, Lng8], popup=f"{Location8}").add_to(myMap)
folium.Marker([Lat9, Lng9], popup=f"{Location9}").add_to(myMap)
folium.Marker([Lat10, Lng10], popup=f"{Location10}").add_to(myMap)
folium.Marker([Lat11, Lng11], popup=f"{Location11}").add_to(myMap)

# All locations into one variable
locations = [ [Lat3, Lng3], [Lat4, Lng4], [Lat5, Lng5], [Lat6, Lng6], [Lat7, Lng7], [Lat8, Lng8], [Lat9, Lng9], [Lat10, Lng10], [Lat11, Lng11], [Lat1, Lng1]]

# Red line
folium.PolyLine(locations=locations, color="red", weight=2.5, opacity=1).add_to(myMap)

#Displaied in map
HTML(myMap._repr_html_())



#Second route
folium.Marker([Lat1a, Lng1a], popup=f"{Location1a}").add_to(myMap)
folium.Marker([Lat2a, Lng2a], popup=f"{Location2a}").add_to(myMap)
folium.Marker([Lat3a, Lng3a], popup=f"{Location3a}").add_to(myMap)
folium.Marker([Lat4a, Lng4a], popup=f"{Location4a}").add_to(myMap)
folium.Marker([Lat5a, Lng5a], popup=f"{Location5a}").add_to(myMap)
folium.Marker([Lat6a, Lng6a], popup=f"{Location6a}").add_to(myMap)
folium.Marker([Lat7a, Lng7a], popup=f"{Location7a}").add_to(myMap)
folium.Marker([Lat8a, Lng8a], popup=f"{Location8a}").add_to(myMap)
folium.Marker([Lat9a, Lng9a], popup=f"{Location9a}").add_to(myMap)
folium.Marker([Lat10a, Lng10a], popup=f"{Location10a}").add_to(myMap)

locations2 = [[Lat1a, Lng1a], [Lat2a, Lng2a], [Lat3a, Lng3a], [Lat4a, Lng4a], [Lat5a, Lng5a], [Lat6a, Lng6a], [Lat7a, Lng7a], [Lat8a, Lng8a], [Lat9a, Lng9a], [Lat10a, Lng10a]]

# Blue line
folium.PolyLine(locations=locations2, color="blue", weight=2.5, opacity=1).add_to(myMap)

#Displaied in map
HTML(myMap._repr_html_())


# In[ ]:





# In[ ]:





# # NEW GOAL
# 
# -App provides current live location from the phone and then python is able to gelocalize  all users from here. 

# In[ ]:


g


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




