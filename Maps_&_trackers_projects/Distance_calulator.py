#!/usr/bin/env python
# coding: utf-8

# Input PC and City and shows it in map
# 
# 
# 

# In[1]:


print("\033[1;38;40mPlease, enter City Name\033[0m")
city = input()
print("\033[1;38;40mPlease, enter Postal Code name\033[0m")
postal_code = input()
from geopy.geocoders import Nominatim

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# specify the city and postal code
#city = "Berlin"
#postal_code = "10115"

# build the location string
location_str = f"{city}, {postal_code}"


# use geolocator to get the latitude and longitude of the location
location = geolocator.geocode(location_str)

# print the latitude and longitude
if location is not None:
    Lat = location.latitude
    Lng = location.longitude
    #location=city
    
    import folium
    from IPython.display import HTML
    myMap= folium.Map(location= [Lat, Lng], zoom_start=9)
    folium.Marker([Lat, Lng],popup=location).add_to((myMap))
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    HTML(myMap._repr_html_())
else:
    print("\033[1;41;41mLocation not found or not available. Attention: This map doesn't show the location\033[0m")

HTML(myMap._repr_html_())   


# In[ ]:





# In[ ]:


print("\033[1;30;40mLocation not found\033[0m")


# In[ ]:


print("\033[1;38;40mLocation not found\033[0m")


# In[ ]:


print("\033[1;41;41mLocation not found\033[0m")


# In[ ]:


print("\033[1;37;41mLocation not found\033[0m")


#  You give the City and POstal Code and you will receive a dataframe  and map with transport companies and recycling points. Telling you which are the closest ones to the customer

# In[ ]:


Company_A=0


# In[ ]:


postal_code


# In[ ]:


# Transport Companies
# use geolocator to get the latitude and longitude of the location

location_str_A='Hannover, 10115'
location_A = geolocator.geocode(location_str_A)

location_str_B='Frankfurt, 60306'
location_B = geolocator.geocode(location_str_B)

location_str_C='Hannover, 30159'
location_C = geolocator.geocode(location_str_C)

location_str_D='Munich, 80331'
location_D = geolocator.geocode(location_str_D)

# Adding to the map the headquarters
folium.Marker([Lat_A, Lng_A], popup=f"{Location_A}").add_to(myMap)
#Displaied in map
HTML(myMap._repr_html_())


# In[ ]:


location_D


# In[ ]:


Location_A="Hannover"
Lat_A=48.1371079
Lng_A=11.5753822


# In[ ]:





# In[ ]:





# In[ ]:





# # funciona pero con solo una ciudad

# In[2]:


# import the necessary libraries
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import folium
from IPython.display import HTML

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# prompt the user to enter a city and postal code
city = input("Please enter a city name: ")
postal_code = input("Please enter the postal code: ")

# build the location string for the user location
location_str = f"{city}, {postal_code}"

# use geolocator to get the latitude and longitude of the user location
location = geolocator.geocode(location_str)

# create the map centered on the user location
if location is not None:
    user_lat = location.latitude
    user_lng = location.longitude
    myMap = folium.Map(location=[user_lat, user_lng], zoom_start=9)
    # add a marker for the user location
    folium.Marker([user_lat, user_lng], 
                  popup=f"Your Location: {location}",
                  icon=folium.Icon(color='green')).add_to(myMap)
else:
    print("\033[1;41;41mLocation not found or not available. Attention: This map doesn't show the location\033[0m")
    myMap = folium.Map(location=[48.137154, 11.576124], zoom_start=9)  # fallback to Munich's coordinates

# build the location string for Munich
munich_str = "Munich, Germany"

# use geolocator to get the latitude and longitude of Munich
munich_location = geolocator.geocode(munich_str)
munich_lat = munich_location.latitude
munich_lng = munich_location.longitude

# add a marker for Munich
folium.Marker([munich_lat, munich_lng], popup="Munich").add_to(myMap)

# calculate the distance between the user location and Munich
if location is not None:
    distance_km = round(geodesic((user_lat, user_lng), (munich_lat, munich_lng)).km, 2)
    # add a line between the user location and Munich
    folium.PolyLine(locations=[(user_lat, user_lng), (munich_lat, munich_lng)], color='red').add_to(myMap)
    # display the distance on the map
    folium.Marker([(user_lat+munich_lat)/2, (user_lng+munich_lng)/2], 
                  popup=f"Distance to Munich: {distance_km} km",
                  icon=folium.Icon(color='purple')).add_to(myMap)

# display the map
HTML(myMap._repr_html_())


# In[ ]:





# --------------------------------------------------

# ------------------------------------

# In[3]:



################################################################# It works

# build the location string for Entsorge
munich_str = "Munich, Germany"
munich="munich"
Frankfurt_str="Frankfurt,Germany"
Frankfurt= "Frankfurt"
Hannover_str="Hannover,Germany"
Hannover="Hannover"
Bremen_str="Bremen,Germany"
Bremen="Bremen"
Hamburg_str="Hamburg,Germany"
Hamburg="Hamburg"

# use geolocator to get the latitude and longitude of Munich
munich_location = geolocator.geocode(munich_str)
munich_lat = munich_location.latitude
munich_lng = munich_location.longitude

Frankfurt_location = geolocator.geocode(Frankfurt_str)
Frankfurt_lat = Frankfurt_location.latitude
Frankfurt_lng = Frankfurt_location.longitude

Hannover_location = geolocator.geocode(Hannover_str)
Hannover_lat = Hannover_location.latitude
Hannover_lng = Hannover_location.longitude

Bremen_location = geolocator.geocode(Bremen_str)
Bremen_lat = Bremen_location.latitude
Bremen_lng = Bremen_location.longitude

Hamburg_location = geolocator.geocode(Hamburg_str)
Hamburg_lat = Hamburg_location.latitude
Hamburg_lng = Hamburg_location.longitude


# Creating map object
myMap = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

# Adding markers for cities
folium.Marker([munich_lat, munich_lng], popup=f"{munich}").add_to(myMap)
folium.Marker([Frankfurt_lat, Frankfurt_lng], popup=f"{Frankfurt}").add_to(myMap)
folium.Marker([Hannover_lat, Hannover_lng], popup=f"{Hannover}").add_to(myMap)
folium.Marker([Bremen_lat, Bremen_lng], popup=f"{Bremen}").add_to(myMap)
folium.Marker([Hamburg_lat, Hamburg_lng], popup=f"{Hamburg}").add_to(myMap)




# Displaying the map
HTML(myMap._repr_html_())


# ---------------------------------------

# In[ ]:





# In[ ]:





# In[4]:


# import the necessary libraries
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import folium
from IPython.display import HTML

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# prompt the user to enter a city and postal code
city = input("Please enter a city name: ")
postal_code = input("Please enter the postal code: ")

# build the location string for the user location
location_str = f"{city}, {postal_code}"

# use geolocator to get the latitude and longitude of the user location
location = geolocator.geocode(location_str)

# create the map centered on the user location
if location is not None:
    user_lat = location.latitude
    user_lng = location.longitude
    myMap = folium.Map(location=[user_lat, user_lng], zoom_start=9)
    # add a marker for the user location
    folium.Marker([user_lat, user_lng], 
                  popup=f"Your Location: {location}",
                  icon=folium.Icon(color='green')).add_to(myMap)
else:
    print("\033[1;41;41mLocation not found or not available. Attention: This map doesn't show the location\033[0m")
    myMap = folium.Map(location=[48.137154, 11.576124], zoom_start=9)  # fallback to Munich's coordinates

# build the location string for Entsorge
munich_str = "Munich, Germany"
munich="munich"
Frankfurt_str="Frankfurt,Germany"
Frankfurt= "Frankfurt"
Hannover_str="Hannover,Germany"
Hannover="Hannover"
Bremen_str="Bremen,Germany"
Bremen="Bremen"
Hamburg_str="Hamburg,Germany"
Hamburg="Hamburg"

# use geolocator to get the latitude and longitude of Munich
munich_location = geolocator.geocode(munich_str)
munich_lat = munich_location.latitude
munich_lng = munich_location.longitude

Frankfurt_location = geolocator.geocode(Frankfurt_str)
Frankfurt_lat = Frankfurt_location.latitude
Frankfurt_lng = Frankfurt_location.longitude

Hannover_location = geolocator.geocode(Hannover_str)
Hannover_lat = Hannover_location.latitude
Hannover_lng = Hannover_location.longitude

