import json
from os import name
from fuzzywuzzy import fuzz

with open('n.json') as j:
    data = json.load(j)

all_indices = {}
top_10_CS = ["Carnegie Mellon University", "Massachusetts Institute of Technology", "Stanford University", "University of California-Berkeley", "Cornell University", "Georgia Institute of Technology-Main Campus", "University of Illinois at Urbana-Champaign", "California Institute of Technology", "Princeton University", "University of California-Los Angeles"] 
top_10_Business = ["University of Pennsylvania", "Massachusetts Institute of Technology", "University of California-Berkeley", "University of Michigan-Ann Arbor", "New York University", "The University of Texas at Austin", "Carnegie Mellon University", "Cornell University", "Indiana University-Bloomington", "University of North Carolina at Chapel Hill"]
top_10_PoliSci = ["Stanford University", "Harvard University", "Princeton University", "University of California-Berkeley", "University of Michigan-Ann Arbor", "Yale University", "Massachusetts Institute of Technology", "Columbia University in the City of New York", "University of California-San Diego", "Duke University"]
top_10_Engineering = ["Massachusetts Institute of Technology", "Stanford University", "University of California-Berkeley", "California Institute of Technology", "Georgia Institute of Technology-Main Campus", "Carnegie Mellon University", "University of Illinois at Urbana-Champaign", "University of Michigan-Ann Arbor", "Cornell University", "Purdue University-Main Campus"]
top_10_Bio = ["Harvard University", "Massachusetts Institute of Technology", "Stanford University", "University of California-Berkeley", "University of California-San Diego", "Johns Hopkins University", "Cornell University", "University of Washington-Seattle Campus", "University of California-Los Angeles", "University of Michigan-Ann Arbor"]
top_10_Psych = ["Stanford University", "University of California-Berkeley", "Harvard University", "University of California-Los Angeles", "University of Michigan-Ann Arbor", "Yale University", "University of Illinois at Urbana-Champaign", "Massachusetts Institute of Technology", "Princeton University", "University of Minnesota-Twin Cities"]
top_10_Nursing = ["University of Pennsylvania", "Duke University", "University of Washington-Seattle Campus", "Emory University", "University of Michigan-Ann Arbor", "University of North Carolina at Chapel Hill", "New York University", "University of Pittsburgh-Pittsburgh Campus", "Case Western Reserve University", "Ohio State University-Main Campus"]


def get_indices(arr, major):
    indices = []
    for name in arr:
        for i in range(len(data)):
            c_name = data[i]['college_name']
            website = data[i]['domain']
            if fuzz.WRatio(name, c_name) >= 98 or fuzz.WRatio(name, website) >= 99:
                # print(i, c_name, website)
                indices.append(i)
                break
            if i >= len(data) - 1:
                print('name: ', name)
    all_indices[major] = indices
    print(len(indices))

# get_indices(top_10_CS, "Computer Science")
# get_indices(top_10_Business, "Business")
# get_indices(top_10_PoliSci, "Political Science")
# get_indices(top_10_Engineering, "Engineering")
get_indices(top_10_Bio, "Biology")
get_indices(top_10_Psych, "Psychology")
get_indices(top_10_Nursing, "Nursing")

print(all_indices)
print(len(all_indices))
