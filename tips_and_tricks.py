#Here I use several libraries, so to understand and to use them at full power access the main sources

#This make things prettier and easier to use
import pprint
pp = pprint.PrettyPrinter()
pp.pprint(your_dict)

#The codes below use the Pandas library
import pandas as pd
#Python statements like "or" and "and" require truth-values, these are ambiguous in pandas so use "|" for "or" and "&" for "and".

#With this one you create a new column with only the year and month ('YYYY-MM') of the date of the previous column, you can use it to group all information about a month or something like that, the previous column needs to be datetime type, you can use "pd.to_datetime(custumers_table['created_at'])" to change the type. In this example I use 'YYYY-MM', but you can also get iferent formats by changing the 'M' in the code.
custumers_table['created_year_month'] = custumers_table['created_at'].dt.to_period('M')

#Usually when you group a column it get a weird format, so, you can use 'reset index' to return to the regular format
#Also, when you use the groupby function, it returns nothing if one of the values is empty(like NaT or NaN)
data_table2 = data_table.groupby(['id']).sum().reset_index()

#This is kind of dumb, but take a while to me to figure out, 'copy_of_real = real' don't create a copy of your Dataframe, so you have to use the code below.
copy_of_real = real.copy()

#Upload in a PostgreSQL database
import psycopg2
conn = psycopg2.connect(
    database="__________",
    user="__________",
    password="__________",
    host="________",
    port='____'
)
#If you want to read you can use:
conn = conn.cursor()
conn.execute(query)
data_table = pd.DataFrame(conn.fetchall())
colnames = [desc_school_e[0] for desc_school_e in conn.description]
data_table.columns = colnames
conn.close()
#If you want to write you can use:
cur = conn.cursor()
cur.execute(query)
conn.commit()
cur.close()
conn.close()
#If you want to write from some tuples with your data you can use:
cur = conn.cursor()
cur.executemany(query,tuples)
conn.commit()
cur.close()
#To make a Dataframe into Tuples:
subset = df[['column1','column2','column3']]
tuples = [tuple(x) for x in subset.values]

#The code below use the Numpy library, the result is based in the selected conditions
conditions = [
              (table['amount_charged'] > 200000),
              (table['amount_charged'] >= 100000) & (table['amount_charged'] <= 200000),
              (table['amount_charged'] >= 50000) & (table['amount_charged'] < 100000),
              (table['amount_charged'] < 50000)]
choices = ['above 2k','between 1k and 2k','between 500 and 1000','below 500']
table['Group'] = np.select(conditions,choices,default='null')

#Here I show some examples of some Pipedrive library that I use sometimes
from pipedrive.client import Client
#Here you can get data from your filters, probably you will need to paginate because this get only 100 deals so use the start to decide where you want to begin
filtered_deals = client.get_deals(filter_id = id_number, start = pagination)

#Here I show some examples of the Close.io api
from closeio_api import Client
api = Client('api_key')
data_lead = api.get('lead', params={'query': 'your query(you can test it at close io) or you can call a smartview'})
data_opportunity = api.get('opportunity', params={'lead_query': 'your query(you can test it at close io) or you can call a smartview'})

#Crawler
#Remember to use a webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#You can use it to several things in several ways I'll just leave a simple example here
#Here I access a page with my loggin and password and get some information by the xpath element
#Remember to put some delay between actions that will load the page
driver = webdriver.Chrome()
driver.get('https://your_page')
driver.minimize_window()
time.sleep(10)
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("user")
password.send_keys("pass")
driver.find_element_by_id("loginBtn").click()
time.sleep(5)
driver.minimize_window()
driver.refresh()
time.sleep(10)
elem = driver.find_element_by_xpath('x_path')

#If you use Google Spreadsheets this may help you, but you will have to make an ServiceAccountCredential from Google API
import gspread
from oauth2client.service_account import ServiceAccountCredentials
G_key = {
 "You could paste here the code in your client_secret.json file, otherwise you will need to leave it in the same folder than your python file. Also remember to give edit access to the e-mail in the client_secret.json file."
}
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials._from_parsed_json_keyfile(G_key, scope)
client = gspread.authorize(creds)
sheet = client.open('your sheet name')
worksheet = sheet.worksheet("your worksheet name")
#with this you can get from the worksheet:
value = worksheet.cell(row,col).value
#with this you write in your worksheet:
worksheet.update_cell(row,col,value)
#If you use dataframes, you can use:
import gspread_dataframe as gd
G_key = {
 "You could paste here the code in your client_secret.json file, otherwise you will need to leave it in the same folder than your python file. Also remember to give edit access to the e-mail in the client_secret.json file."
}
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials._from_parsed_json_keyfile(G_key, scope)
gc = gspread.authorize(creds)
ws = gc.open("sheet name").worksheet("worksheet name")
#with this you can get from the worksheet:
data_get = gd.get_as_dataframe(ws)
#with this you write in your worksheet:
gd.set_with_dataframe(ws, data)

#Correlation heatmap
import seaborn as sns
sns.heatmap(z.corr(), annot=True, fmt=".2f");

#DataFrame general info
df.info()

#this link it's a guide to generate the requirements https://qxf2.com/blog/auto-generate-requirements-txt-file-using-pipreqs/

#To get holidays use this awesome librarie(https://pypi.org/project/holidays/)
import holidays
#And here a example
for date, name in sorted(holidays.US(state='CA', years=2014).items()):
    print(date, name)

#To create packages and upload at PyPI
#at the comand promp type:"cd 'PATH_OF_THE_FILES'"
#"python setup.py sdist"
#"twine upload dist/*" If you have some problems with twine, try to locate the twine.exe file in your computer and add this path
#insert your username and password
#DONE!
#To upload a newer version, follow the same proceeds, but instead of "twine upload dist/*" use "twine upload --skip-existing dist/*"
#Also remember that if you, for some reason, delete some version in the PyPI page, you should also delete the same version in your 'PATH/dist' folder, otherwise, you will have some problems to upload new versions.

#While using Google Colab, there are some limits in sizes, so using this, for example, you can see this dataframe completely
pd.set_option('display.max_rows', df.shape[0]+1)

#To upload files (in this example a .csv and generating a DataFrame) into Google Colab, you can use
import csv
import pandas as pd
from google.colab import files

uploaded = files.upload()
df = pd.read_csv('file_name.csv',delimiter=',')

#To download files (in this example a .csv and generating a DataFrame) into Google Colab, you can use
df.to_csv("archive.csv", sep=",", index=False) #Here you can change the separator(sep) and if you want to import the row number value(index=True)
files.download("archive.csv")  