Bremen_location = geolocator.geocode(Bremen_str)
Bremen_lat = Bremen_location.latitude
Bremen_lng = Bremen_location.longitude

Hamburg_location = geolocator.geocode(Hamburg_str)
Hamburg_lat = Hamburg_location.latitude
Hamburg_lng = Hamburg_location.longitude


# Adding markers for cities
folium.Marker([munich_lat, munich_lng], popup=f"{munich}").add_to(myMap)
folium.Marker([Frankfurt_lat, Frankfurt_lng], popup=f"{Frankfurt}").add_to(myMap)
folium.Marker([Hannover_lat, Hannover_lng], popup=f"{Hannover}").add_to(myMap)
folium.Marker([Bremen_lat, Bremen_lng], popup=f"{Bremen}").add_to(myMap)
folium.Marker([Hamburg_lat, Hamburg_lng], popup=f"{Hamburg}").add_to(myMap)

# calculate the distance between the user location and Munich
if location is not None:
    distance_km = round(geodesic((user_lat, user_lng), (munich_lat, munich_lng)).km, 2)
    # add a line between the user location and Munich
    folium.PolyLine(locations=[(user_lat, user_lng), (munich_lat, munich_lng)], color='red').add_to(myMap)
    # display the distance on the map
    folium.Marker([(user_lat+munich_lat)/2, (user_lng+munich_lng)/2], 
                  popup=f"Distance to Munich: {distance_km} km",
                  icon=folium.Icon(color='purple')).add_to(myMap)

# display the map
HTML(myMap._repr_html_())


# In[ ]:





# In[ ]:





# ## User inputs vs distances with Entsorge

# In[5]:


# import the necessary libraries
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import folium
from IPython.display import HTML

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# prompt the user to enter a city and postal code
city = input("Please enter a city name: ")
postal_code = input("Please enter the postal code: ")

# build the location string for the user location
location_str = f"{city}, {postal_code}"

# use geolocator to get the latitude and longitude of the user location
location = geolocator.geocode(location_str)

# create the map centered on the user location
if location is not None:
    user_lat = location.latitude
    user_lng = location.longitude
    myMap = folium.Map(location=[user_lat, user_lng], zoom_start=9)
    # add a marker for the user location
    folium.Marker([user_lat, user_lng], 
                  popup=f"Your Location: {location}",
                  icon=folium.Icon(color='green')).add_to(myMap)
else:
    print("\033[1;41;41mLocation not found or not available. Attention: This map doesn't show the location\033[0m")
    myMap = folium.Map(location=[48.137154, 11.576124], zoom_start=9)  # fallback to Munich's coordinates

# build the location strings and geocode them for each city
cities = ["Munich, Germany", "Frankfurt, Germany", "Hannover, Germany", "Bremen, Germany", "Hamburg, Germany","Offenbach, Germany"]
city_lats = []
city_lngs = []
for city in cities:
    location = geolocator.geocode(city)
    if location is not None:
        city_lats.append(location.latitude)
        city_lngs.append(location.longitude)
        # add a marker for the city location
        folium.Marker([location.latitude, location.longitude], 
                      popup=f"{city}",
                      icon=folium.Icon(color='blue')).add_to(myMap)
    else:
        print(f"\033[1;41;41m{city} not found or not available.\033[0m")

# calculate the distance between the user location and each city
if location is not None:
    for i in range(len(cities)):
        distance_km = round(geodesic((user_lat, user_lng), (city_lats[i], city_lngs[i])).km, 2)
        # add a line between the user location and the city
        folium.PolyLine(locations=[(user_lat, user_lng), (city_lats[i], city_lngs[i])], color='red').add_to(myMap)
        # display the distance on the map
        folium.Marker([(user_lat+city_lats[i])/2, (user_lng+city_lngs[i])/2], 
                      popup=f"Distance to {cities[i]}: {distance_km} km",
                      icon=folium.Icon(color='purple')).add_to(myMap)

# display the map
HTML(myMap._repr_html_())


# In[ ]:





# In[ ]:





# ## Creation of DF

# In[6]:


# create an empty dataframe
import pandas as pd
df = pd.DataFrame()

# create a dataframe with data
for i in range(len(city_lats)):
    # create a new column with the name of the city
    city_name = cities[i]
    df[city_name] = [city_lats[i], city_lngs[i]]
    
# set the city names as the index
df.index = ['Latitude', 'Longitude']

# move the head of df to index
df = df.T.set_index(df.columns)

# rename columns with Lat and Lng values
df = df.rename(columns={'Latitude': 'Latitude', 'Longitude': 'Longitude'})

df


# In[ ]:





# In[126]:


df


# # FINAL - It works, map and DF with ctites sorted by distance towards the users city input

# In[7]:


# import the necessary libraries
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import folium
from IPython.display import HTML
import pandas as pd

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# prompt the user to enter a city and postal code
city = input("Please enter a city name: ")
users_city_input = city
postal_code = input("Please enter the postal code: ")

# build the location string for the user location
location_str = f"{city}, {postal_code}"

# use geolocator to get the latitude and longitude of the user location
location = geolocator.geocode(location_str)

# create the map centered on the user location
if location is not None:
    user_lat = location.latitude
    user_lng = location.longitude
    myMap = folium.Map(location=[user_lat, user_lng], zoom_start=9)
    # add a marker for the user location
    folium.Marker([user_lat, user_lng], 
                  popup=f"Your Location: {location}",
                  icon=folium.Icon(color='green')).add_to(myMap)
else:
    print("\033[1;41;41mLocation not found or not available. Attention: This map doesn't show the location\033[0m")
    myMap = folium.Map(location=[48.137154, 11.576124], zoom_start=9)  # fallback to Munich's coordinates

# build the location strings and geocode them for each city
cities = ["Munich, Germany", "Frankfurt, Germany", "Hannover, Germany", "Bremen, Germany", "Hamburg, Germany","Offenbach, Germany"]
city_lats = []
city_lngs = []
for city in cities:
    location = geolocator.geocode(city)
    if location is not None:
        city_lats.append(location.latitude)
        city_lngs.append(location.longitude)
        # add a marker for the city location
        folium.Marker([location.latitude, location.longitude], 
                      popup=f"{city}",
                      icon=folium.Icon(color='blue')).add_to(myMap)
    else:
        print(f"\033[1;41;41m{city} not found or not available.\033[0m")

# calculate the distance between the user location and each city
if location is not None:
    for i in range(len(cities)):
        distance_km = round(geodesic((user_lat, user_lng), (city_lats[i], city_lngs[i])).km, 2)
        # add a line between the user location and the city
        folium.PolyLine(locations=[(user_lat, user_lng), (city_lats[i], city_lngs[i])], color='red').add_to(myMap)
        # display the distance on the map
        folium.Marker([(user_lat+city_lats[i])/2, (user_lng+city_lngs[i])/2], 
                      popup=f"Distance to {cities[i]}: {distance_km} km",
                      icon=folium.Icon(color='purple')).add_to(myMap)
        
        
        
        
        
######## Creating datframe          
        
# create an empty dataframe
df = pd.DataFrame()

# create a dataframe with data
for i in range(len(city_lats)):
    # create a new column with the name of the city
    city_name = cities[i]
    df[city_name] = [city_lats[i], city_lngs[i]]
    
    
# set the city names as the index
df.index = ['Latitude', 'Longitude']

# move the head of df to index
df = df.T.set_index(df.columns)

# rename columns with Lat and Lng values
df = df.rename(columns={'Latitude': 'Latitude', 'Longitude': 'Longitude'})


# calculate the distance between the user location and each city and store in a list
distance_km = []
if location is not None:
    for i in range(len(cities)):
        dist = round(geodesic((user_lat, user_lng), (city_lats[i], city_lngs[i])).km, 2)
        distance_km.append(dist)

        
        
df = df.assign(Distance_km=distance_km) 


# sort the DataFrame by shortest distance
df = df.sort_values(by=['Distance_km'])

print("Table with distances to " +" " + users_city_input)
### Map and Df can be only together posted if DF is in print mode
print(df)

# display the map
HTML(myMap._repr_html_())


# In[ ]:





# # next steps:
# 
# Create a website where I introduce the city name and I get the distance.
# 
# Same concept as the code abovebut in a website.
# 

# ## - Other taks: Ploting driver routes

