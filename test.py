from os import name
import traceback
from fuzzywuzzy import fuzz
import requests
import json
import urllib.request
from colorthief import ColorThief
import shutil


url = 'http://logo.clearbit.com/' + 'www.famu.edu' 
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response


# link = 'http://logo.clearbit.com/' + 'www.famu.edu'
# urllib.request.urlretrieve(link, 'college')
color_thief = ColorThief('img.png')
dom = color_thief.get_color(quality=10)
print(dom)

def get_url(name):
    name = name.replace("&", "")
    name = name.replace(".", "")
    print(name)
    base = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.name={name}&fields=school.name,latest.admissions.admission_rate.overall,school.school_url,location.lat,location.lon,school.locale,academics.program.program_reporter.program_1.cip_6_digit.title,latest.student.demographics.race_ethnicity.white,latest.student.demographics.race_ethnicity.black,latest.student.demographics.race_ethnicity.hispanic,latest.student.demographics.race_ethnicity.asian,latest.student.demographics.race_ethnicity.aian,latest.student.demographics.race_ethnicity.nhpi,latest.student.demographics.race_ethnicity.two_or_more,latest.student.demographics.race_ethnicity.non_resident_alien,latest.student.demographics.race_ethnicity.unknown,latest.student.size,school.carnegie_size_setting&api_key=zJUVytBSiG42DRiPmZbmk0a7Q9gcSamwFM3GHE9s".format(name=name)
    return base

new_data = []

def get_optimized_url(name, fields):
    name = name.replace("&", "")
    name = name.replace(".", "")
    base = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.name={name}&fields=".format(name=name)
    base += ",".join(fields)
    base += "&api_key=zJUVytBSiG42DRiPmZbmk0a7Q9gcSamwFM3GHE9s"
    return base 

def extract_salary(data):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        if data['earnings']['highest']['2_yr']['overall_median_earnings'] is None:
            return 0
        return data['earnings']['highest']['2_yr']['overall_median_earnings']
    except KeyError:
        return 0

def extract_grads(data):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        if data['counts']['ipeds_awards2'] is None:
            return 0
        return data['counts']['ipeds_awards2']
    except KeyError:
        return 0 

def delete_keys(dict_, keys):
    print(dict_)
    for key in keys:
        del dict_[key]
    return dict_

fields = [
          'school.name', 'school.ownership', 'latest.admissions.admission_rate.overall', 
          'latest.student.retention_rate.four_year.full_time', 'latest.student.size', 
          'school.school_url', 'school.price_calculator_url', 'location.lat', 'location.lon', 'school.locale', 
          'school.carnegie_size_setting', '2018.admissions.act_scores.25th_percentile.english', 
          '2018.admissions.act_scores.75th_percentile.english', '2018.admissions.act_scores.25th_percentile.math', 
          '2018.admissions.act_scores.75th_percentile.math', '2018.admissions.sat_scores.25th_percentile.critical_reading', 
          '2018.admissions.sat_scores.75th_percentile.critical_reading', '2018.admissions.sat_scores.25th_percentile.math', 
          '2018.admissions.sat_scores.75th_percentile.math', 'latest.student.demographics.men', 'latest.student.demographics.women', 
          'latest.student.demographics.race_ethnicity.white', 'latest.student.demographics.race_ethnicity.black', 'latest.student.demographics.race_ethnicity.hispanic', 
          'latest.student.demographics.race_ethnicity.asian', 'latest.student.demographics.race_ethnicity.aian', 'latest.student.demographics.race_ethnicity.nhpi', 
          'latest.student.demographics.race_ethnicity.two_or_more', 'latest.student.demographics.race_ethnicity.non_resident_alien', 
          'latest.student.demographics.race_ethnicity.unknown', 'latest.cost.attendance.academic_year', 'latest.cost.tuition.in_state', 
          'latest.cost.tuition.out_of_state', 'latest.school.tuition_revenue_per_fte', 'latest.school.instructional_expenditure_per_fte', 
          'net_price.public.by_income_level.0-30000', 'net_price.public.by_income_level.30001-48000',
          'net_price.public.by_income_level.48001-75000', 'net_price.public.by_income_level.75001-110000',
          'net_price.public.by_income_level.110001-plus', 'net_price.private.by_income_level.0-30000',
          'net_price.private.by_income_level.30001-48000', 'net_price.private.by_income_level.48001-75000', 
          'net_price.private.by_income_level.75001-110000', 'latest.school.faculty_salary',
          'latest.aid.pell_grant_rate', 'programs.cip_4_digit.title', 'programs.cip_4_digit.credential.title', 
          'programs.cip_4_digit.counts.ipeds_awards2', 'programs.cip_4_digit.earnings.highest.2_yr.overall_median_earnings'
        ]

# r = requests.get(get_optimized_url("Harvard University", fields))
# print(r.json())
data = """[
  {
    "college_name": "Wheaton College",
    "address": "501 College Ave",
    "city": "Wheaton",
    "state": "Illinois",
    "domain": "www.wheaton.edu",
    "graduation_rate": 89,
    "percent_admitted": 85,
    "tuition": 37700,
    "percent_financial_aid": 88,
    "SAT_W_75_Percentile": 720,
    "SAT_M_75_Percentile": 720,
    "ACT_25_Percentile": 26,
    "ACT_75_Percentile": 32,
    "application_total": 1889,
    "total_enrollment": 3279,
    "": ""
  }
]"""

# with open('data.json') as d:
#     listOfColleges = json.load(d)
# print(listOfColleges[0]) 

# cnt = 0
# for c in listOfColleges:
#     c = {k: v for k, v in c.items() if k != ""}
#     if cnt == 0:
#        print(c) 
#        break
#     cnt += 1

new_ = json.loads(data)
# print(new_)

duplicate_keys = ['school.school_url', 'school.name', 'latest.programs.cip_4_digit', 'SAT_W_75_Percentile', 'SAT_M_75_Percentile']

try:
    for c in new_:
        c = {k: v for k, v in c.items() if k != ""}
        c_name = c['college_name']
        website = c['domain']
        url = get_optimized_url(c_name, fields)
        r = requests.get(url)
        responseJSON = r.json()
        for college in responseJSON['results']:
            if (fuzz.WRatio(college['school.name'], c_name) >= 99 or fuzz.WRatio(college['school.school_url'], website) >= 99):
                biggestMajors = []
                highestEarningMajors = []
                # c['percent_admitted'] = college['latest.admissions.admission_rate.overall']
                # c['latitude'] = college['location.lat']
                # c['longitude'] = college['location.lon']
                # c['setting'] = college['school.locale']
                college['latest.programs.cip_4_digit'].sort(key=extract_grads, reverse=True)
                for i in range(5):
                    biggestMajors.append(college['latest.programs.cip_4_digit'][i])
                college['latest.programs.cip_4_digit'].sort(key=extract_salary, reverse=True)
                for i in range(5):
                    highestEarningMajors.append(college['latest.programs.cip_4_digit'][i])
                c['popular_majors'] = biggestMajors
                c['top_salaries'] = highestEarningMajors
                c.update(college)
                c = delete_keys(c, duplicate_keys)
                new_data.append(c)
except Exception as e:
    # print("fail")
    with open('wheaton.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
        traceback.print_exc()

with open('data.json') as d:
    listOfColleges = json.load(d)
#print(listOfColleges[0]) 
print(listOfColleges)
with open('new_data.json') as j:
    new_data = json.load(j)

names = []

cnt = {}

# for i in listOfColleges:
#     names.append(i['college_name'])
# print(names)
# for i in new_data:
#     if (i['college_name'] not in cnt.keys()):
#         cnt[i['college_name']] = 1
#     else:
#         cnt[i['college_name']] += 1
# for k, i in cnt.items():
#     if i > 1:
#         print(k + "   " + str(i))


def remove_dup(it):
    seen = []
    for x in it:
        if x not in seen:
            yield x
            seen.append(x)

n = list(remove_dup(new_data))

cnt = {}

for i in n:
    if (i['college_name'] not in cnt.keys()):
        cnt[i['college_name']] = 1
    else:
        cnt[i['college_name']] += 1
for k, i in cnt.items():
    if i > 1:
        print(k + "   " + str(i))

print(len(listOfColleges))
print(len(n))

li = []

for i in n:
    li.append(i['college_name'])

for i in listOfColleges:
    if i['college_name'] not in li:
        print(i['college_name'])



with open('final_data.json', 'w', encoding='utf-8') as f:
        json.dump(n, f, ensure_ascii=False, indent=4)

with open('addColors.json') as d:
    lis = json.load(d)

lis = lis[0]

popular = lis['popular_majors']
salaries = lis['top_salaries']

for pMajor in popular:
    pMajor['title'] = pMajor['title'].strip('.,')
    pMajor['credential'] = pMajor['credential']['title'].strip('.,')
    counts = pMajor['counts']['ipeds_awards2']
    pMajor['counts'] = str(counts) if counts is not None else None
    
    earnings = pMajor['earnings']['highest']['2_yr']['overall_median_earnings']
    pMajor['earnings'] = str(earnings) if earnings is not None else None
for sMajor in salaries:
    sMajor['title'] = sMajor['title'].strip('.,')
    sMajor['credential'] = sMajor['credential']['title'].strip('.,')

    counts = sMajor['counts']['ipeds_awards2']
    sMajor['counts'] = str(counts) if counts is not None else None

    earnings = sMajor['earnings']['highest']['2_yr']['overall_median_earnings']
    sMajor['earnings'] = str(earnings) if earnings is not None else None

with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(lis, f, ensure_ascii=False, indent=4)

with open('addColors.json') as j:
    data = json.load(j)

with open('data.json') as j:
    d = json.load(j)

print(len(data), len(d))