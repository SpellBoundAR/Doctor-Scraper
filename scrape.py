# importing the requests library 
import requests 
  
# import webbrowser
# print(webbrowser.get('https://health.usnews.com/best-hospitals/search-data?type=pediatric&page=2'))

import urllib
googleContent = urllib.urlopen('https://health.usnews.com/best-hospitals/search-data?type=pediatric&page=2').read()

# # api-endpoint 
# URL = "https://health.usnews.com/best-hospitals/search-data?type=pediatric&page=2"
  
# PARAMS = {} 

# print("sending request")
# r = requests.get(URL) 

# print(r)

# # extracting data in json format 
# data = r.json() 

# print(data)
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address'] 