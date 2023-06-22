#!/usr/bin/env python
# coding: utf-8

# #                 Final Project - Database Management in Cloud                              
# 
# 
# ## How to find final functions? Search for ' Final Project' and those will be the summaries. The rest is additional information.

# ---------------------------------------

# # API AND MONDE B FROM test-api
# # MODE B - GET DATA FROM GOOGLE SHEET AS DATAFRAME

# In[13]:


gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
] #standar
credentials = ServiceAccountCredentials.from_json_keyfile_name('mythic-delight-370211-09579ff6aae2.json', scope)
url = "https://docs.google.com/spreadsheets/d/1_mFu_NgmarXt6QbXPFGdWh7LV4xZPpe4pVXDsPCIkBs/edit#gid=02"


# In[10]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
] #standar
credentials = ServiceAccountCredentials.from_json_keyfile_name('mythic-delight-370211-09579ff6aae2.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open("Final Project").worksheet("Input") #sheet name
next_row = next_available_row(worksheet)

creds= ServiceAccountCredentials.from_json_keyfile_name("mythic-delight-370211-09579ff6aae2.json", scope)
client= gspread.authorize(creds)
python_test= client.open("Final Project").worksheet("StockOverview")
time.sleep(1)
#insert on the next available row

#worksheet.update_acell("A{}".format(next_row), "cccc") # what to upload
#worksheet.update_acell("B{}".format(next_row), somevar2)


# In[172]:





# In[173]:


response = requests.get(url)


# In[174]:


response.status_code # 200 status code means OK!


# In[175]:


url


# In[176]:


response.content


# In[177]:


soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)


# In[179]:


sh= gc.open("Final Project").worksheet("OrderTracker")


# In[65]:


# get all the records of the data
records_data = sh.get_values() 

# view the data
records_data


# In[66]:


records_df = pd.DataFrame.from_dict(records_data)
new_header = records_df.iloc[0] #grab the first row for the header

records_df.columns = new_header #copy the header row as the df header

records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
        axis=0, 
        inplace=True)

records_df


# -------------------------------------

# In[48]:


import pandas as pd # groupby from MySQL
df= pd.read_csv("Index.xml",decimal=',') #repalce commas by dotsnext_available_row
Index_df=df
Index_df


# --------------------------------------
# 

# # MODE A-  DOWNLOAD THE DATA IN FILE WEB FORMAT BUT ITS NOT AUTOMATED, MUST BE DOWNLOADED IT MANUALLY
# https://www.analyticslane.com/2020/09/21/importar-datos-desde-google-spreadsheets-en-python-con-pandas/

# In[49]:


import pandas as pd

url1="https://docs.google.com/spreadsheets/d/e/2PACX-1vR53_WotSs9zjU3cF-pasH3CPJnzU76ugbiSoGttv5BQp6lZt3TtIehyF7HD9E-J7NH7C261w981pga/pub?output=csv"
df_DESDEWEB = pd.read_csv(url1)


# In[50]:


df_DESDEWEB  


# In[70]:


https://www.youtube.com/watch?v=n0EkLvSOWc8  ## como sacar data de la sheet a python


# ## Importar DF en Spreadsheet

# In[213]:


import pandas as pd  #version with head
import gspread
import time
from gspread_dataframe import set_with_dataframe
gc = gspread.service_account(filename='mythic-delight-370211-09579ff6aae2.json')
sh = gc.open("Final Project").worksheet("SKU-List")
worksheet = gc.open("Final Project").worksheet("SKU-List")
next_row = next_available_row(worksheet) #----- new

#next_row=int(next_row)
set_with_dataframe(worksheet, Index_df)

time.sleep(1)


# # Insert name file and export Stock analysy to Spread

# #### it can be added the option of grapping the data from the google spread sheet, read it and send it back to the Stock sheet already proccessed - Below 2 versions to import the data from Spreadsheets

# In[180]:


import gspread
import pandas as pd
gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
sh= gc.open("Final Project").worksheet("OrderTracker")

# get all the records of the data
records_data = sh.get_values() 

records_df = pd.DataFrame.from_dict(records_data)
new_header = records_df.iloc[0] #grab the first row for the header

records_df.columns = new_header #copy the header row as the df header

records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
        axis=0, 
        inplace=True)


# In[54]:


import pandas as pd

url1="https://docs.google.com/spreadsheets/d/e/2PACX-1vR53_WotSs9zjU3cF-pasH3CPJnzU76ugbiSoGttv5BQp6lZt3TtIehyF7HD9E-J7NH7C261w981pga/pub?output=csv"
df_DESDEWEB = pd.read_csv(url1)


# # BI Overview in StockOverview (Final Project)
# introudce file name and process everything

# In[40]:


def Stock_file_Spread(): # SQL_Purchase_Order_Report.xlsx    Goood one -> # New_Purchase_Order_Report.xlsx.xlsx
    import pandas as pd
    x=input()
    Excel_file = pd.read_excel(x)
    Copy_1= Excel_file
    Sorted_copy= Copy_1[["Brand","Supplier Supplier Name","Cancellation Reason (PO Position Number)","Value_init_Ordered","Value_Ordered_Canc& Closing","Value_Overdelivered","Value_Canceled","Value_Open"]]
    
    New_sorted = Sorted_copy[Sorted_copy["Cancellation Reason (PO Position Number)"] != "INTERNAL_MISTAKE"]
    New_sorted =Sorted_copy[Sorted_copy["Cancellation Reason (PO Position Number)"] != "CANCELED_BY_ZALANDO"]
    New_sorted =Sorted_copy[Sorted_copy["Cancellation Reason (PO Position Number)"] != "OTHER"]
    New_sorted_brand =New_sorted.groupby(['Brand']).sum().reset_index()
    

    Sorted_nan=New_sorted_brand.dropna()
    
    
    ### cancelations per brand

    Sorted_nan_cancellations= pd.DataFrame(((Sorted_nan["Value_Canceled"])/Sorted_nan["Value_init_Ordered"])*100)
    Sorted_nan_cancellations = round(Sorted_nan_cancellations,2)
    Sorted_nan_cancellations.index = New_sorted_brand.Brand
    Sorted_nan_cancellations.columns = ["%cancel"]
    
    Sorted_nan_cancellations = Sorted_nan_cancellations.reset_index() #reset the index again, brand are settled as index, and not show in G.Spread, they must be as column to be exported
    Sorted_nan_cancellations=pd.DataFrame(Sorted_nan_cancellations)
    #Sorted_nan_cancellations
    
    #OPEN VALUE per brand
    Sorted_nan_open=pd.DataFrame(Sorted_nan["Value_Open"]/Sorted_nan["Value_init_Ordered"]*100)
    Sorted_nan_open= round(Sorted_nan_open,2)
    Sorted_nan_open.index = New_sorted_brand.Brand
    Sorted_nan_open.columns = ["%open_value"]
    
    Sorted_nan_open = Sorted_nan_open.reset_index() #reset the index again, brand are settled as index, and not show in G.Spread, they must be as column to be exported
    Sorted_nan_open=pd.DataFrame(Sorted_nan_open)
    #Sorted_nan_open
    
    #inicial cancel and open üper brand
    InicialVSperbrand= ((Sorted_nan["Value_Canceled"]+Sorted_nan["Value_Open"])/Sorted_nan["Value_init_Ordered"])*100
    InicialVSperbrand.index = New_sorted_brand.Brand
   
    InicialVSperbrand=pd.DataFrame(InicialVSperbrand)
    InicialVSperbrand.columns = ["%canceled_waiting_VS_initial_order"]
    InicialVSperbrand= round(InicialVSperbrand,2)
    InicialVSperbrand = InicialVSperbrand.reset_index() #reset the index again, brand are settled as index, and not show in G.Spread, they must be as column to be exported
    InicialVSperbrand=pd.DataFrame(InicialVSperbrand)
    #InicialVSperbrand
    #--------------------------------Total values--------------------------------
    
    t_c=New_sorted_brand["Value_Canceled"].sum()/New_sorted_brand["Value_init_Ordered"].sum()*100
    tc= round(t_c,2)
    #tc

    t_opv=New_sorted_brand["Value_Open"].sum()/New_sorted_brand["Value_init_Ordered"].sum()*100
    t_opv= round(t_opv,2) # open value based on total initial order, including cancellations
    #t_opv
    
    t_opvf=New_sorted_brand["Value_Open"].sum()/(New_sorted_brand["Value_init_Ordered"].sum()-New_sorted_brand["Value_Canceled"].sum())*100
    t_opvf= round(t_opvf,2) #New open stock based in current orders after removing the cancellations
    #t_opvf # open stock after removing cancelations
    
    
    

    #t_b=(New_sorted_brand["Value_Canceled"].sum()+New_sorted_brand["Value_Open"].sum())/New_sorted_brand["Value_init_Ordered"].sum()
   # t_b=round(t_b,2)
    #t_b   #57%(with internal mistake)- 51% of orignal ordered stock is not comming after removing Internal mistakes
    
    #t_b is kind of already added troutgh the presvious mentioned open variables
    
    #--------------------------------------------MERGE----------------------------------------------------------
    final_df = pd.concat([Sorted_nan_cancellations, Sorted_nan_open,  InicialVSperbrand])
    final_df =final_df.groupby(['Brand']).sum().reset_index()


    
    
    #---------------------------------------API---------------------------------------------------------------------------
    import pandas as pd  #version with head
    import gspread
    from gspread_dataframe import set_with_dataframe
    gc = gspread.service_account(filename='mythic-delight-370211-09579ff6aae2.json')
    sh = gc.open("Final Project").worksheet("StockOverview")
    worksheet = gc.open("Final Project").worksheet("StockOverview")
    next_row = next_available_row(worksheet)
    creds= ServiceAccountCredentials.from_json_keyfile_name("mythic-delight-370211-09579ff6aae2.json", scope)
    client= gspread.authorize(creds)
    python_test= client.open("Final Project").worksheet("StockOverview")
    
    time.sleep(1)
    
    
#---------------------------------------------------  HERE FILE----------------------------------------
        
    
    set_with_dataframe(worksheet, final_df) # HERE!!!!!!!!!!!!!!!!!!!!!!! Sorted_copy_2_Open is thee file to upload!!!!!
    
    python_test.update_cell(1,6,"Total cancelled value over initial Ordder" )
    python_test.update_cell(2,6,tc )
    python_test.update_cell(1,7,"Total open stock value vs Original Order (cancellations included) " )
    python_test.update_cell(2,7,t_opv )
    python_test.update_cell(1,8,"Open stock value after removing cancelations vs Original Order" )
    python_test.update_cell(2,8,t_opvf )

    
    
    #python_test.update_cell(1,5, )
    #python_test.update_cell(1,10, Sorted_nan_open)
    #python_test.update_cell(1,15, nan_balance_brand)
    #python_test.update_cell(1,20, InicialVSperbrand)
        
        
        
    time.sleep(1)
    
    return print("It ran well")


