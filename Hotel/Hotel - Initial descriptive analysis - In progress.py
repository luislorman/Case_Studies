#!/usr/bin/env python
# coding: utf-8

# # Introduction 
# ## This is an initial descriptive analysis before the Forecast, in order to know in detail the type of data that will be worked on.
# ## Notes: Some rows contain the word 'Tableau' that is a personal note, which means  I have worked the date in that tool as well. 

# ------------------------------------------------------

# In[ ]:


import pandas as pd
df = pd.read_csv('Hotel Reservations.csv')


# In[417]:


ID_df = pd.read_csv('ID_category_price.csv')


# In[418]:


type_df = pd.read_csv('type_category_price.csv')


# In[419]:


ID_df.to_excel('ID_df.xlsx', sheet_name='Sheet1', index=False)
type_df.to_excel('type_df.xlsx', sheet_name='Sheet1', index=False)


# In[420]:


hotel = df
hotel


# In[9]:


hotel.to_excel('hotel.xlsx', sheet_name='Sheet1', index=False)


# In[11]:


hotel.info()


# In[78]:


hotel[["room_type_reserved","avg_price_per_room"]]


# In[79]:


import pandas as pd


# Group the data by room_type_reserved and calculate the mean of avg_price_per_room
grouped_data = hotel.groupby('room_type_reserved')['avg_price_per_room'].mean()

# Print the result
print(grouped_data)


# # Check price total nights* average price and seeing what segments provides more revenue (corporate, oline,etc)
# 

# In[ ]:


no_of_weekend_nights
no_of_week_nights
avg_price_per_room 


# In[ ]:


# group_by sum of avgr_price ////// REMINDER - withihn the same room type, there are different prices, this is a avgr sum


# In[124]:


# price within room type
unique_prices = hotel[['room_type_reserved', 'avg_price_per_room']].drop_duplicates().reset_index(drop=True)
unique_prices # there are different avg_price within the same room type


# In[128]:


# AVRG PRICE WITHIN ROOM TYPE - I WILL USE THIS ONE
# Group the data by room_type_reserved and calculate the mean of avg_price_per_room
room_MEAN_price = hotel.groupby('room_type_reserved')[["room_type_reserved","avg_price_per_room"]].mean()
#room_total_price = room_total_price.sort_values(by='avg_price_per_room', ascending=False)
room_MEAN_price


# In[129]:



# Group the data by room_type_reserved and calculate the mean of avg_price_per_room
room_nights = hotel.groupby('room_type_reserved')[["no_of_weekend_nights","no_of_week_nights"]].sum()
#room_total_price = room_total_price.sort_values(by='avg_price_per_room', ascending=False)
room_nights 


# In[134]:


# GLOBAL - merge without unique prices within room
merged_group_df = pd.merge(room_nights, room_MEAN_price, left_index=True, right_index=True)
merged_group_df


# In[193]:


merge_room_price = pd.read_csv('merge_room_price.csv')
merge_room_price


# In[194]:


merge_room_price= merge_room_price.drop('room_type_reserved.1', axis=1)
merge_room_price


# #  TODO - % money from only adults or adults with kids - is a family hotel?

# In[ ]:





# # in order to see where there is more money and compare it between dates, it is necessary to create a new file with IB and dates.

# In[162]:


test_df = merge_room_price.groupby('room_type_reserved')[["room_type_reserved","total_price"]].sum()
test_df = test_df.sort_values(by='total_price', ascending=False)
test_df


# # done=  most profitble rooms 

# In[163]:


import matplotlib.pyplot as plt

test_df.plot(kind='bar', y='total_price', legend=False)
plt.title('Total Price by Room Type Reserved')
plt.xlabel('Room Type Reserved')
plt.ylabel('Total Price')
plt.show()


# ## Tableau =  corporate = less guests than online, but they are the ones who more repeat. 
# 

# In[231]:


hotel.info()


# In[ ]:





# In[253]:


hotel["repeated_guest"].unique()


# In[254]:


hotel["repeated_guest"].value_counts()


# In[256]:


repeated_guest_count = hotel.groupby('market_segment_type')['repeated_guest'].count()
repeated_guest_count


# In[258]:


repeated_guest_value_counts = hotel.groupby('market_segment_type')['repeated_guest'].value_counts()
repeated_guest_value_counts


# In[248]:


sorted_guests = hotel.groupby('market_segment_type')['repeated_guest'].count().sort_values(ascending=True)
sorted_guests #total repated and not


