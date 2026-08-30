"""urllib.request
urllib.parse
urllib.error
urllib.robotparser

"""

from urllib.parse import urlparse

url = "https://www.example.com/products?id=10"

result = urlparse(url)
#print(result)


#----------------Access Individual parts------------------------------
print("Scheme:", result.scheme)#--------http/https/ftp--------------------
print("Domain:", result.netloc)#------------------network Location-------------
print("Path:", result.path)
print("Query:", result.query)
















#-------------------------It converts query parameters into a Python dictionary-like structure.

from urllib.parse import urlparse, parse_qs

url = "https://example.com/search?name=python&level=beginner"

result = urlparse(url)

data = parse_qs(result.query)

print(data)







#----------------------Build A URL-----------------------------------
from urllib.parse import urlunparse

url = urlunparse((
    "https",
    "example.com",
    "/products",
    "",
    "id=10",
    ""
))

print(url)



















#---------------------------------urlencode()-------------------------------------
data = {
    "name": "python",
    "level": "beginner"
}
from urllib.parse import urlencode

query = urlencode(data)

print(query)

url = "https://example.com/search?" + query

print(url)














#-------------------------URL Request---------------------
import urllib.request

response = urllib.request.urlopen("https://example.com")

print(response.status)
"""200 → Success
301 → Redirect
404 → Not Found
403 → Forbidden
500 → Server Error
    """








































#----------------------------------Real life use -----------------------------------------
import urllib.request

url = "https://example.com"

response = urllib.request.urlopen(url)

print("Status:", response.status)

data = response.read()

text = data.decode("utf-8")

print(text)


















#-----------------------------------------Handle errors-----------------------------------
import urllib.request

response = urllib.request.urlopen(
    "https://example.com",
    timeout=5
)


























#---------------------------------Handle Error----------------------------------------
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen(
        "https://example.com",
        timeout=5
    )

    print("Status:", response.status)

except urllib.error.URLError as e:
    print("URL error:", e)
 
 
 
 
 
 
 
 
 
 
 
 
 
 







#---------------------------------------Handle Error--------------------------------------------   
    
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen(
        "https://example.com",
        timeout=5
    )

    print("Status:", response.status)

except urllib.error.URLError as e:
    print("URL error:", e)
    



"""
1. Parse URL
from urllib.parse import urlparse
result = urlparse(url)





2. Get domain
result.hostname



3. Get query
result.query



4. Parse query
from urllib.parse import parse_qs
parse_qs(result.query)



5. Make request
import urllib.request
response = urllib.request.urlopen(url)





6. Get status
response.status





7. Read content
data = response.read()







8. Decode it
text = data.decode("utf-8")
"""

























