import json
import urllib.request
#url = input("Tell me the link: ")
url ='http://py4e-data.dr-chuck.net/comments_1378490.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)
print('User count:', len(info))
print(type(info))
print(info)
print(info["note"])
counter = 0
for item in info["comments"]:
    print('Name', item['name'])
    print('Count', item['count'])
    counter = counter + int(item['count'])
print("The sum is:",counter)