# https://towardsdatascience.com/visualization-in-python-finding-routes-between-points-2d97d4881996

# In[8]:


import networkx as nx
import osmnx
import networkx


# In[ ]:


52.526452959064315, 13.419494432032993


# In[1]:


import osmnx as ox
import networkx as nx
ox.settings.log_console=True
ox.settings.use_cache=True
# define the start and end locations in latlng
start_latlng = (52.543078901085025,13.421612628441949)
end_latlng = (52.526452959064315,13.419494432032993)
# location where you want to find your route
place     = 'Berlin, Germany'
# find shortest route based on the mode of travel
mode      = 'drive'        # 'drive', 'bike', 'walk'
# find shortest path based on distance or time
optimizer = 'time'        # 'length','time'
# create graph from OSM within the boundaries of some 
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)
# find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1],
                                      start_latlng[0])
# find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1],
                                      end_latlng[0])
#  find the shortest path
shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)


# In[2]:


shortest_route_map = ox.plot_route_folium(graph, shortest_route)
shortest_route_map


# In[14]:


shortest_route_map = ox.plot_route_folium(graph, shortest_route, 
                                          tiles='openstreetmap')
shortest_route_map


# ----------------------------------------------------------------------------------------

# In[ ]:





# In[3]:


import osmnx as ox
import networkx as nx

ox.settings.log_console = True
ox.settings.use_cache = True

# define the start and end locations in latlng
start_latlng = (52.526452959064315,13.419494432032993)
end_latlng = (52.543078901085025,13.421612628441949)

# location where you want to find your route
place = 'Potsdam, Germany'

# find shortest route based on the mode of travel
mode = 'drive'  # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'time'  # 'length','time'

# create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)

# find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)


# In[9]:


import osmnx as ox
import networkx as nx
import folium

ox.config(log_console=True, use_cache=True)

# define the start and end locations in latlng
start_latlng = (52.543078901085025,13.421612628441949)
end_latlng = (52.526452959064315,13.419494432032993)

# location where you want to find your route
place = 'Berlin, Germany'

# find shortest route based on the mode of travel
mode = 'drive' # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'time' # 'length','time'

# create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)

# add speed and travel time attributes to the edges of the graph
graph = ox.add_edge_speeds(graph)
graph = ox.add_edge_travel_times(graph)

# find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

# plot the route on a map
route_map = ox.plot_route_folium(graph, shortest_route)

# add start and end markers to the map
start_marker = folium.Marker(location=start_latlng)
start_marker.add_to(route_map)
end_marker = folium.Marker(location=end_latlng)
end_marker.add_to(route_map)

# display the map
route_map


# # It works - Berlin -Postdam

# In[10]:


import osmnx as ox
import networkx as nx
ox.config(log_console=True, use_cache=True)

# Define the start and end locations in latlng
start_latlng = (52.520008, 13.404954)  # Berlin
end_latlng = (52.396577, 13.061915)  # Potsdam city center

# Location where you want to find your route
place = ["Berlin, Germany", "Potsdam, Germany"]


# Find shortest route based on the mode of travel
mode = 'drive'  # 'drive', 'bike', 'walk'

# Find shortest path based on distance or time
optimizer = 'time'  # 'length','time'

# Create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)

# Find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# Find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# Find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

# Plot the route on a map
route_map = ox.plot_route_folium(graph, shortest_route)

# Add start and end markers to the map
start_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])
end_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])
start_point = (start_latlng[0], start_latlng[1])
end_point = (end_latlng[0], end_latlng[1])
route_map = ox.plot_route_folium(graph, shortest_route, route_map=route_map, start=start_node, end=end_node, popup_attribute='name')

# Add markers for start and end points
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(route_map)

# Show the map
route_map


# In[ ]:





# In[ ]:





# In[ ]:


52.40816786138833, 12.536663690133658


# In[17]:


import osmnx as ox
import networkx as nx
ox.config(log_console=True, use_cache=True)

# Define the start and end locations in latlng
start_latlng = (52.520008, 13.404954)  # Berlin
end_latlng = (52.40816786138833, 12.536663690133658)  # Potsdam city center

# Location where you want to find your route
place = ["Berlin, Germany", "Potsdam, Germany"]


# Find shortest route based on the mode of travel
mode = 'drive'  # 'drive', 'bike', 'walk'

# Find shortest path based on distance or time
optimizer = 'time'  # 'length','time'

# Create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)

# Find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# Find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# Find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

# Plot the route on a map
route_map = ox.plot_route_folium(graph, shortest_route)

# Add start and end markers to the map
start_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])
end_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])
start_point = (start_latlng[0], start_latlng[1])
end_point = (end_latlng[0], end_latlng[1])
route_map = ox.plot_route_folium(graph, shortest_route, route_map=route_map, start=start_node, end=end_node, popup_attribute='name')

# Add markers for start and end points
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(route_map)

# Show the map
route_map


# In[ ]:





# # It works Colored map with marks

# In[3]:


import osmnx as ox
import networkx as nx
import folium

ox.config(log_console=True, use_cache=True)

# Define the start and end locations in latlng
start_latlng = (52.520008, 13.404954)  # Berlin
end_latlng = (52.45, 13.5)  # Potsdam city center

# Location where you want to find your route
place = ["Berlin, Germany", "Potsdam, Germany"]


# Find shortest route based on the mode of travel
mode = 'drive'  # 'drive', 'bike', 'walk'

# Find shortest path based on distance or time
optimizer = 'time'  # 'length','time'

# Create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)

# Find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# Find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# Find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

# Plot the route on a map
route_map = ox.plot_route_folium(graph, shortest_route)

# Add start and end markers to the map
start_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])
end_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])
start_point = (start_latlng[0], start_latlng[1])
end_point = (end_latlng[0], end_latlng[1])
route_map = ox.plot_route_folium(graph, shortest_route, route_map=route_map, start=start_node, end=end_node, popup_attribute='name')

# Add markers for start and end points
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(route_map)

# Traza la ruta en un mapa de OpenStreetMap
shortest_route_map = ox.plot_route_folium(graph, shortest_route, 
                                          tiles='openstreetmap', 
                                          route_color='#FF4136',
                                          start=start_latlng,
                                          end=end_latlng )


# Agrega las marcas de inicio y fin
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(shortest_route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(shortest_route_map)

# Muestra el mapa
shortest_route_map


# In[ ]:





# ------------

# # It works Colored map with marks - Berlin -Brandenburg

# ## Notes: The provided route is different and it seems longer that the one showed by google maps

# In[8]:


from PIL import Image
from IPython.display import display

# Open image using Image module
img = Image.open("Route_test.PNG")

# Show image using display function
display(img)


# In[ ]:





# In[4]:


import osmnx as ox
import networkx as nx

ox.config(log_console=True, use_cache=True)

# Define the start and end locations in latlng
start_latlng = (52.520008, 13.404954)  # Berlin
end_latlng = (52.346152628888895, 14.538561690865155)  # Potsdam city center

# Location where you want to find your route
place = ["Berlin, Germany", "Brandenburg, Germany"]


# Find shortest route based on the mode of travel
mode = 'drive'  # 'drive', 'bike', 'walk'

# Find shortest path based on distance or time
optimizer = 'time'  # 'length','time'

# Create graph from OSM within the boundaries of some geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)

# Find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])

# Find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])

# Find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

# Plot the route on a map
route_map = ox.plot_route_folium(graph, shortest_route)

# Add start and end markers to the map
start_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])
end_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])
start_point = (start_latlng[0], start_latlng[1])
end_point = (end_latlng[0], end_latlng[1])
route_map = ox.plot_route_folium(graph, shortest_route, route_map=route_map, start=start_node, end=end_node, popup_attribute='name')

# Add markers for start and end points
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(route_map)

# Traza la ruta en un mapa de OpenStreetMap
shortest_route_map = ox.plot_route_folium(graph, shortest_route, 
                                          tiles='openstreetmap', 
                                          route_color='#FF4136',
                                          start=start_latlng,
                                          end=end_latlng )


# Agrega las marcas de inicio y fin
folium.Marker(location=start_point, icon=folium.Icon(color='green')).add_to(shortest_route_map)
folium.Marker(location=end_point, icon=folium.Icon(color='red')).add_to(shortest_route_map)

# Muestra el mapa
shortest_route_map


# In[ ]:





# ---------------------------------------

# In[ ]:


51.341980591084464, 12.376849847244774


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




