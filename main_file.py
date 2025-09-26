import requests # for http request
from bs4 import BeautifulSoup as bs # for web scraping
import smtplib # for sending email

#Load the webpage content
r = requests.get("https://thehackernews.com/")

#Convert to a beautiful soup object
soup = bs(r.content, features="html.parser")

#Print out our html and adding the prettify makes it nice and readable
# print(soup.prettify())

##how to find only one item in the soup object using the find keyword
# first_blog = soup.find("h2")
# print(first_blog)

## finding multiple items in the soup object using find_all
# all_blogs = soup.find_all("h2")
# print(all_blogs)

##how to find only one first item in the soup object using the list [] and find
# blog = soup.find(['h1', 'h2'])
# print(blog)

## finding multiple items in the soup object using find_all and []
# blog = soup.find_all(['h1', 'h2'])
# print(blog)

# headings = soup.find_all("h2", attrs={"class": "home-title"})
# print(headings)

body = soup.find("body")
div = body.find("div")
# print(div)

##searching specific stings in our find/find_all calls
import re
head = soup.find_all("h2", string=re.compile("Hackers"))
# print(head)

#Using the select
soup_select = soup.select("p")

#Using the find method to get only the strings without the keyword by using string
ss = soup.find('p')
# print(ss.string)


#Using the find method to get all the strings without the keyword by using get_text()
ssa = soup.find('div')
print(ssa.get_text())