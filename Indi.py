import requests
import openpyxl
from bs4 import BeautifulSoup



excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'First Item'

#change the url here for each item
url = "https://www.flipkart.com/ecraftindia-man-sitting-thinking-position-handcrafted-decorative-showpiece-27-cm/p/itmcaa0247cf83e9?pid=SHIG2CKHMVFJQ2DG&fm=organic&ppt=pp&ppn=pp&ssid=re9t1qq2g00000001664291810971"
page = requests.get(url)
doc = page.text
soup = BeautifulSoup(doc,'html.parser')



title = soup.find(["span"],class_="B_NuCI").get_text()
over_all_rating = soup.find(["div"],class_="_3LWZlK").get_text()

number_reviews = soup.find(["span"],class_="_2_R_DZ").get_text()
number_reviews = number_reviews.split() #gives a list as ['851', 'Ratings', '&', '100', 'Reviews']
# print(number_reviews[3])

new_url = url.replace("/p/", "/product-reviews/" ) #to shift to the reviews page


page1 = requests.get(new_url) 
doc1 = page1.text  
soup1 = BeautifulSoup(doc1,'html.parser')  

temp=soup1.find_all("div",{ "class" : "col _2wzgFH K0kLPL"})



insert=[url, title, over_all_rating, int(number_reviews[3])]

for temp in (soup1.find_all("div",{ "class" : "col _2wzgFH K0kLPL"})) :
    rating = temp.find("div",{ "class" : "_3LWZlK _1BLPMq"}) #rating
    heading = temp.find("p",{ "class" : "_2-N8zT"}).get_text() #Heading 
    comments = temp.find("div",{"class" : "t-ZTKy"}).get_text() #Comments
    comments = comments.removesuffix('READ MORE')
    
    update = ""
    if rating == None:
        bad_rating = temp.find("div",{ "class" : "_3LWZlK _1rdVr6 _1BLPMq"})
        update = update + (bad_rating.get_text()) +"-"
    else:
        update = update + (rating.get_text()) +"-"
    
    update = update + (heading) +"-"
    update = update + (comments)
    insert.append(update)

sheet.append(insert)

excel.save("Handicraft.xlsx") #change the excel sheet name