# In[65]:


Stock_file_Spread()   # New_Purchase_Order_Report.xlsx.xlsx   #Sorted_copy_2_Open
 


# In[ ]:





# # Input SKU

# In[8]:


def Input_SKU():
    
    Config_SKU= Index_df["Config_SKU"]
    x=input()
    
    import pandas as pd  #version with head
    import gspread
    from gspread_dataframe import set_with_dataframe
    gc = gspread.service_account(filename='mythic-delight-370211-09579ff6aae2.json')
    sh = gc.open("Final Project").worksheet("Input")
    worksheet = gc.open("Final Project").worksheet("Input")
    next_row = next_available_row(worksheet) #----- new
    
    for i in Config_SKU: #   0LF11A027-A11
        
        if(i == x):
            print("Element Exists ")
            print(Index_df.loc[Index_df['Config_SKU'] == x,'Season_Type'])       
            #a = round(Index_df.loc[Index_df['Config_SKU'] == x,"PurchasePrice_bDisc"],2)
            b = Index_df.loc[Index_df['Config_SKU'] == x,"Brand"]
            c = Index_df.loc[Index_df['Config_SKU'] == x,"Commodity_Group_3"]
            #print(a)
        
            #print(b)
        
            #print(c)    
    Input_df=Index_df.loc[Index_df["Config_SKU"] == x]
    #next_row=int(next_row)
    set_with_dataframe(worksheet, Input_df )

    time.sleep(1)
    return Input_df 


# In[14]:


Input_SKU() #       0LF11A027-A11


# ## Input SKU export into Sheets in last row but in JSON format - all in one line

# In[52]:


Config_SKU= Index_df["Config_SKU"]
x=input()

for i in Config_SKU: #   0LF11A027-A11
    if(i == x):
        print("Element Exists ")
        print(Index_df.loc[Index_df['Config_SKU'] == x,'Season_Type'])       #getting value that matchs
        #a = round(Index_df.loc[Index_df['Config_SKU'] == x,"PurchasePrice_bDisc"],2) #im suing the DF version of string, that is why i put off this variable called a, since its a number and the format for web doesnt read it
        b = Index_df.loc[Index_df['Config_SKU'] == x,"Brand"]
        c = Index_df.loc[Index_df['Config_SKU'] == x,"Commodity_Group_3"]
       # print(a)
        print(b)
        print(c)
Input_df=Index_df.loc[Index_df["Config_SKU"] == x]
time.sleep(1)
import json
#json.dumps(Input_df.to_dict())# transform into JSON


Input_df= Input_df.to_json()


def next_available_row(worksheet):  ##get last row
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
] #standar
credentials = ServiceAccountCredentials.from_json_keyfile_name('mythic-delight-370211-09579ff6aae2.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open("Final Project").worksheet("Input") #sheet name
next_row = next_available_row(worksheet)

#insert on the next available row
 
worksheet.update_acell("A{}".format(next_row), Input_df)

#worksheet.update_acell("A{}".format(next_row), json.dumps(Input_df.to_dict())) #last part in this code= what to upload
#worksheet.update_acell("B{}".format(next_row), somevar2)


# In[225]:


Input_df = '{"Config_SKU":{"0":"0LF11A027-A11"},"Season_Type":{"0":"All Spring-Summer"},"EAN":{"0":2001813394315.0},"PurchasePrice_bDisc":{"0":63.6},"Brand":{"0":"L37"},"Main_Supplier":{"0":"Loft37 Sp. z o.o."},"Commodity_Group_3":{"0":"Ballerinas"}}'


# # WH capacity -  Final Project

# In[53]:


def storage(): 
    
    import gspread #getting access
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    sh= gc.open("Final Project").worksheet("OrderTracker")
    records_data = sh.get_values() 
    # get all the records of the data
    records_data = sh.get_values()  
    #wh_total=1440
    
    
    import pandas as pd
  
    # get all the records of the data
    records_data = sh.get_values() 
    records_df = pd.DataFrame.from_dict(records_data)
    new_header = records_df.iloc[0] #grab the first row for the header
    records_df.columns = new_header #copy the header row as the df header
    records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
        axis=0, 
        inplace=True)
    WH_Capacity=records_df["Warehouse_Capacity"].iloc[0]
    WH_Capacity= float(WH_Capacity.replace(",",".").strip(""))


    
    for i in range(1):
        n_sku = int (input()) 
        volume_sneakers = 5.6
            
        future_space =WH_Capacity
        check=future_space
        
        if check -(volume_sneakers*n_sku) < 0:
            balance_after= volume_sneakers*n_sku
            per_sku=round(balance_after/volume_sneakers,2)
            per_sku = int(per_sku) #esta es la cantidad que introduje
            new= WH_Capacity/volume_sneakers #calcula unitdades q faltan apra el max      
            new=str(round(new) )
            check = future_space   
            print("Reached limit of space " + new + " units above limit" ) #bien
            
        elif check -(volume_sneakers*n_sku) >= 0:  #rvisar
            future_space = future_space - (volume_sneakers*n_sku)
            wh_total= future_space
            new= wh_total/volume_sneakers #calcula unitdades q faltan apra el max      
            new=str(round(new) )

            q=(future_space/WH_Capacity)*100
            q1=round(q,2)
            #q2=(WH_Capacity - (future_space/WH_Capacity))
            
            #q2= (future_space/WH_Capacity) to know % left free
           # q2=(1-q2)*100 
        
            q2= (WH_Capacity - future_space)
            q2= WH_Capacity - q2 
        
        
            print("Space available in WH: " +  str(q1) + "%" + " by " + new +" units left.")  
            print("Space left: " + str(round(q2,3)) +" Sqm left")
            
            import gspread #getting access
            gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
            sh= gc.open("Final Project").worksheet("OrderTracker")
            sh.update("AG2",q2) #updating cell with updated space left