# ### number of guest by segment

# In[259]:


import matplotlib.pyplot as plt

# group the data by market segment type and count the number of repeated guests
repeated_guest = hotel.groupby('market_segment_type')['repeated_guest'].count()

# create a bar chart of the data
plt.bar(repeated_guest.index, repeated_guest.values)

# add labels to the chart
plt.xlabel('Market Segment Type')
plt.ylabel('Number of Repeated Guests')
plt.title('Number of Repeated Guests by Market Segment Type')

# display the chart
plt.show()


# ### number of repeated guest by segment

# In[9]:


repeated_guest_value_counts = hotel.groupby('market_segment_type')['repeated_guest'].value_counts()
repeated_guest_value_counts


# In[14]:


import matplotlib.pyplot as plt

# Create a stacked bar chart from the repeated_guest_value_counts DataFrame
repeated_guest_value_counts.unstack().plot(kind='bar', stacked=True)

# Add labels and title
plt.xlabel('Market Segment Type')
plt.ylabel('Count')
plt.title('Market Segment Type vs Repeated Guest')

# Add legend with custom labels
plt.legend(title='Repeated Guest', labels=['No Repeated (0)', 'Repeated (1)'])

# Show the plot
plt.show()


# ### very low number of  repeats
# 

# its the low number linked ot the high increase of new customers?

# In[ ]:





# 

# ## (solved,below) check if there is a conexion betewing the online people (business segment) who request parking and chances of reapeating 

# In[179]:


hotel[["market_segment_type","room_type_reserved","booking_status"]]


# In[192]:


hotel[["market_segment_type","room_type_reserved","booking_status","repeated_guest","required_car_parking_space"]]


# In[199]:


import pandas as pd

# create a new dataframe with one-hot encoding of the categorical variables
hotel_encoded = pd.get_dummies(hotel[["market_segment_type"]])

# add the numerical variables to the encoded dataframe
hotel_encoded["repeated_guest"] = hotel["repeated_guest"]
hotel_encoded["required_car_parking_space"] = hotel["required_car_parking_space"]

# calculate the correlation matrix
corr_matrix = hotel_encoded.corr()

# display the correlation matrix
corr_matrix


# In[200]:


import seaborn as sns

# create a heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")

# display the plot
plt.title("Correlation Matrix")
plt.show()


# # conlusion 0.42 corporate and repeated guesst, parking slot and buisness segemtn not linked

# ### notes BOOKINGS_N: online 25k bookings, offline 10.528 bookings (what kind o customer profile, they dont have kids, car?), corporate 2k 
# ### notes Repeated guest: total reapetes guests= 930 //// corporate 602 
# ### notes parking segment: online 869, corporative 184, others basically extremly low

# In[ ]:





# ## solved, below -  profile offline registrations
# 

# In[219]:


hotel


# In[225]:


# create a boolean mask indicating which rows contain the value "Offline" in the "market_segment_type" column
mask = hotel["market_segment_type"] == "Offline"

# apply the mask to filter the dataframe and sort the result based on the "market_segment_type" column
hotel_sorted = hotel.loc[mask].sort_values(by="market_segment_type", ascending=True)

# display the sorted dataframe
hotel_sorted


# ### ofline second highst customer type and reasonable number of kids, no particular profile - tableau

# ## popular rooms by segment
# 

# In[16]:


hotel[["room_type_reserved","market_segment_type"]]


# In[38]:


grouped_data_A = hotel.groupby('room_type_reserved')["market_segment_type"].value_counts()

grouped_data_A 


# In[39]:


# pasar a dataframe

grouped_data_A  = pd.DataFrame(grouped_data_A )
grouped_data_A 


# In[35]:


import matplotlib.pyplot as plt

# group the data by market segment type and count the number of repeated guests
a = hotel.groupby('room_type_reserved')["Booking_ID"].count()

# create a bar chart of the data
plt.bar(a.index, a.values)

# adjust the spacing between the x-axis labels
plt.xticks(rotation=45, ha='right', fontsize=12)

# add labels to the chart
plt.xlabel('Market Segment Type')
plt.ylabel('Number of booked Rooms')
plt.title('Number of Rooms booked by type')



# display the chart
plt.show()


# In[41]:


import matplotlib.pyplot as plt
import pandas as pd

# create the dataframe
data = {'Room Type': ['Room_Type 1', 'Room_Type 1', 'Room_Type 1', 'Room_Type 1', 'Room_Type 1',
                      'Room_Type 2', 'Room_Type 2', 'Room_Type 2', 'Room_Type 2',
                      'Room_Type 3', 'Room_Type 3', 'Room_Type 3', 'Room_Type 3',
                      'Room_Type 4', 'Room_Type 4', 'Room_Type 4', 'Room_Type 4', 'Room_Type 4',
                      'Room_Type 5', 'Room_Type 5', 'Room_Type 5', 'Room_Type 5',
                      'Room_Type 6', 'Room_Type 6', 'Room_Type 6', 'Room_Type 6',
                      'Room_Type 7', 'Room_Type 7', 'Room_Type 7', 'Room_Type 7'],
        'Market Segment Type': ['Online', 'Offline', 'Corporate', 'Complementary', 'Aviation',
                                'Online', 'Offline', 'Complementary', 'Corporate',
                                'Complementary', 'Offline', 'Online', 'Corporate',
                                'Online', 'Offline', 'Corporate', 'Aviation', 'Complementary',
                                'Online', 'Offline', 'Corporate', 'Complementary',
                                'Online', 'Offline', 'Complementary', 'Corporate',
                                'Online', 'Complementary', 'Corporate', 'Offline'],
        'Count': [16243, 9747, 1833, 247, 60,
                  613, 57, 20, 2,
                  2, 2, 1, 1,
                  5228, 613, 99, 65, 52,
                  93, 81, 74, 17,
                  926, 23, 14, 3,
                  109, 39, 5, 5]}

df = pd.DataFrame(data)

# create a pivot table to group by room type and market segment type
pivot_table = pd.pivot_table(df, index=['Room Type'], columns=['Market Segment Type'], values='Count')

# create a bar chart of the data
pivot_table.plot(kind='bar', stacked=True)

# add labels to the chart
plt.xlabel('Room Type')
plt.ylabel('Number of Booked Rooms')
plt.title('Number of Room Type by Market Segment Type')

# display the chart
plt.show()


# ### popular rooms by segemt : type 1, 4 and 6 - tableau

# In[ ]:





# In[177]:


hotel.info()


# # most profitable room and business segment + date or key dates
# # repeated guests

# In[118]:


room_status = hotel[["market_segment_type","room_type_reserved","booking_status"]]
room_status


# In[ ]:





# In[119]:


#room_status = room_status.groupby('market_segment_type')[['room_type_reserved',"booking_status"]].count()
import pandas as pd
import matplotlib.cm as cm

# create a pivot table with the counts
table = pd.pivot_table(room_status, index=["room_type_reserved"], columns=["booking_status", "market_segment_type"], aggfunc=len, fill_value=0)



# create a colormap with the same blue tone as Tableau
#tableau_blue = cm.get_cmap('Blues')

# color the cells based on their values using the tableau_blue colormap
#colored_table = table.style.background_gradient(cmap=tableau_blue)

# display the colored table
#colored_table
table


# ## % cancelled by segment

# In[75]:


room_status = hotel[["market_segment_type","booking_status"]]
room_status


# In[77]:


# create a boolean mask indicating which rows contain the value "Offline" in the "market_segment_type" column
mask_B = hotel["booking_status"] == "Canceled"

# apply the mask to filter the dataframe and sort the result based on the "market_segment_type" column
room_canceled= hotel.loc[mask_B].sort_values(by="booking_status", ascending=True)

#######
# create a boolean mask indicating which rows contain the value "Offline" in the "market_segment_type" column
mask_C = hotel["booking_status"] == "Not_Canceled"

# apply the mask to filter the dataframe and sort the result based on the "market_segment_type" column
room_open = hotel.loc[mask_C].sort_values(by="booking_status", ascending=True)


# In[89]:


room_open["market_segment_type"].value_counts


# In[90]:


room_canceled["market_segment_type"].value_counts()


# In[91]:


hotel["market_segment_type"].value_counts()


# In[93]:


room_open["market_segment_type"].value_counts()/hotel["market_segment_type"].value_counts()


# In[94]:


room_canceled["market_segment_type"].value_counts()/hotel["market_segment_type"].value_counts()
# nan because of 0 cancelations


# ## Done, anwers
# ### 36% cancellations in online 
# ### almost 30% of cancellations in aviation
# ### complementary doesn't have cancellations
# 
# ## Following questions:
# ### why cancellation? 
# ### next question: how much money did it 'cost'?
# ### how did it take to book it again?

