#!/usr/bin/env python
# coding: utf-8

# In[296]:


import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'Germany ICP - Case study-Copy1.xlsx'  # Replace with your file path

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)


# In[ ]:





# In[297]:


df = df.drop('Company_country_name', axis=1)
df 


# In[298]:


new_df = df.iloc[:, [3,4,5, 6,14,11,13]]
new_df


# In[17]:


#Converting objects into numricals

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
new_df["Revised_number_of_employees"] = label_encoder.fit_transform(new_df["Revised_number_of_employees"])
new_df["Deal_Provenance"] = label_encoder.fit_transform(new_df["Deal_Provenance"])
new_df["Deal_Origin"] = label_encoder.fit_transform(new_df["Deal_Origin"])
new_df["Industry"] = label_encoder.fit_transform(new_df["Industry"])
new_df["Decision_Maker"] = label_encoder.fit_transform(new_df["Decision_Maker"])
new_df["Champion"] = label_encoder.fit_transform(new_df["Champion"])


# In[18]:


#renaming since it doesnt indentify
new_df = new_df.rename(columns={new_df.columns[2]: 'Deal_Origin'})
new_df = new_df.rename(columns={new_df.columns[6]: 'Decision_Maker'})
new_df = new_df.rename(columns={new_df.columns[0]: 'Revised_number_of_employees'})
new_df = new_df.rename(columns={new_df.columns[4]: 'Industry'})


# In[19]:


new_df


# In[20]:


for i, col_name in enumerate(new_df.columns):
    print(f"Column {i}: {col_name}")


# In[21]:


new_df


# In[22]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corr = new_df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr, mask=mask,cmap='coolwarm', vmin=-1,vmax=1,annot=True, square=True)


# In[23]:


new_df.corr()


# In[24]:


#select industry, round(avg(Revised_number_of_employees),2),
#round(avg(Amount_in_Euro),2),round(sum(Amount_in_Euro),2) from Company group by industry;


# In[25]:


#---------------------------------------- INDUTRIAL SECTOR PROFIL-------------------------------------


# In[26]:


df["Revised_number_of_employees"].mean()


# In[27]:


import pandas as pd

# Group by the "industry" column and calculate the mean for "Revised_number_of_employees"
mean_employees_by_industry = df.groupby('Industry')['Revised_number_of_employees'].mean()

# Convert the result to a DataFrame (optional)
mean_employees_by_industry = mean_employees_by_industry.reset_index()

# Rename the columns for clarity (optional)
mean_employees_by_industry.columns = ['Industry', 'mean_employees']

# Display the result
print(mean_employees_by_industry)


# In[28]:


median_employees_by_industry = df.groupby('Industry')['Revised_number_of_employees'].median()
median_employees_by_industry


# In[29]:


import pandas as pd

# Group by the "industry" column and calculate the mean for "Revised_number_of_employees"
df_sume = df.groupby('Industry')['Amount_in_Euro'].sum()
df_sume


# In[30]:


import pandas as pd

# Group by the "industry" column and calculate the mean for "Revised_number_of_employees"
df_mean_money = df.groupby('Industry')['Amount_in_Euro'].mean()
df_mean_money


# In[ ]:





# In[31]:


# Combine DataFrames based on the "Industry" column
combined_df = mean_employees_by_industry.merge(median_employees_by_industry, on="Industry")
combined_df = combined_df.merge(df_sume, on="Industry")

# Display the combined DataFrame
combined_df


# In[32]:


# Combine DataFrames based on the "Industry" column
combined_df = combined_df.merge(df_mean_money, on="Industry")

# Display the combined DataFrame
combined_df


# In[33]:


#renaming since it doesnt indentify
#combined_df = combined_df.rename(columns={combined_df.columns[2]: 'Median_number_of_employees'})
combined_df = combined_df.rename(columns={combined_df.columns[3]: 'Sum_Amount_in_Euro'})
combined_df = combined_df.rename(columns={combined_df.columns[4]: 'Mean_Amount_in_Euro'})
combined_df = combined_df.rename(columns={combined_df.columns[2]: 'Median_number_of_employees'})


# In[34]:


df_industry_value_counts= df["Industry"].value_counts()
df_industry_value_counts


# In[35]:


# Combine DataFrames based on the "Industry" column
combined_df = combined_df.merge(df_industry_value_counts, on="Industry")

# Display the combined DataFrame
combined_df


# In[36]:


#renaming since it doesnt indentify
#combined_df = combined_df.rename(columns={combined_df.columns[2]: 'Median_number_of_employees'})
combined_df = combined_df.rename(columns={combined_df.columns[5]: 'Count_industry'})
combined_df[["Industry","Count_industry","mean_employees","Median_number_of_employees","Sum_Amount_in_Euro","Mean_Amount_in_Euro"]]


