import os
import requests
from PIL import Image
from IPython.display import IFrame

# HTTP GET requests

# You can make a GET request via the method get to www.ibm.com:
url = "https://www.ibm.com/"

# We have the response object r, this has information about the request, like the status of the request.
r = requests.get(url)
print(r)

# We can view the status code using the attribute status_code.
print(r.status_code)
print(r.request.url)

# You can view the request headers:
print(r.request.headers)

# You can view the request body, in the following line, as there is no body for a get request we get a None
print("request body:", r.request.body)

# You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header = r.headers
print(header)

# We can obtain the date the request was sent using the key Date
print(header['Date'])

#  Content-Type indicates the type of data:
print(header['Content-Type'])

# You can also check the encoding:
print(r.encoding)

#  As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
print(r.text[0:100])
# print(r.text)

# You can load other types of data for non-text requests, like images.

url_1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r_img = requests.get(url_1)
print(r_img.status_code)
print(r_img.headers)
print(r_img.headers['Content-Type'])

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
print(path)

# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r_img.content)
# print(r_img.content)

# We can view the image:
img=Image.open(path)   
img.show()

"""
What You Learned:
requests.get(url) downloads data (image here).

r_img.content gives the image in bytes.

with open(..., 'wb') saves it as a file.

PIL.Image.open() opens the image.

.show() displays it.
"""