# ## 34% rooms type 4 cancelled - Explained: all segment has a high ratio of cancellations,  sometimes hitting above 30%, except Complementary segment with 0% and Offline with 0,06% - regarding room type 4 -

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# From month 7 grow, reaching top on 10 and falling on 11 to take back on 12
# 
# Huge increase in year 2018

# In[124]:


first_month_year = hotel[["arrival_month","arrival_year"]]
first_month_year


# In[ ]:


hotel[["Booking_ID","arrival_month","arrival_year"]]


# In[116]:


zimmer = hotel.groupby('arrival_year')[['arrival_month',"Booking_ID"]].count()
zimmer


# In[125]:


# create a pivot table with the counts
zimmer = pd.pivot_table(first_month_year, index=["arrival_month"], columns=["arrival_year"], aggfunc=len, fill_value=0)

zimmer


# In[134]:


hotel["arrival_year"].value_counts()


# In[155]:


x = (6514/29761)*100
y = 100 - x
print("% increase from 2017 to 2018 {:.2f}%".format(y))


# ## done -
# ### One  Top in 6, falls in 7 and then  grow, reaching top on 10 and falling after 11 - 2018
# ### From month 7 grow, reaching top on 10 and then falling on 11 to take back on 12 in 2017 
# 
# ### Huge increase in year 2018

# In[ ]:





# ## more ancelations in particular months?

# In[163]:


status_month = hotel[["arrival_month","booking_status"]]
status_month


# In[ ]:





# In[162]:


status_month = status_month.set_index('arrival_month')
status_month


# In[164]:



# Group the data by room_type_reserved and calculate the mean of avg_price_per_room
grouped_data_Z = hotel.groupby('arrival_month')['booking_status'].value_counts()


# In[165]:


grouped_data_Z  = pd.DataFrame(grouped_data_Z)
grouped_data_Z


# In[169]:


import matplotlib.pyplot as plt

grouped_data_Z = hotel.groupby('arrival_month')['booking_status'].value_counts()

# Convert the second level of the index into separate columns
grouped_data_Z = grouped_data_Z.unstack()

# Create a bar chart
grouped_data_Z.plot(kind='bar', stacked=True)

# Set the chart title and axis labels
plt.title('Bookings by Arrival Month and Status')
plt.xlabel('Arrival Month')
plt.ylabel('Count of Bookings')

# Show the chart
plt.show()


# In[168]:


import matplotlib.pyplot as plt

# Group the data and compute the percentages as before
grouped_data_Z = hotel.groupby('arrival_month')['booking_status'].value_counts().unstack()
grouped_data_Z = grouped_data_Z.apply(lambda x: 100 * x / float(x.sum()), axis=1)

# Create a bar chart
ax = grouped_data_Z.plot(kind='bar', stacked=True)

# Set the chart title and axis labels
plt.title('Bookings by Arrival Month and Status')
plt.xlabel('Arrival Month')
plt.ylabel('% of Bookings')

# Add the percentage values to each bar
for p in ax.patches:
    height = p.get_height()
    width = p.get_width()
    x, y = p.get_xy()
    ax.text(x+width/2, y+height/2, f'{height:.1f}%', ha='center', va='center')

# Show the chart
plt.show()


# # DONE- Answers
# ## there is some tendency between n° of bookings and % of cancellations - around 30%
# ## comparing the graph of booking n° and the graph of %, pointing out the relevanta number of cancellations in month 6 & 7.
# ## Month 12 outperforming, high level of bookings and only 13% cancelled, first month the best but not relevant mention due to the low n° of bookings

# # questions - what kind o profile has the customers from month 1 
# ## answer: no relevant data, comparation ratio n° bookings and profile, doesnt show anything relevant

# In[ ]:





# In[176]:


hotel[["booking_status","market_segment_type","arrival_month"]]


# In[186]:


# create a boolean mask indicating which rows contain the value "Offline" in the "market_segment_type" column
mask_E = hotel["booking_status"] == "Canceled"

# apply the mask to filter the dataframe and sort the result based on the "market_segment_type" column
segment_month_1 = hotel.loc[mask_E].sort_values(by="booking_status", ascending=True)

# create a boolean mask indicating which rows contain the value "Offline" in the "market_segment_type" column
mask_F = hotel["arrival_month"] == 1

