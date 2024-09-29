from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page=requests.get(url)
# print(page.text)

soup=BeautifulSoup(page.text,'html')
table=soup.find('table',class_ = "wikitable sortable")
# print(table)

word_title=table.find_all('th')
word_table_title= [title.text.strip() for title in word_title]
# print(word_table_title)
#for column print
df = pd.DataFrame(columns=word_table_title)
print(df)
#for data print
column_data=table.find_all('tr')
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_data=[data.text.rstrip() for data in row_data]

    lenght=len(df)
    df.loc[lenght]=individual_data
print(df.to_string())
df.to_csv(r'C:\Users\venka\OneDrive\Desktop\alex_project.csv',index=False)
