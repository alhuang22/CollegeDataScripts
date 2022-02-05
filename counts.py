import json

with open('data.json') as j:
    data = json.load(j)

with open('translated.json') as j:
    d = json.load(j)


cnt = 0
for college in d:
    if cnt == 444:
        print(college['college_name'])
    cnt += 1