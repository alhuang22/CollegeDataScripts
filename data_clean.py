import json
# from jsonIterator import c
import urllib.request
from colorthief import ColorThief
import traceback

with open('colleges.json') as j:
    data = json.load(j)

n = []
for college in data:
    try:
        print(college['college_name'])
        link = 'http://logo.clearbit.com/' + college['domain']
        urllib.request.urlretrieve(link, 'college')
        color_thief = ColorThief('college')
        dom = color_thief.get_color(quality=10)
    except Exception:
        college['red'] = None
        college['green'] = None
        college['blue'] = None
        n.append(college)
        with open("skipped.txt", "a") as myfile:
            myfile.write(college['college_name'] + '\n')
    else:
        college['red'] = dom[0]
        college['green'] = dom[1]
        college['blue'] = dom[2]
        n.append(college)


    

with open('addColors2.json', 'w', encoding='utf-8') as f:
        json.dump(n, f, ensure_ascii=False, indent=4) 