# In[54]:


storage()


# In[55]:


def WH_capacity (wh_total):
    
    import gspread #getting access
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    sh= gc.open("Final Project").worksheet("OrderTracker")
    sh.update("AG2",wh_total) #updating cell with updated space left
    wh_total=wh_total


# In[56]:


WH_capacity(2000) # add into Sheet WH space


# In[ ]:





# # Final SKU Input for Only 1 Purchase - Import and export from/to G.Sheet
# ## Complex Invoice 
# 
# # Final Project
#  

# In[57]:


def One_SKU_Input():
    
    import gspread
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import time
    
    
    def next_available_row(worksheet): ## KEY DEF FOR EXPORTING'
        str_list = list(filter(None, worksheet.col_values(1)))
        return str(len(str_list)+1)
        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive'] #standar
        credentials = ServiceAccountCredentials.from_json_keyfile_name('mythic-delight-370211-09579ff6aae2.json', scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open("Final Project").worksheet("Input") #sheet name
        next_row = next_available_row(worksheet)

        creds= ServiceAccountCredentials.from_json_keyfile_name("mythic-delight-370211-09579ff6aae2.json", scope)
        client= gspread.authorize(creds)
        python_test= client.open("Final Project").worksheet("StockOverview")
        time.sleep(1)   # FUNCTION TO EXPORT INTO SPREADSHEET BELOW 
                        # set_with_dataframe(worksheet, Input_df )
    
    
    
    
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    SKU_sh= gc.open("Final Project").worksheet("SKU-List")
    url_SKU="https://docs.google.com/spreadsheets/d/1_mFu_NgmarXt6QbXPFGdWh7LV4xZPpe4pVXDsPCIkBs/edit#gid=1465508786"
    response = requests.get(url_SKU)
    response.status_code # 200 status code means OK!
    SKU_records_data = SKU_sh.get_values() 
    #GETTING DATA FROM SPREADSHEET AS DF
    SKU_records_df = pd.DataFrame.from_dict(SKU_records_data)
    SKU_new_header = SKU_records_df.iloc[0] #grab the first row for the header
    SKU_records_df.columns = SKU_new_header #copy the header row as the df header
    SKU_records_df.drop(index=SKU_records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
        axis=0, 
        inplace=True)
    Index_df=SKU_records_df
    
    # Prcess Input dataframe
    print("Please, enter SKU code")   #   0LF11A027-A11
    Config_SKU= Index_df["Config_SKU"]
    x=input()
    print("Please,enter amount of items:")
    n_sku=int(input())

    Input_df=Index_df.loc[Index_df["Config_SKU"] == x]
    Input_df["Quantity"]=n_sku
    
    a =Input_df["PurchasePrice_bDisc"].to_string(index=False)
    a =float(a.replace(",","."))
    
    Input_df["Sum Price"]=a*n_sku
    Input_df["Total price"]=Input_df["Sum Price"]
 
    import gspread #getting access
    from gspread_dataframe import set_with_dataframe
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    sh= gc.open("Final Project").worksheet("OrderTracker")
    records_data = sh.get_values() 
    # get all the records of the data
    records_data = sh.get_values()  
    #wh_total=1440
    
    
    import pandas as pd
  
 # get all the records of the data
    records_data = sh.get_values() 
    records_df = pd.DataFrame.from_dict(records_data)
    new_header = records_df.iloc[0] #grab the first row for the header
    records_df.columns = new_header #copy the header row as the df header
    records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
     axis=0, 
    inplace=True)
    WH_Capacity=records_df["Warehouse_Capacity"].iloc[0]
    WH_Capacity= float(WH_Capacity.replace(",",".").strip(""))


    
    for i in range(1):
        volume_sneakers = 5.6
            
        future_space =WH_Capacity
        check=future_space
        
        if check -(volume_sneakers*n_sku) < 0:
            balance_after= volume_sneakers*n_sku
            per_sku=round(balance_after/volume_sneakers,2)
            per_sku = int(per_sku) #esta es la cantidad que introduje
            new= WH_Capacity/volume_sneakers #calcula unitdades q faltan apra el max      
            new=str(round(new) )
            check = future_space   
            print("Reached limit of space " + new + " units above limit" ) #bien
            
        elif check -(volume_sneakers*n_sku) >= 0:  #rvisar
            future_space = future_space - (volume_sneakers*n_sku)
            wh_total= future_space
            new= wh_total/volume_sneakers #calcula unitdades q faltan apra el max      
            new=str(round(new) )

            q=(future_space/WH_Capacity)*100
            q1=round(q,2)
        #q2=(WH_Capacity - (future_space/WH_Capacity))
            
            #q2= (future_space/WH_Capacity) to know % left free
           # q2=(1-q2)*100 
        
            q2= (WH_Capacity - future_space)
            q2= WH_Capacity - q2 
        
        
            print("Space available in WH: " +  str(q1) + "%" + " by " + new +" units left.")  
            print("Space left: " + str(round(q2,3)) +" Sqm left")
            
            import gspread #getting access
            gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
            sh= gc.open("Final Project").worksheet("OrderTracker")
            sh.update("AG2",q2) #updating cell with updated space left
            #set_with_dataframe(worksheet, Input_df )    #FUNCTION TO EXPORT ENTIRE DF INTO SPREADSHEET ON TOP OF SPREAD
