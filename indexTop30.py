import json
from os import name
from fuzzywuzzy import fuzz

with open('n.json') as j:
    data = json.load(j)

top_thirty = ["Princeton University", "Harvard University", "Columbia University", "University of Florida", "Massachusetts Institute of Technology", "Yale University", "Stanford University", "University of Chicago", "University of Pennsylvania", "California Institute of Technology", "Johns Hopkins University", "Northwestern University", "Duke University", "Dartmouth College", "Brown University", "Vanderbilt University", "Rice University", "Washington University in St. Louis", "Cornell University", "University of Notre Dame", "University of California - Los Angeles", "Emory University", "University of California - Berkeley", "Georgetown University", "University of Michigan", "Carnegie Mellon University", "University of Virginia-Main Campus", "University of Southern California", "New York University", "Tufts University", "University of California - Santa Barbara"] 
top_thirty = ["Carnegie Mellon University", "Massachusetts Institute of Technology", "Stanford University", "University of California - Berkeley", "Cornell University", "Georgia Institute of Technology", "University of Illinois at Urbana-Champaign", "California Institute of Technology", "Princeton University", "University of California - Los Angeles", "Johns Hopkins University", "Northwestern University", "Duke University", "Dartmouth College", "Brown University", "Vanderbilt University", "Rice University", "Washington University in St. Louis", "Cornell University", "University of Notre Dame", "University of California - Los Angeles", "Emory University", "University of California - Berkeley", "Georgetown University", "University of Michigan", "Carnegie Mellon University", "University of Virginia-Main Campus", "University of Southern California", "New York University", "Tufts University", "University of California - Santa Barbara"]
indices = []

for name in top_thirty:
    for i in range(len(data)):
        c_name = data[i]['college_name']
        website = data[i]['domain']
        if fuzz.WRatio(name, c_name) >= 98 or fuzz.WRatio(name, website) >= 99:
            print(i, c_name, website)
            indices.append(i)
            break
        if i >= len(data) - 1:
            print('name: ', name)

print(indices)
print(len(indices))