# display the sorted dataframe
segment_month_1 = segment_month_1.loc[mask_F].sort_values(by="arrival_month", ascending=True)
segment_month_1["market_segment_type"].value_counts()


# In[185]:


hotel[""]


# In[ ]:





# # room and kids - tableau
# ## there is a profile by type of meal
# ## adults type 4 and kids type 7
# 

# In[432]:


room_customer_df = hotel[["room_type_reserved","no_of_adults","no_of_children"]]
room_customer_df


# In[433]:


room_customer_df = hotel.groupby('room_type_reserved')[['no_of_adults',"no_of_children"]].sum()
room_customer_df


# In[434]:


my_dict = room_customer_df.to_dict() # i move this to Dictionary format and then I plot a bar chart
my_dict


# In[435]:


import matplotlib.pyplot as plt
import pandas as pd

data = {'no_of_adults': {'Room_Type 1': 49799, 'Room_Type 2': 1093, 'Room_Type 3': 11, 'Room_Type 4': 13280, 'Room_Type 5': 461, 'Room_Type 6': 1927, 'Room_Type 7': 355},
        'no_of_children': {'Room_Type 1': 1389, 'Room_Type 2': 407, 'Room_Type 3': 0, 'Room_Type 4': 231, 'Room_Type 5': 35, 'Room_Type 6': 1631, 'Room_Type 7': 126}}

df = pd.DataFrame(data)

ax = df.plot(kind='bar')
ax.set_xlabel('Room Type')
ax.set_ylabel('Number of People')
ax.set_title('Number of Adults and Children by Room Type')
plt.xticks(rotation=55)

plt.show()


# In[436]:


import matplotlib.pyplot as plt
import pandas as pd



ax = room_customer_df.plot(kind='bar')
ax.set_xlabel('Room Type')
ax.set_ylabel('Number of People')
ax.set_title('Number of Adults and Children by Room Type')


#label on the bar
for p in ax.patches: 
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), rotation=50)



plt.xticks(rotation=55)


plt.show()


# # Answer: Room 1 most successfully, extremly popular among adults and second most booked by 'kids'
# ## Room Type 4, second most requested by adults.
# ## Room 6 highly popluar among 'kids', almost reaching number of adult, which is their third most popular room type.
# ## Room Type 2, is the third type of room most popular among adults, and kids
# ## Rest of rooms dont have relevant numbers.

# ---------------------------

# # meals - tableau - answer below
# 

# In[437]:


hotel.info()


# In[438]:


hotel[["type_of_meal_plan","no_of_adults","no_of_children"]]


# In[439]:


customer_meal = hotel.groupby('type_of_meal_plan')[['no_of_adults',"no_of_children"]].sum()
customer_meal


# In[440]:


import matplotlib.pyplot as plt
import pandas as pd



ax = customer_meal.plot(kind='bar')
ax.set_xlabel('Room Type')
ax.set_ylabel('Number of People')
ax.set_title('Number of Adults and Children by Room Type')


#label on the bar
for p in ax.patches: 
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), rotation=50)



plt.xticks(rotation=55)


plt.show()


# In[446]:


segment_meal = hotel.groupby('type_of_meal_plan')["market_segment_type"].value_counts()
segment_meal


# In[447]:


my_dict_meal = segment_meal.to_dict() # i move this to Dictionary format and then I plot a bar chart
my_dict_meal


# In[477]:


import matplotlib.pyplot as plt

# define the data
data = {('Meal Plan 1', 'Online'): 17356,
 ('Meal Plan 1', 'Offline'): 7988,
 ('Meal Plan 1', 'Corporate'): 1996,
 ('Meal Plan 1', 'Complementary'): 370,
 ('Meal Plan 1', 'Aviation'): 125,
 ('Meal Plan 2', 'Offline'): 2365,
 ('Meal Plan 2', 'Online'): 923,
 ('Meal Plan 2', 'Complementary'): 11,
 ('Meal Plan 2', 'Corporate'): 6,
 ('Meal Plan 3', 'Complementary'): 4,
 ('Meal Plan 3', 'Offline'): 1,
 ('Not Selected', 'Online'): 4935,
 ('Not Selected', 'Offline'): 174,
 ('Not Selected', 'Corporate'): 15,
 ('Not Selected', 'Complementary'): 6}

# get the labels and values
labels = list(data.keys())
values = list(data.values())

# create a bar chart of the data
plt.bar(range(len(labels)), values)