###aqui     
                        # INVOICE
            
            import os
            from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
            from InvoiceGenerator.pdf import SimpleInvoice 
            import os
            from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
            from InvoiceGenerator.pdf import SimpleInvoice
            import datetime
            current_date = datetime.date.today()
            current_date= str(current_date)
            
            
            
            #Brand name
            Brand_name=Index_df.loc[Index_df["Config_SKU"] == x]
            Brand_name=Brand_name["Brand"]
            Brand_name = Brand_name.values
            # Convert the NumPy array to a list
            Brand_name = Brand_name.tolist()
            Brand_name = Brand_name[0]
            #Supplier name
            Supplier_name=Index_df.loc[Index_df["Config_SKU"] == x]
            Supplier_name=Supplier_name["Main_Supplier"]
            Supplier_name = Supplier_name.values
            # Convert the NumPy array to a list
            Supplier_name = Supplier_name.tolist()
            Supplier_name = Supplier_name[0]
            
            
            # Choose English as the document language
            os.environ["INVOICE_LANG"] = "en"
            # Define the client, provider, and creator
            client = Client(Brand_name)
            provider = Provider(Supplier_name)
            Date= creator = Creator(current_date)
            # Create the invoice
            invoice = Invoice(client, provider, creator)
            # Add the items to the invoice
            SKU = n_sku
            SKU_Price=Index_df.loc[Index_df["Config_SKU"] == x]
            value = SKU_Price[ "PurchasePrice_bDisc"]
            
            
            b =Input_df["EAN"].to_string(index=False) # adding EAN into Invoice
            description= {"SKU": x, "EAN": b}
            description=str(description)
            description = description.replace("}","")
            description= description.replace("{","")
            description= description.replace("'","")
          
            # Convert the dataframe to a NumPy array
            arr = value.values
            # Convert the NumPy array to a list
            lst = arr.tolist()
            lst = lst[0]
            lst = float(lst.replace(",", "."))
            #value
            #milk_description = "COsas"
            #fruits_quantity = 2000000
    #        #fruits_price = 200009
    #        
            invoice.add_item(Item(SKU, lst,description))
            
            
            
            #------ Select data from PO-Invoice---------------------------------
            gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
            PO_sh= gc.open("Final Project").worksheet("PO-Invoice")
            url_PO="https://docs.google.com/spreadsheets/d/1_mFu_NgmarXt6QbXPFGdWh7LV4xZPpe4pVXDsPCIkBs/edit#gid=824586195"
            response = requests.get(url_PO)
            response.status_code # 200 status code means OK!
            PO_records_data = PO_sh.get_values() 
             #GETTING DATA FROM SPREADSHEET AS DF
            PO_records_df = pd.DataFrame.from_dict(PO_records_data)
            PO_new_header = PO_records_df.iloc[0] #grab the first row for the header
            PO_records_df.columns = PO_new_header #copy the header row as the df header
            PO_records_df.drop(index=PO_records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
            axis=0, inplace=True)
            PO_df=PO_records_df  # PO-Invoice List in DF
    
            #---------- Adapt data PO
            new_PO = PO_df.iloc[-1] # to get last row

            new_PO = new_PO.to_string(index=False) # convert to int without PO string part
            new_PO=new_PO.replace("0\nPO-","")
            new_PO=int(new_PO)
            new_PO=new_PO+1
    
            new_PO={"PO-": new_PO}
            
            new_PO=str(new_PO)
            
            
            new_PO=new_PO.replace("{","")
            new_PO=new_PO.replace("}","")
    
            new_PO=new_PO.replace(":","")
            new_PO=new_PO.replace(" ","")
    
            new_PO=new_PO.replace("'","")
            new_PO=new_PO.replace("'","")
            
            
            new_PO_invoice=str(new_PO) # this is only for the invoice, just take tha value of this DF but not theindex info
            
    
            new_PO = {new_PO} # it must be as dictionary
            new_PO = pd.DataFrame.from_dict(new_PO)
            
            new_header_PO = new_PO.iloc[0]
            new_PO.columns = new_header_PO #copy the header row as the df header
            new_PO.drop(index=new_PO.index[0], #remove first row, since now its the header (it was duplicated as row data)
            axis=0, 
            inplace=True)  # the tittle column is posted as well, therefore you copy the first row as tittle and then remove the orginal row, so only the column tittle will be posted.
    
    #new_PO= new_PO.to_json()
            worksheet_PO = gc.open("Final Project").worksheet("PO-Invoice")
            worksheet_PO.append_rows([new_PO.columns.values.tolist()] + new_PO.values.tolist(), value_input_option="USER_ENTERED") #EXPORT TO LAST ROW IN SPREADSHEET
            
    #        # Set the currency and invoice number
            invoice.currency = "Euros"
        
            invoice.number =new_PO_invoice
   #         # Generate the invoice
            docu = SimpleInvoice(invoice)
   #         # Set the column widths
            docu.gen("invoice2.pdf", generate_qr_code=False)
    
    
    #-------------------------------------------
    #export ew final DF (SKU,prices,etc)
            Input_df["PO-Invoice"]=new_PO_invoice
        
        
        
            # shift column 'C' to first position
            first_column = Input_df.pop('PO-Invoice')
  
            # insert column using insert(position,column_name,first_column) function
            Input_df.insert(1, 'PO-Invoice', first_column)
    
            worksheet.append_rows([Input_df.columns.values.tolist()] + Input_df.values.tolist(), value_input_option="USER_ENTERED") #EXPORT TO LAST ROW IN SPREADSHEET
            
    
    
    return Input_df


