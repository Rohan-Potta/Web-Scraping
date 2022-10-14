import requests
import openpyxl
from bs4 import BeautifulSoup



excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Second Item'

url=""
page = requests.get(url)
doc = page.text
soup = BeautifulSoup(doc,'html.parser')



title = soup.find(["span"],class_="B_NuCI").get_text()
over_all_rating = soup.find(["div"],class_="_3LWZlK").get_text()
# print(title)
# print(over_all_rating)

number_reviews = soup.find(["div"],class_="col-12-12").get_text()
print(number_reviews)
# number_reviews = number_reviews.split() #gives a list as ['851', 'Ratings', '&', '100', 'Reviews']
# print(number_reviews[3])

# #new_url = "https://www.flipkart.com/ecraftindia-man-sitting-thinking-position-handcrafted-decorative-showpiece-27-cm/product-reviews/itmcaa0247cf83e9?pid=SHIG2CKHMVFJQ2DG&lid=LSTSHIG2CKHMVFJQ2DGSPPS6Q&marketplace=FLIPKART"
new_url = url.replace("/p/", "/product-reviews/" ) #to shift to the reviews page
# # print(url)
# # print(new_url)

page1 = requests.get(new_url) 
doc1 = page1.text  
soup1 = BeautifulSoup(doc1,'html.parser')  

temp=soup1.find_all("div",{ "class" : "col _2wzgFH K0kLPL"})


# #NEEED TO FIX THE RATING ONEEEEEEEEEEE  #remove get_text ,if none ignore
# # print(temp[5].find("div",{ "class" : "_3LWZlK _1rdVr6 _1BLPMq"})) #bad rating
# # print(temp[4].find("div",{ "class" : "_3LWZlK _1BLPMq"})) #good rating

# # if value == None:
# #     value = (temp.find("div",{ "class" : "_3LWZlK _1rdVr6 _1BLPMq"}))
# #     print(value.get_text())
# # else:
# #     print (value.get_text())


# insert=[url, title, over_all_rating, number_reviews[3]]
# print(insert)
# # print(number_reviews)
# # number_reviews.pop()
# # number_reviews.pop()
# # print(number_reviews)

# for temp in (soup1.find_all("div",{ "class" : "col _2wzgFH K0kLPL"})) :
#     rating = temp.find("div",{ "class" : "_3LWZlK _1BLPMq"}) #rating
#     heading = temp.find("p",{ "class" : "_2-N8zT"}).get_text() #Heading 
#     comments = temp.find("div",{"class" : "t-ZTKy"}).get_text() #Comments
#     comments = comments.removesuffix('READ MORE')
    
#     update = ""
#     if rating == None:
#         bad_rating = temp.find("div",{ "class" : "_3LWZlK _1rdVr6 _1BLPMq"})
#         # print(bad_rating.get_text())
#         update = update + (bad_rating.get_text()) +"-"
#     else:
#         # print(rating.get_text())  
#         update = update + (rating.get_text()) +"-"
#         # update.append(rating.get_text()) 
    
#     update = update + (heading) +"-"
#     update = update + (comments)
#     # print(heading)
#     # print(comments)
#     insert.append(update)
#     # print("-------------------------------------------------------------------------------------")


# # print(insert)
# # sheet.append(insert)

# # excel.save("Handicraft.xlsx")