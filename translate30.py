from googletrans.client import Translator
import googletrans

translator = Translator()

arr = ["Princeton University", "Harvard University", "Columbia University", "Massachusetts Institute of Technology", "Yale University", "Stanford University", "University of Chicago", "University of Pennsylvania", "California Institute of Technology", "Johns Hopkins University", "Northwestern University", "Duke University", "Dartmouth College", "Brown University", "Vanderbilt University", "Rice University", "Washington University in St. Louis", "Cornell University", "University of Notre Dame", "University of California - Los Angeles", "Emory University", "University of California - Berkeley", "Georgetown University", "University of Michigan", "Carnegie Mellon University", "University of Virginia-Main Campus", "University of Southern California", "New York University", "Tufts University", "University of California - Santa Barbara"]

esarr = []
zharr = []

for name in arr:
    ESname = translator.translate(name, dest='es')
    ZHname = translator.translate(name, dest='zh-cn')
    esarr.append(ESname.text)
    zharr.append(ZHname.text)

print(esarr)
print()
print(zharr)