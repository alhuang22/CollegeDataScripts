from simplifyJson import earnings
from googletrans import Translator, constants
import json
import traceback

translator = Translator()

with open('translated.json') as j:
    data = json.load(j)

current = False

historyES = {}
historyZH = {}

try:
    for college in data:
        name = college['college_name']
        if name == 'United States Merchant Marine Academy':
            current = True
        if not current:
            continue
        popular = college['popular_majors']
        top = college['top_salaries']
        ZHpop = []
        ESpop = []
        ZHtop = []
        ESTop = []
        ESname = translator.translate(name, dest='es')
        ZHname = translator.translate(name, dest='zh-cn')
        for major in popular:
            if major is None:
                continue
            ESdictpop = {}
            ZHdictpop = {}
            for key, value in major.items():
                if key == 'counts' or key == 'earnings':
                    ESdictpop[key] = value
                    ZHdictpop[key] = value
                    continue
                if value in historyES.keys():
                    ESdictpop[key] = historyES[value]
                    ZHdictpop[key] = historyZH[value]
                else:
                    ESdictpop[key] = translator.translate(value, dest='es').text
                    ZHdictpop[key] = translator.translate(value, dest='zh-cn').text
                    historyES[value] = ESdictpop[key]
                    historyZH[value] = ZHdictpop[key]
            ESpop.append(ESdictpop)
            ZHpop.append(ZHdictpop)
        for major in top:
            if major is None:
                continue
            ESdict = {}
            ZHdict = {}
            for key, value in major.items():
                if key == 'counts' or key == 'earnings':
                    ESdict[key] = value
                    ZHdict[key] = value
                    continue
                if value in historyES.keys():
                    ESdict[key] = historyES[value]
                    ZHdict[key] = historyZH[value]
                else:
                    ESdict[key] = translator.translate(value, dest='es').text
                    ZHdict[key] = translator.translate(value, dest='zh-cn').text
                    historyES[value] = ESdict[key]
                    historyZH[value] = ZHdict[key]
            ESTop.append(ESdict)
            ZHtop.append(ZHdict)
        college['college_nameES'] = ESname.text
        college['college_nameZH'] = ZHname.text
        college['popular_majorsES'] = ESpop
        college['popular_majorsZH'] = ZHpop
        college['top_salariesES'] = ESTop
        college['top_salariesZH'] = ZHtop
except Exception as e:
    with open('translated.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    traceback.print_exc()


with open('translated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

