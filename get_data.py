# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
raw_data = json.loads(response.text)
print(raw_data['name'])

request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url2)
my_list = json.loads(response2.text)

for p in my_list:
    print(p["id"]," ",p["name"])


#From Alanna
request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
grades = requests.get(request_url3)
listgrades = json.loads(grades.text)
students = listgrades["students"]
#print("students",students)
grades = []
for i in students:
    i["finalGrade"] = float(i["finalGrade"])
    grades.append(i["finalGrade"])
avg = statistics.mean(grades)
mingrades = min(grades)
maxgrades = max(grades)
#print(grades)
print("average", avg)
print("minimum",mingrades)
print("maximum", maxgrades)