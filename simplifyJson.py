import json

with open('addColors.json') as j:
    data = json.load(j)

n = []

for college in data:
    popular = college['popular_majors']
    salaries = college['top_salaries']

    newPopular = []
    newSalaries = []
    print(college['college_name'])

    for pMajor in popular:
        if pMajor:
            pMajor['title'] = pMajor['title'].strip('.,')
            pMajor['credential'] = pMajor['credential']['title'].strip('.,')

            counts = pMajor['counts']['ipeds_awards2']
            pMajor['counts'] = str(counts) if counts is not None else None
            
            earnings = pMajor['earnings']['highest']['2_yr']['overall_median_earnings']
            pMajor['earnings'] = str(earnings) if earnings is not None else None
        newPopular.append(pMajor)
    for sMajor in salaries:
        if sMajor:
            sMajor['title'] = sMajor['title'].strip('.,')
            sMajor['credential'] = sMajor['credential']['title'].strip('.,')

            counts = sMajor['counts']['ipeds_awards2']
            sMajor['counts'] = str(counts) if counts is not None else None

            earnings = sMajor['earnings']['highest']['2_yr']['overall_median_earnings']
            sMajor['earnings'] = str(earnings) if earnings is not None else None
        newSalaries.append(sMajor)
    popular = newPopular
    salaries = newSalaries
# print(data[0])


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)