# set the tick labels to be the labels
plt.xticks(range(len(labels)), labels, rotation=88)



# set the axis labels
plt.xlabel('Meal Plan and Market Segment Type')
plt.ylabel('Number of Bookings')

# set the title
plt.title('Distribution of Bookings by Meal Plan and Market Segment Type')





# display the chart
plt.show()


# In[480]:


import matplotlib.pyplot as plt

# define the data
data = {('Meal Plan 1', 'Online'): 17356,
 ('Meal Plan 1', 'Offline'): 7988,
 ('Meal Plan 1', 'Corporate'): 1996,
 ('Meal Plan 1', 'Complementary'): 370,
 ('Meal Plan 1', 'Aviation'): 125,
 ('Meal Plan 2', 'Offline'): 2365,
 ('Meal Plan 2', 'Online'): 923,
 ('Meal Plan 2', 'Complementary'): 11,
 ('Meal Plan 2', 'Corporate'): 6,
 ('Meal Plan 3', 'Complementary'): 4,
 ('Meal Plan 3', 'Offline'): 1,
 ('Not Selected', 'Online'): 4935,
 ('Not Selected', 'Offline'): 174,
 ('Not Selected', 'Corporate'): 15,
 ('Not Selected', 'Complementary'): 6}

# define the colors for each segment type
colors = {'Online': 'tab:blue',
          'Offline': 'tab:orange',
          'Corporate': 'tab:green',
          'Complementary': 'tab:red',
          'Aviation': 'tab:purple'}

# get the labels and values
labels = list(data.keys())
values = list(data.values())

# create a list of colors based on the segment type
segment_colors = [colors[label[1]] for label in labels]

# create a bar chart of the data
plt.bar(range(len(labels)), values, color=segment_colors)

# set the tick labels to be the labels
plt.xticks(range(len(labels)), labels, rotation=83)

# set the axis labels
plt.xlabel('Meal Plan and Market Segment Type')
plt.ylabel('Number of Bookings')

# set the title
plt.title('Distribution of Bookings by Meal Plan and Market Segment Type')

# add labels on top of each bar
for i, v in enumerate(values):
    plt.text(i, v, str(v), ha='center', va='bottom')



# display the chart
plt.show()


# 
# ## meal plan 1 - first option for both adults and kids
# ## no meal - adults 
# ## meal plan 3 - not success
# ## Aviation only plan 1 
# ## meal 2 has his highest success by offline segment
# ## corporate choose meal plan 1

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Question and answers below: price of the room type related to the kind of meal ? kids more profitable over average?

# # TODO in what months there are more kids?

# In[517]:


hotel


# In[518]:


kids = hotel[["arrival_month","no_of_children","Booking_ID"]]
kids


# In[519]:


kids_merged_group_df = pd.merge(kids, merge_room_price, left_index=True, right_index=True)
kids_merged_group_df


# In[520]:


kids_merged_group_df= kids_merged_group_df.drop('Booking_ID_y', axis=1)
kids_merged_group_df= kids_merged_group_df.drop('total_nights', axis=1)
kids_merged_group_df


# In[521]:


grouped_kids_merged_group_count_df = kids_merged_group_df.groupby('no_of_children')['total_price'].count()
grouped_kids_merged_group_count_df ## count type of guests


# In[522]:


grouped_kids_merged_group_SUM_df = kids_merged_group_df.groupby('no_of_children')['total_price'].sum()
grouped_kids_merged_group_SUM_df # sum of earning by type


# In[523]:


grouped_kids_merged_group_AVG_df = kids_merged_group_df.groupby('no_of_children')['total_price'].mean()
grouped_kids_merged_group_AVG_df # average price by number of kids


# In[524]:


grouped_kids_merged_group_AVG_df  = pd.DataFrame(grouped_kids_merged_group_AVG_df) #transform all in DF
grouped_kids_merged_group_SUM_df  = pd.DataFrame(grouped_kids_merged_group_SUM_df)
grouped_kids_merged_group_count_df  = pd.DataFrame(grouped_kids_merged_group_count_df)


# In[525]:


Final_kids_merged_group_df = pd.merge(grouped_kids_merged_group_AVG_df, grouped_kids_merged_group_SUM_df, left_index=True, right_index=True)
# merging all DFs - do not delate the code below - 


# In[526]:


Final_kids_merged_group_df = pd.merge(grouped_kids_merged_group_count_df, Final_kids_merged_group_df, left_index=True, right_index=True)