# In[37]:


# Sort the DataFrame in descending order based on "Mean_Amount_in_Euro"
combined_df = combined_df.sort_values(by="Mean_Amount_in_Euro", ascending=False)

# Display the sorted DataFrame
combined_df


# In[38]:


combined_df[["Industry","Count_industry","mean_employees","Median_number_of_employees","Sum_Amount_in_Euro","Mean_Amount_in_Euro"]]


# In[39]:


# relevant Enteirtainment only 7 accounts in this field with the hights avg price, potential.
# tourism, just one account not relevant.
#Industrials third avg position and second main industry after 'Others' and hights income source comming from. Focus here
#Information and technology has an average price ordinal, but third biggest field sector and sum_amount.

#Clients have a 'medium' size company the avg and medain number of employees. It seems there are not yet 'huge' players


# In[40]:


df["Amount_in_Euro"].sum() # total sume matches


# In[41]:


combined_df.sum()  # total sume matches


# In[42]:


via_new_df = df.iloc[:, [0,1,3,4,5, 6,15,14,11,13]]
via_new_df


# In[43]:


### correlation Emplyess vs money


# In[44]:


easy_correlation_df = df.iloc[:, [3,1]]
easy_correlation_df


# In[45]:


# correlation 9 between money and number of emploeys
correlation_check = df['Revised_number_of_employees'].corr(df['Amount_in_Euro'])
correlation_check


# In[46]:


# comapre correlation wihtin industry and heatmap
industry_correlation_df = df.iloc[:, [3,1,14]]
industry_correlation_df


# In[47]:


# encoding categoricals into numericals for heatmap
industry_correlation_df["Industry"] = label_encoder.fit_transform(industry_correlation_df["Industry"])
industry_correlation_df["Industry"] 


# In[48]:


industry_correlation_df


# In[ ]:


# correlation Size & Investment


# In[49]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corr = industry_correlation_df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr, mask=mask,cmap='coolwarm', vmin=-1,vmax=1,annot=True, square=True)


# In[50]:


# correlation betewwn decisionmaking CEO and company size

decision_champion_size_correlation = new_df
decision_champion_size_correlation = decision_champion_size_correlation.drop('Deal_Provenance', axis=1)
decision_champion_size_correlation = decision_champion_size_correlation.drop('Create_Date', axis=1)
decision_champion_size_correlation = decision_champion_size_correlation.drop('Industry', axis=1)
decision_champion_size_correlation = decision_champion_size_correlation.drop('Deal_Origin', axis=1)
decision_champion_size_correlation


# In[51]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corr = decision_champion_size_correlation.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr, mask=mask,cmap='coolwarm', vmin=-1,vmax=1,annot=True, square=True)


# In[134]:


decision_champion_size_correlation.corr()


# --------

# # Correlation experiment, Champion vs Company size = 0.3
# ## I will check the avg, median and mode size per company grouped by champion

# --------

# In[285]:


### Relevant tech note aside: 
### merged_correlation_test_X file at the bottom,
## is saved/run before the otehr dfs, since the Champion was saved a numerical insted of keeping it as categorical


# ## original DF reagrding correlations

# In[263]:


correlation_test = decision_champion_size_correlation
correlation_test


# In[264]:


# Calcular la media de empleados por empresa para cada 'champion'
correlation_test_avg= correlation_test
correlation_test_avg = df.groupby('Champion')['Revised_number_of_employees'].mean().reset_index()
correlation_test_avg.columns = ['Champion', 'Avg_employees']


# In[265]:


merged_correlation_test_avg= correlation_test_avg
correlation_test_avg


# In[246]:


# transform column Champion into numerical again
correlation_test_avg["Champion"] = label_encoder.fit_transform(correlation_test_avg["Champion"])


# In[247]:


correlation_test_avg


# In[248]:


# Calcular la correlación entre la nueva columna 'moda_empleados' y 'champion'
correlation_test_avg = correlation_test_avg['Champion'].corr(correlation_test_avg['Avg_employees'])
correlation_test_avg


# ## median

# In[275]:


correlation_test_median = correlation_test

# Calcular la mediana de empleados por empresa para cada 'champion'
correlation_test_median = df.groupby('Champion')['Revised_number_of_employees'].median().reset_index()
correlation_test_median.columns = ['Champion', 'Median_of_employees']

#for future merged
merged_correlation_test_median= correlation_test_median

correlation_test_median


# In[250]:


# transform column Champion into numerical again
correlation_test_median["Champion"] = label_encoder.fit_transform(correlation_test_median["Champion"])
correlation_test_median


# In[251]:


# Calcular la correlación entre la nueva columna 'moda_empleados' y 'champion'
correlation_test_median = correlation_test_median['Champion'].corr(correlation_test_median['Median_of_employees'])
correlation_test_median


# ##  mode
# 

# In[252]:


correlation_test_mode= correlation_test


# In[260]:


# Calcular la moda de empleados por empresa para cada 'champion'
correlation_test_mode = df.groupby('Champion')['Revised_number_of_employees'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None).reset_index()
correlation_test_mode.columns = ['Champion', 'Mode_employees']

#for future mergedf
merged_correlation_test_mode= correlation_test_mode
correlation_test_mode


# In[254]:


# transform column Champion into numerical again
correlation_test_mode["Champion"] = label_encoder.fit_transform(correlation_test_mode["Champion"])
correlation_test_mode


# In[255]:


# Calcular la correlación entre la nueva columna 'moda_empleados' y 'champion'
correlation_test_mode = correlation_test_mode['Champion'].corr(correlation_test_mode['Mode_employees'])
correlation_test_mode


# In[ ]:





# ## correlations merged

# In[279]:


# Combinar los DataFrames en función de la columna 'champion'
merged_test_df = pd.merge(merged_correlation_test_mode, merged_correlation_test_median, on='Champion')
merged_test_df = pd.merge(merged_test_df, merged_correlation_test_avg, on='Champion')
merged_test_df


# In[282]:


saved_test_version_df = merged_test_df
saved_test_version_df


# ## Global company size correlation/ Champion  Vs  Media, Mode & Mean/Champion

# In[ ]:





# In[286]:


# transform column Champion into numerical again
merged_test_df["Champion"] = label_encoder.fit_transform(merged_test_df["Champion"])
merged_test_df


# In[287]:


merged_test_df.corr()


# In[288]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corr = merged_test_df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr, mask=mask,cmap='coolwarm', vmin=-1,vmax=1,annot=True, square=True)


# #### In summary, there is a weak positive correlation between 'Champion' and company size, and the strength of the correlation varies from very weak to considerable depending on the specific company size metric (mode, median, or average) you are considering.

# In[ ]:


# exporint file for excel


# In[289]:


# Specify the file path for the Excel file
excel_file_path = 'output_file.xlsx'

# Export the DataFrame to Excel
saved_test_version_df.to_excel(excel_file_path, index=False)


# ### I grouped CEO & CFO vs 'Smaller position'

# In[293]:


import pandas as pd

# Creating the DataFrame
data = {'Champion': [1, 2, 2, 1, 1, 1, 1, 1],
        'Avg_employees': [26, 22.79166667, 15, 37.39344262, 39.08108108, 25, 23, 83.75]}

Bigvsothers_df = pd.DataFrame(data)

# Display the DataFrame
Bigvsothers_df


# In[295]:


# Calcular la correlación entre la nueva columna 'moda_empleados' y 'champion'
Bigvsothers_df = Bigvsothers_df['Champion'].corr(Bigvsothers_df['Avg_employees'])
Bigvsothers_df

# Some tendecy 


# # TIME (month) AND INDUSTRIAL SECTOR

# In[300]:


inudstry_date_df = new_df
inudstry_date_df


# In[303]:


# Convert the 'datetime_column' to a datetime object
inudstry_date_df['Create_Date'] = pd.to_datetime(inudstry_date_df['Create_Date'])

# Extract the month and create a new column 'month'
inudstry_date_df['month'] = inudstry_date_df['Create_Date'].dt.month

# Display the DataFrame with the extracted month
inudstry_date_df[['Create_Date', 'month']]


# In[304]:


inudstry_date_df


# In[305]:


# Group by 'industry' and 'month', then count the number of accounts
inudstry_date_df = inudstry_date_df.groupby(['Industry', 'month']).size().reset_index(name='number_of_accounts')
inudstry_date_df


# In[308]:


inudstry_date_df


# In[309]:


#renaming since it doesnt indentify
inudstry_date_df = inudstry_date_df.rename(columns={inudstry_date_df.columns[0]: 'Industry'})


# In[312]:


inudstry_date_df["Industry"]


# In[313]:


# turning into numerical
inudstry_date_df["Industry"] = label_encoder.fit_transform(inudstry_date_df["Industry"])
inudstry_date_df["Industry"]


# In[314]:



inudstry_date_df.corr()


# In[315]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

corr = inudstry_date_df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr, mask=mask,cmap='coolwarm', vmin=-1,vmax=1,annot=True, square=True)


# In[ ]:




