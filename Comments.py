import requests
import openpyxl
from bs4 import BeautifulSoup


#enter the url here
# url1_indi = "https://www.flipkart.com/dinine-craft-wooden-2-pocket-key-holder-wall-home-decor-decorative-showpiece-6-cm/product-reviews/itmb6135a09b4d7d?pid=SHIGG8J7VQ7BHUYK&lid=LSTSHIGG8J7VQ7BHUYKODYETT&marketplace=FLIPKART"
url1_indi = input("Enter Comments URL Here: ")
page_01 = requests.get(url1_indi)
doc_01 = page_01.text
soup_01 = BeautifulSoup(doc_01,'html.parser')

string = "https://www.flipkart.com"
pages = soup_01.find_all(["a"],class_="ge-49M")

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Page 1'

insert = []

for i in pages:
    url = string+i['href']
    # print(url)
    page = requests.get(url)
    doc = page.text
    soup = BeautifulSoup(doc,'html.parser')

    for temp in (soup.find_all("div",{ "class" : "col _2wzgFH K0kLPL"})) :
        rating = temp.find("div",{ "class" : "_3LWZlK _1BLPMq"}) #rating
        heading = temp.find("p",{ "class" : "_2-N8zT"}).get_text() #Heading 
        comments = temp.find("div",{"class" : "t-ZTKy"}).get_text() #Comments
        comments = comments.removesuffix('READ MORE')
        update = ""
        if rating == None:
            bad_rating = temp.find("div",{ "class" : "_3LWZlK _1rdVr6 _1BLPMq"})
            if bad_rating == None:
                bad_rating = "NULL"
            else:
                bad_rating = bad_rating.get_text()


            update = update + (bad_rating) +"-"
        else:
            update = update + (rating.get_text()) +"-"
        
        update = update + (heading) +"-"
        update = update + (comments)
        insert.append(update)



sheet.append(insert)

sheet_name = input("Enter the excel sheet file name(No Spaces): ")
excel.save(sheet_name+".xlsx") #change the excel sheet name