# In[527]:


Final_kids_merged_group_df


# In[528]:


# change the column names
Final_kids_merged_group_df = Final_kids_merged_group_df.rename(columns={'total_price': 'total_count', 'B': 'Y'})
Final_kids_merged_group_df = Final_kids_merged_group_df.rename(columns={'total_price_x': 'avg_price', 'B': 'Y'})
Final_kids_merged_group_df = Final_kids_merged_group_df.rename(columns={'total_price_y': 'total_price', 'B': 'Y'})
Final_kids_merged_group_df


# In[529]:


a_count= ((1618+1618)/ 33577)*100
print (str(a_count) + " %  of 1 and 2 kids bookings / 0 kids")


# In[530]:


b_sum= ((508324.07 + 362731.24) / 10469988.18)*100
print (str(b_sum)+ " % of total price from group 1 and 2 kids over no kids price sum")


# ### ANSWER the % of kis is higly low, however there is a high averga earning in bookings of adult/s with 1 or 2 kids, from 3 the earning is lower than 0 kids.

# In[ ]:





# # Question: Kids Vs Adults and Month - Correlations?
# ## Answer below

# In[ ]:


group month and kids, then two dataframes, one grpah only adults other graph for kids


# In[332]:


adults_month = hotel[["no_of_adults","arrival_month"]]
kids_month = hotel[["no_of_children","arrival_month"]]


# In[333]:


adults_month


# In[334]:


hotel["no_of_children"].value_counts() 


# In[335]:


adults_month = hotel.groupby('arrival_month')['no_of_adults'].sum() # it must be sum, with count, it doesnt work, it gives times, but not sume
kids_month = hotel.groupby('arrival_month')['no_of_children'].sum()

kids_month = pd.DataFrame(kids_month)
adults_month = pd.DataFrame(adults_month)
adults_month


# In[336]:


# reset index, moving arrival_,month (index) to column

adults_month = adults_month.reset_index()
kids_month = kids_month.reset_index()
adults_month # data matchs tableau


# In[338]:


kids_month # data matchs tableau


# In[339]:


# just 1 graph to check
import matplotlib.pyplot as plt

# Sample data
x = adults_month["arrival_month"]
y = adults_month["no_of_adults"]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the line
ax.plot(x, y)

# Set the axis labels
ax.set_xlabel('Month')
ax.set_ylabel('N° of Adults')

# Set the title
ax.set_title('Adults_Month')

# Display the plot
plt.show()


# In[307]:


# just 1 graph to check
import matplotlib.pyplot as plt

# Sample data
x = kids_month["arrival_month"]
y = kids_month["no_of_children"]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the line
ax.plot(x, y)

# Set the axis labels
ax.set_xlabel('Month')
ax.set_ylabel('N° of Children')

# Set the title
ax.set_title('Children_Month')

# Display the plot
plt.show()


# In[340]:


import pandas as pd
import matplotlib.pyplot as plt

# Create sample DataFrames
#df1 = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]})
#df2 = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [2, 4, 6, 8]})

# Extract data from DataFrames
x1, y1 = adults_month["arrival_month"], adults_month["no_of_adults"]
x2, y2 = kids_month["arrival_month"], kids_month["no_of_children"]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first graph on the first subplot
axs[0].plot(x1, y1)
axs[0].set_title('N° of Adults')

# Plot the second graph on the second subplot
axs[1].plot(x2, y2)
axs[1].set_title('N° of Children')

# Display the plot
plt.show()


# In[349]:


import pandas as pd
import matplotlib.pyplot as plt

# Create sample DataFrames
#df1 = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]})
#df2 = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [2, 4, 6, 8]})

# Extract data from DataFrames
x1, y1 = adults_month["arrival_month"], adults_month["no_of_adults"]
x2, y2 = kids_month["arrival_month"], kids_month["no_of_children"]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the lines
ax.plot(x1, y1, label='Line 1')
ax.plot(x2, y2, label='Line 2')



# Set the axis labels
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')

# Set the title
ax.set_title('Comparison of two lines')

# Set y-axis limits
#ax.set_ylim(0, 60)

# Add legend
ax.legend()

# Display the plot
plt.show()


# In[367]:


import pandas as pd
import matplotlib.pyplot as plt

# Extract data from DataFrames
x1, y1 = adults_month["arrival_month"], adults_month["no_of_adults"]
x2, y2 = kids_month["arrival_month"], kids_month["no_of_children"]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the lines
ax.plot(x1, y1, label='N°Adults')