# In[58]:


One_SKU_Input()  #   


# # Final SKU Input- Several Purchases - Import PC, export G.Spread

# ------------------------------------------------Run before second code--------------------------------------------------------------

# In[59]:


import pandas as pd
#Index_df= pd.read_excel("NewIndex.xlsx") # new
#Index_df= pd.read_excel("Index.xml")


# In[60]:


df=pd.read_excel("NewIndex.xlsx")
Index_df=df
Index_df


# In[61]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
] #standar
credentials = ServiceAccountCredentials.from_json_keyfile_name('mythic-delight-370211-09579ff6aae2.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open("Final Project").worksheet("Input") #sheet name
next_row = next_available_row(worksheet)

creds= ServiceAccountCredentials.from_json_keyfile_name("mythic-delight-370211-09579ff6aae2.json", scope)
client= gspread.authorize(creds)
python_test= client.open("Final Project").worksheet("StockOverview")
time.sleep(1)
#insert on the next available row

#worksheet.update_acell("A{}".format(next_row), "cccc") # what to upload
#worksheet.update_acell("B{}".format(next_row), somevar2)


# In[62]:



def Final_SKU_Local_Input() :
    
    
    import gspread
    from bs4 import BeautifulSoup
    from oauth2client.service_account import ServiceAccountCredentials
    import requests
    import pandas as pd
    import time
    
    
    
    # Prcess Input dataframe
    
    TOTAL_QT=int(input("Please, enter the total number of items in the order, in order to check the WH space: "))
    
    #print("Please, enter SKU code")   #   0LF11A027-A11
    #Config_SKU= Index_df["Config_SKU"]
   # x=input()
    #print("Please,enter amount of items:")
    #n_sku=int(input())

    #Input_df=Index_df.loc[Index_df["Config_SKU"] == x]
   # Input_df["Quantity"]=n_sku
    
    #a =Input_df["PurchasePrice_bDisc"].to_string(index=False)
    #a =float(a.replace(",","."))
    
    #Input_df["Total price"]=a*n_sku
    
 
    import gspread #getting access
    from gspread_dataframe import set_with_dataframe
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    sh= gc.open("Final Project").worksheet("OrderTracker")
    records_data = sh.get_values() 
    # get all the records of the data
    records_data = sh.get_values()  
    #wh_total=1440
    
    
    import pandas as pd
  
 # get all the records of the data
    records_data = sh.get_values() 
    records_df = pd.DataFrame.from_dict(records_data)
    new_header = records_df.iloc[0] #grab the first row for the header
    records_df.columns = new_header #copy the header row as the df header
    records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
     axis=0, 
    inplace=True)
    WH_Capacity=records_df["Warehouse_Capacity"].iloc[0]
    WH_Capacity= float(WH_Capacity.replace(",",".").strip(""))


    
    
    volume_sneakers = 5.6
            
    future_space =WH_Capacity
    check=future_space
        
    if check -(volume_sneakers*TOTAL_QT) < 0:
        balance_after= volume_sneakers*TOTAL_QT
        per_sku=round(balance_after/volume_sneakers,2)
        per_sku = int(per_sku) #esta es la cantidad que introduje
        new= WH_Capacity/volume_sneakers #calcula unitdades q faltan apra el max      
        new=str(round(new) )
        check = future_space   
        print("Reached limit of space " + new + " units above limit" ) #bien
            
    elif check -(volume_sneakers*TOTAL_QT) >= 0:  #rvisar
        future_space = future_space - (volume_sneakers*TOTAL_QT)
        wh_total= future_space
        new= wh_total/volume_sneakers #calcula unitdades q faltan apra el max      
        new=str(round(new) )

        q=(future_space/WH_Capacity)*100
        q1=round(q,2)
        #q2=(WH_Capacity - (future_space/WH_Capacity))
            
            #q2= (future_space/WH_Capacity) to know % left free
           # q2=(1-q2)*100 
        
        q2= (WH_Capacity - future_space)
        q2= WH_Capacity - q2 
        
        
        print("Space available in WH: " +  str(q1) + "%" + " by " + new +" units left.")  
        print("Space left: " + str(round(q2,3)) +" Sqm left")
            
        import gspread #getting access
        gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
        sh= gc.open("Final Project").worksheet("OrderTracker")
        sh.update("AG2",q2) #updating cell with updated space left
        
        df=()
        
        while True:
            # Ask the user to input a number
            df = pd.DataFrame(df)
            x=input("Enter SKU: ")
            n_sku = int(input("Enter a number: "))
            
            # Try to convert the input to a float
            
            try:
                #num = int(num)
                # If the conversion was successful, add the number to the DataFrame
                df = df.append({'Config_SKU': x, "Quantity":n_sku}, ignore_index=True)
                #df = df.append({'number': num}, ignore_index=True)
                # Ask the user if they want to add another number
                add_more = input("Do you want to add another SKU? yes/no ")
                # If the user doesn't want to add more numbers, break out of the inner loop
                if add_more == "no":
                    break
                    
            except ValueError:
                # If the input could not be converted to a float, print an error message
                print("Invalid input. Please enter a number.")
        
              
#it works
    merged_Test= Index_df
    df_merged = pd.merge(merged_Test, df, on='Config_SKU')
    df_merged["Sum Price"]=df_merged["PurchasePrice_bDisc"]*df_merged["Quantity"]
    
    #------ Select data from PO-Invoice---------------------------------
    gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
    PO_sh= gc.open("Final Project").worksheet("PO-Invoice")
    url_PO="https://docs.google.com/spreadsheets/d/1_mFu_NgmarXt6QbXPFGdWh7LV4xZPpe4pVXDsPCIkBs/edit#gid=824586195"
    response = requests.get(url_PO)
    response.status_code # 200 status code means OK!
    PO_records_data = PO_sh.get_values() 
     #GETTING DATA FROM SPREADSHEET AS DF
    PO_records_df = pd.DataFrame.from_dict(PO_records_data)
    PO_new_header = PO_records_df.iloc[0] #grab the first row for the header
    PO_records_df.columns = PO_new_header #copy the header row as the df header
    PO_records_df.drop(index=PO_records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
    axis=0, inplace=True)
    PO_df=PO_records_df  # PO-Invoice List in DF
    
            #---------- Adapt data PO
    new_PO = PO_df.iloc[-1] # to get last row

    new_PO = new_PO.to_string(index=False) # convert to int without PO string part
    new_PO=new_PO.replace("0\nPO-","")
    new_PO=int(new_PO)
    new_PO=new_PO+1
    
    new_PO={"PO-": new_PO}
            
    new_PO=str(new_PO)
            
            
    new_PO=new_PO.replace("{","")
    new_PO=new_PO.replace("}","")
    
    new_PO=new_PO.replace(":","")
    new_PO=new_PO.replace(" ","")
    
    new_PO=new_PO.replace("'","")
    new_PO=new_PO.replace("'","")
            
            
    new_PO_invoice=str(new_PO) # this is only for the invoice, just take tha value of this DF but not theindex info
            
    
    new_PO = {new_PO} # it must be as dictionary
    new_PO = pd.DataFrame.from_dict(new_PO)
            
    new_header_PO = new_PO.iloc[0]
    new_PO.columns = new_header_PO #copy the header row as the df header
    new_PO.drop(index=new_PO.index[0], #remove first row, since now its the header (it was duplicated as row data)
    axis=0, 
    inplace=True)  # the tittle column is posted as well, therefore you copy the first row as tittle and then remove the orginal row, so only the column tittle will be posted.
    
    #new_PO= new_PO.to_json()
    worksheet_PO = gc.open("Final Project").worksheet("PO-Invoice")
    worksheet_PO.append_rows([new_PO.columns.values.tolist()] + new_PO.values.tolist(), value_input_option="USER_ENTERED") #EXPORT TO LAST ROW IN SPREADSHEET
            

    
    #-------------------------------------------
    #export ew final DF (SKU,prices,etc)
    df_merged["PO-Invoice"]=new_PO_invoice
        
        
        
            # shift column 'C' to first position
    first_column = df_merged.pop('PO-Invoice')
  
            # insert column using insert(position,column_name,first_column) function
    df_merged.insert(1, 'PO-Invoice', first_column)
    
    
    
    
    
    
    df_merged["Total Price"] = round(df_merged["Sum Price"].sum(),2)
    #df_merged['Price Sum'].iloc[0] = df_merged['Data'].iloc[-1]
    df_merged['Total Price'].iloc[:-1] = '-'
    
    worksheet.append_rows([df_merged.columns.values.tolist()] + df_merged.values.tolist(), value_input_option="USER_ENTERED") #EXPORT TO LAST ROW IN SPREADSHEET
    
    #------------------------------------------------------INVOICE------------------------------------------------


      # Import the necessary libraries                                                
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    
    #cREATING BANK TABLE INFO
    
    Payment_df= pd.DataFrame([['Visa 123456', '123456'], ['Mastercard 456789', '456789'], ['Discover 901234', '901234']],
                  columns=['Payment information', 'Account number'])
    
    Payment_df = pd.DataFrame.from_dict(Payment_df)
    

# Create the figure and axes objects
    fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(20,7))

# Turn off the axis lines and labels for both axes
    ax1.axis('tight')
    ax1.axis('off')
    ax2.axis('tight')
    ax2.axis('off')

# Create a table using the data in the first DataFrame
    the_table1 = ax1.table(cellText=df_merged.values,colLabels=df_merged.columns,loc='center')

# Create a table using the data in the second DataFrame
    the_table2 = ax2.table(cellText=Payment_df.values,colLabels=Payment_df.columns,loc='center')

# Create a table using the data in the second DataFrame
    #the_table3 = ax2.table(cellText=df_merged.values,colLabels=df_merged.columns,loc='center')

# Set the title for the axes

    df_merged["PO-Invoice"]
    ö= df_merged['PO-Invoice'].unique()
    ö=str(ö)    
    #ö = ö.replace("\nName: PO-Invoice, dtype: object","")
    #ö= ö.replace("0    "," PO-Invoice code: ")

    ö = ö.replace("[","PO-Invoice: ")
    ö = ö.replace("]","")
    ö = ö.replace("''","")
    
    #ö= ö.replace("0    "," PO-Invoice code: ")
    
    
    
    
    
    Tittle =str(ö)
    ax1.set_title(Tittle, fontsize=20)

# Save the figure to a PDF file
    pp = PdfPages("foo.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    


    return df_merged
#   0LF11A027-A11     ALJ11A02U-B11               ALJ11A02S-Q11


# In[64]:


Final_SKU_Local_Input()


# In[ ]:





# # INVOICES 

# In[116]:


import reportlab


# In[123]:


import os

# other code here

# Print the current working directory
print(os.getcwd())   #FIND INVOICE'


# -- ONE INVOICE TYPE

# In[125]:


# create a product and price for three items
product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 598.99
product3_name, product3_price = 'Monitor', 156.89

# create a company name and information
company_name = 'Thecleverprogrammer, inc.'
company_address = '144 Kalka ji.'
company_city = 'New Delhi'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)


# In[ ]:





# -- INVOICE FOR ONE PURCHASE---
# 

# In[168]:


import os

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice

# choosing English as the document language

os.environ["INVOICE_LANG"] = "en"

client = Client('Client company')

provider = Provider('SUPPLIER', bank_account='6454-6361-217273', bank_code='2021')

creator = Creator('Karl Iris')

invoice = Invoice(client, provider, creator)

invoice.add_item(Item(26, 780, description="Milk"))

invoice.add_item(Item(14, 460, description="Fruits"))

invoice.add_item(Item(10, 290, description="Nuts"))

invoice.add_item(Item(3, 165, description="Biscuits"))

invoice.currency = "Rs."

invoice.number = "10393069"

docu = SimpleInvoice(invoice)

docu.gen("invoice2.pdf", generate_qr_code=False) #you can put QR code by setting the #qr_code parameter to ‘True’

#docu.gen("invoice.xml") ## We can also generate an XML file of this invoice


# ------------------------------------------------------INVOICE-------------------------------------------------------------

# In[ ]:


#------------------------------------------------------INVOICE------------------------------------------------


# Import the necessary libraries                                                
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Create the figure and axes objects
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(20,7))

# Turn off the axis lines and labels for both axes
ax1.axis('tight')
ax1.axis('off')
ax2.axis('tight')
ax2.axis('off')

# Create a table using the data in the first DataFrame
the_table1 = ax1.table(cellText=df_merged.values,colLabels=df_merged.columns,loc='center')

# Create a table using the data in the second DataFrame
the_table2 = ax2.table(cellText=df_merged.values,colLabels=df_merged.columns,loc='center')

# Create a table using the data in the second DataFrame
the_table3 = ax2.table(cellText=df_merged.values,colLabels=df_merged.columns,loc='center')

# Set the title for the axes
Tittle =str(df_merged['PO-Invoice'].iloc[:-1])
ax1.set_title(Tittle, fontsize=20)

# Save the figure to a PDF file
pp = PdfPages("foo.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()


# In[ ]:





# ----  ONE TYPE OF INVOICE

# In[167]:


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a new PDF document with a letter-sized page
c = canvas.Canvas("invoice.pdf", pagesize=letter)

# Define some standard font sizes and styles
LARGE_FONT = 16
SMALL_FONT = 12
BOLD_FONT = "Helvetica-Bold"
NORMAL_FONT = "Helvetica"

# Draw the invoice header
c.setFont(BOLD_FONT, LARGE_FONT)
c.drawString(100, 750, "Invoice")

# Draw the invoice details (date, invoice number, etc.)
c.setFont(NORMAL_FONT, SMALL_FONT)
c.drawString(100, 720, "Date: 12/09/2022")
c.drawString(100, 700, "Invoice number: 123456")

# Draw the table with the invoice items
c.rect(50, 600, 500, 100)  # Draw the table outline
c.line(100, 650, 550, 650)  # Draw a line to separate the header row from the rest of the table

# Draw the table header row
c.setFont(BOLD_FONT, SMALL_FONT)
c.drawString(100, 670, "Item")
c.drawString(300, 670, "Quantity")
c.drawString(400, 670, "Price")

# Draw some sample invoice items
c.setFont(NORMAL_FONT, SMALL_FONT)
c.drawString(100, 630, "Widget")
c.drawString(300, 630, "10")
c.drawString(400, 630, "$5.00")
c.drawString(100, 610, "Thingamajig")
c.drawString(300, 610, "5")
c.drawString(400, 610, "$10.00")

# Draw the total amount due
c.setFont(BOLD_FONT, SMALL_FONT)
c.drawString(100, 570, "Total:")
c.drawString(400, 570, "$75.00")

# Save the PDF to disk
c.save()


# In[ ]:





# # grab data from Sheet and export it to MySQL -  Final Project

# In[37]:


import gspread
import pandas as pd
gc= gspread.service_account(filename = "mythic-delight-370211-09579ff6aae2.json")
sh= gc.open("Final Project").worksheet("OrderTracker")

# get all the records of the data
records_data = sh.get_values() 

records_df = pd.DataFrame.from_dict(records_data)
new_header = records_df.iloc[0] #grab the first row for the header

records_df.columns = new_header #copy the header row as the df header

records_df.drop(index=records_df.index[0], #remove first row, since now its the header (it was duplicated as row data)
        axis=0, 
        inplace=True)

#Or you can try to access the database when making the connection:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lupitabonita1010",
  database="mydatabase"
) #If the database does not exist, you will get an error.

import pandas as pd # FROM API SHEET

url1="https://docs.google.com/spreadsheets/d/e/2PACX-1vR53_WotSs9zjU3cF-pasH3CPJnzU76ugbiSoGttv5BQp6lZt3TtIehyF7HD9E-J7NH7C261w981pga/pub?output=csv"
df_DESDEWEB = pd.read_csv(url1)

# import the module
from sqlalchemy import create_engine
import pymysql
# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Lupitabonita1010",
                               db="mydatabase"))

#drop
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lupitabonita1010",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE mydatabase"

mycursor.execute(sql)

#create table
df_DESDEWEB.to_sql('mydatabase', con = engine, if_exists = 'append', chunksize = 1000) # inserted in MySQL


# In[ ]:





# In[ ]:




