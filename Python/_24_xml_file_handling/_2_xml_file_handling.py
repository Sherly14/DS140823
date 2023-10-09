# pip install bs4

from bs4 import BeautifulSoup

file = open(r"C:\Users\vashi\OneDrive\Documents\GitHub\DS140823\_24_xml_file_handling\demo.xml")

soup = BeautifulSoup(file,'html.parser')

# it will convert your soup object into list
data = soup.find_all("students")
# print(data)

name_data = soup.find("name")
print(name_data)
print(name_data.text)

name_data1 = soup.find("name",{"name":"three"})
print(name_data1.text)