# Create a new y-axis
ax2 = ax.twinx()

# Plot Line 2 on the second y-axis
ax2.plot(x2, y2, 'r-', label='N°Children')
ax2.set_ylabel('N° of Children')
ax2.tick_params(axis='y')

# Set the axis labels
ax.set_xlabel('Arrival Months')
ax.set_ylabel('N° of Adults')

# Set the title
ax.set_title('N° Children Vs Adults Monthly')

# Add legend
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, -0.2))

# Display the plot
plt.show()


# # Answer: tableau - adult constant increase per month and matching in somehow kid's tendency, which seem correlated to specific months.
# ## Adults and Kids match on Months:  4, 5, 7-8, 10 and 11-12 - Basically kids increment goes along with holidays. Adults recover better than kids.

# In[ ]:





# In[483]:


hotel.info()


# # Earnings by segment

# In[486]:


market_ID = hotel[["Booking_ID","market_segment_type"]]
market_ID


# In[482]:


kids_merged_group_df


# In[490]:


merged_segment_df = pd.merge(market_ID, kids_merged_group_df, left_index=True, right_index=True)
merged_segment_df


# In[491]:


merged_segment_df= merged_segment_df.drop('arrival_month', axis=1)
merged_segment_df= merged_segment_df.drop('Booking_ID_x', axis=1)
merged_segment_df= merged_segment_df.drop('no_of_children', axis=1)

merged_segment_df


# In[550]:


#SUM
grouped_merged_segment_SUM_total= merged_segment_df.groupby('market_segment_type')["avg_price_per_room","total_price"].sum()
grouped_merged_segment_SUM_total 
# total price = price with extras and nights = total final value


# In[539]:


#AVG
grouped_merged_segment_AVG= merged_segment_df.groupby('market_segment_type')[["avg_price_per_room","total_price"]].mean()
grouped_merged_segment_AVG

# within each type of room, there are different prices, that is why there are relevant differences between avg_price_room and total price.
# total price = price with extras and nights = total final value


# In[500]:


merged_segment_count= merged_segment_df["market_segment_type"].value_counts()
merged_segment_count


# In[501]:


merged_segment_count = pd.DataFrame(merged_segment_count)
merged_segment_count


# In[544]:


merged_segment_countVStotal = pd.merge(grouped_merged_segment_SUM_total, merged_segment_count, left_index=True, right_index=True)
merged_segment_countVStotal


# In[545]:


# change the column names
Final_merged_segment_countVSprice = merged_segment_countVSprice.rename(columns={'market_segment_type': 'segment_count'})
Final_merged_segment_countVSprice


# In[548]:


import pandas as pd



# Calculate the total sum of segment_count
total_segment_count = Final_merged_segment_countVSprice['segment_count'].sum()

# Calculate the percentage for each row
Final_merged_segment_countVSprice['segment_percentage'] = Final_merged_segment_countVSprice['segment_count'] / total_segment_count * 100

# Print the resulting dataframe
Final_merged_segment_countVSprice


# In[555]:


Final_merged_segment_countVSprice[["segment_count","segment_percentage","total_price"]]


# In[556]:


import pandas as pd



# Calculate the total sum of segment_count
total_segment_count = Final_merged_segment_countVSprice['total_price'].sum()

# Calculate the percentage for each row
Final_merged_segment_countVSprice['Price_percentage'] = Final_merged_segment_countVSprice['total_price'] / total_segment_count * 100

# Print the resulting dataframe
Final_merged_segment_countVSprice


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Pushing into SQL

# In[46]:


import mysql.connector   #CREATING DATABASE' 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lupitabonita1010"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Hotel") # the aprt of CREATE DATABASE = MUTS BE KEEP IT AS ITS; SINCE ITS A CODE


# In[47]:


#cheking if database exist

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lupitabonita1010"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[52]:


#Or you can try to access the database when making the connection:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lupitabonita1010",
  database="Hotel"
) #If the database does not exist, you will get an error.


# In[53]:


# import the module
from sqlalchemy import create_engine
import pymysql


# In[54]:


# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Lupitabonita1010",
                               db="Hotel"))


# In[56]:


hotel.to_sql('Hotel', con = engine, if_exists = 'append', chunksize = 1000) # inserted in MySQL


# In[39]:


hotel


# In[ ]:




