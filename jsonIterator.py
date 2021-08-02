import json
from test import new_data
import requests
import sys
from fuzzywuzzy import fuzz
import traceback

def get_optimized_url(name, fields):
    # construct api endpoint url with params: college name, fields indicating desired variables 
    name = name.replace("&", "")
    name = name.replace(".", "")
    base = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.name={name}&fields=".format(name=name)
    base += ",".join(fields)
    base += "&api_key=zJUVytBSiG42DRiPmZbmk0a7Q9gcSamwFM3GHE9s"
    return base 

def extract_salary(data):
    # function for sorting salaries
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        if data['earnings']['highest']['2_yr']['overall_median_earnings'] is None:
            return 0
        return data['earnings']['highest']['2_yr']['overall_median_earnings']
    except KeyError:
        return 0

def extract_grads(data):
    # function for sorting counts
    try:
        if data['counts']['ipeds_awards2'] is None:
            return 0
        return data['counts']['ipeds_awards2']
    except KeyError:
        return 0 

def delete_keys(dict_, keys):
    # lives up to its name :P
    for key in keys:
        del dict_[key]
    return dict_

headers = {'Content-Type': 'application/json'}
# #print(sys.executable)
with open('data.json') as d:
    listOfColleges = json.load(d)
# #print(listOfColleges[0]) 
# print(listOfColleges)
with open('new_data.json') as j:
    new_data = json.load(j)

# names of the variables to be received from api endpoint
fields = [
          'school.name', 'school.ownership', 'latest.admissions.admission_rate.overall', 
          'latest.student.retention_rate.four_year.full_time', 'latest.student.size', 
          'school.school_url', 'school.price_calculator_url', 'location.lat', 'location.lon', 'school.locale', 
          'school.carnegie_size_setting', 'latest.admissions.act_scores.25th_percentile.english', 
          'latest.admissions.act_scores.75th_percentile.english', 'latest.admissions.act_scores.25th_percentile.math', 
          'latest.admissions.act_scores.75th_percentile.math', 'latest.admissions.sat_scores.25th_percentile.critical_reading', 
          'latest.admissions.sat_scores.75th_percentile.critical_reading', 'latest.admissions.sat_scores.25th_percentile.math', 
          'latest.admissions.sat_scores.75th_percentile.math', 'latest.student.demographics.men', 'latest.student.demographics.women', 
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

duplicate_keys = ['school.school_url', 'school.name', 'latest.programs.cip_4_digit']
# duplicate_keys_original = ['SAT_W_75_Percentile', 'SAT_M_75_Percentile']

try:
    for c in listOfColleges:
        c = {k: v for k, v in c.items() if k != ""} # removes empty key, value pairs
        c_name = c['college_name']
        # print(c_name)
        website = c['domain']
        url = get_optimized_url(c_name, fields)
        r = requests.get(url, headers=headers)
        responseJSON = r.json()
        for college in responseJSON['results']:
            if len(college['school.name'].split(" ")) == len(c_name.split(" ")) and (fuzz.WRatio(college['school.name'], c_name) >= 99 or fuzz.WRatio(college['school.school_url'], website) >= 99):
                # sometimes the response has multiple colleges that closely match, the if statement makes sure we're getting the correct data
                biggestMajors = []
                highestEarningMajors = []
                college['latest.programs.cip_4_digit'].sort(key=extract_grads, reverse=True) # sort entries by number count
                for i in range(5):
                    if i > len(college['latest.programs.cip_4_digit']) - 1:
                        biggestMajors.append(None)
                    else:
                        biggestMajors.append(college['latest.programs.cip_4_digit'][i])
                college['latest.programs.cip_4_digit'].sort(key=extract_salary, reverse=True) # sort entries by number of grads
                for i in range(5):
                    if i > len(college['latest.programs.cip_4_digit']) - 1:
                        highestEarningMajors.append(None)
                    else:
                        highestEarningMajors.append(college['latest.programs.cip_4_digit'][i])
                c['popular_majors'] = biggestMajors
                c['top_salaries'] = highestEarningMajors
                c.update(college)
                c = delete_keys(c, duplicate_keys)
                new_data.append(c)
except Exception as e:
    with open('new_data.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    traceback.print_exc()

with open('new_data.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)