import requests
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=handicraft&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1" 

page = requests.get(url) #this gets all the data from the url
doc = page.content  #doc stores all the content of the page
soup = BeautifulSoup(doc,'html.parser')  # soup now has all the html code of the file

got_links=[] #a list to store all the links


string = "www.flipkart.com" #the links we get only store after the flipkart.com so need this as to call the link

links = soup.find_all(["a"],class_="s1Q9rs")  #this goes to the class and finds all the 'a' tags
for i in links:
    got_links.append(string+i['href'])  
    # print(i['href']) #this will print all the data in the respective class

for i in got_links:
    print(i)




