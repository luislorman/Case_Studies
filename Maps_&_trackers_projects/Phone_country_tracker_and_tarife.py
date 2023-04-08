#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phonenumbers


# In[2]:


# notebook files are not pure py but ipynb, they need a different library
https://stackoverflow.com/questions/20186344/importing-an-ipynb-file-from-another-ipynb-file


# In[3]:


import import_ipynb


# In[4]:


from  myphone import number # I import the variable from the other file called myphone - it must be within the same folder


# In[5]:


from phonenumbers import geocoder # to extract the country name


# In[6]:


parsed_number = phonenumbers.parse(number)  # CODE A - SAME AS B
location = geocoder.description_for_number(parsed_number, "en")
print(location) #GET COUNTRY


# In[7]:


parsed_number


# In[8]:


# IMPORTANT NOTE - If the code from In[32] doesnt show the number you want, run the code below, to assign the number to the variable


# In[1]:


import phonenumbers  #CODE B - SAME AS A 

number = "+341111111" #all together
parsed_number = phonenumbers.parse(number)
print("Country Code:", parsed_number.country_code)
print("National Number:", parsed_number.national_number)


# In[51]:


# Get service provider


# In[52]:


from phonenumbers import carrier


# In[53]:


number="+34111111"


# In[54]:


service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


# In[55]:


# get map location 


# In[56]:


# ATTENTION - This location code only provides a location in the centre of the phone’s country, not the current live location


# In[57]:


key= "--------" # got the key from web OpenCage,  they sent me an email with the API Key


# In[58]:


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query=str(location)
results = geocoder.geocode(query)
print(results) # we want the part of the first line lng and the numbers


# In[59]:


import folium


# In[60]:


lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print(lat,lng)


# In[61]:


myMap= folium.Map(location= [lat, lng], zoom_start=9)
folium.Marker([lat, lng],popup=location).add_to((myMap))


# In[ ]:


# save map in html file


# In[ ]:


myMap.save ("TheLocation.html") # it show a location in the centre of the country for each national code. bu tnot the phone location


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# >Code to check if Geocoder is able to geolocate the phone live location


# In[1]:


import phonenumbers
from geopy.geocoders import Nominatim

number = "+34111111111"
parsed_number = phonenumbers.parse(number)

if phonenumbers.is_valid_number(parsed_number):
    country_code = parsed_number.country_code
    national_number = parsed_number.national_number
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(f"+{country_code}{national_number}", exactly_one=True)
    if location:
        print(location.address)
        print(location.latitude, location.longitude)
    else:
        print("Location not found.")
else:
    print("Invalid phone number.")


# In[ ]:




