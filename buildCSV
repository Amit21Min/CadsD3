
import csv
from collections import defaultdict
counterDict = defaultdict(dict)


buildFiltered = "Agency,Offense,Street,City,State,Forcible,"
tempString = ""
tempStringComma = ""
buildDict = ""

#counters = {"ASSAULT", "TRESPASSING":0, "B&E":0, "LOUD MUSIC":0, "DRIVING":0, "VANDALISM":0, "ALCOHOL":0, "DRUNK":0, "DRUNK":0, "FIGHTING":0, "RAPE":0, "DRUG":0, "GUNSHOTS":0, }
counters = {}

#counterDict = {"2019": {}, "2018": {}, "2017": {}, "2016": {}, "2015": {}, "2014": {}, "2013": {}, "2012": {}, "2011": {}, "2010": {}}
counterDict['2019'] = {}
counterDict['2018'] = {}
counterDict['2017'] = {}
counterDict['2016'] = {}
counterDict['2015'] = {}
counterDict['2014'] = {}
counterDict['2013'] = {}
counterDict['2012'] = {}
counterDict['2011'] = {}
counterDict['2010'] = {}

print(counterDict)

testDict = {"2019": {}, "2018": {}, "2017": {}, "2016": {}, "2015": {}, "2014": {}, "2013": {}, "2012": {}, "2011": {}, "2010": {}}
#counterDict = testDict

counter = 0
streetCounter = 0
with open('crimeData.csv', mode='r') as infile:
	for row in infile:
		#print(row)
		street = row.split(",")[2].split(" ", 1)
		year = row.split(",")[8].split("/")
		crime = row.split(",")[1]
		#print(crime)
		if (len(year) > 1):
			year = year[2]
		#print(year)
		if (len(street) > 1):
			street = street[1]
		else:
			street = street[0]
		#print(counterDict)
		if ("ASSAULT" in row.split(",")[1] and not "NO ASSAULT" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Assault": 1}})
			elif (street in counterDict[year]):
				if ("Assault" not in counterDict[year][street]):
					counterDict[year][street]["Assault"] = 1
				else:
					counterDict[year][street]["Assault"] += 1
			buildDict += row
		if ("TRESPASSING" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Trespassing": 1}})
			elif (street in counterDict[year]):
				if ("Trespassing" not in counterDict[year][street]):
					counterDict[year][street]["Trespassing"] = 1
				else:
					counterDict[year][street]["Trespassing"] += 1			
			#counters["TRESPASSING"] += 1
			buildDict += row
		if ("B&E" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"B&E": 1}})
			elif (street in counterDict[year]):
				if ("B&E" not in counterDict[year][street]):
					counterDict[year][street]["B&E"] = 1
				else:
					counterDict[year][street]["B&E"] += 1			
			buildDict += row
		if ("LOUD MUSIC" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"LoudMusic": 1}})
			elif (street in counterDict[year]):
				if ("LoudMusic" not in counterDict[year][street]):
					counterDict[year][street]["LoudMusic"] = 1
				else:
					counterDict[year][street]["LoudMusic"] += 1			
			buildDict += row
		if ("DRIVING" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Driving": 1}})
			if (street in counterDict[year]):
				if ("Driving" not in counterDict[year][street]):
					counterDict[year][street]["Driving"] = 1
				else:
					counterDict[year][street]["Driving"] += 1			
			buildDict += row			
		if ("VANDALISM" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Vandalism": 1}})
			elif (street in counterDict[year]):
				if ("Vandalism" not in counterDict[year][street]):
					counterDict[year][street]["Vandalism"] = 1
				else:
					counterDict[year][street]["Vandalism"] += 1			
			buildDict += row
		if ("ALCOHOL" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year][street] = {"Alcohol": 1}
				#counterDict[year].update({street: {"Alcohol": 1}})
			elif (street in counterDict[year]):
				if ("Alcohol" not in counterDict[year][street]):
					counterDict[year][street]["Alcohol"] = 1
				else:
					counterDict[year][street]["Alcohol"] += 1			
			buildDict += row
		if ("DRUNK" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Drunk": 1}})
			elif (street in counterDict[year]):
				if ("Drunk" not in counterDict[year][street]):
					counterDict[year][street]["Drunk"] = 1
				else:
					counterDict[year][street]["Drunk"] += 1			
			buildDict += row
		if ("FIGHTING" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Fighting": 1}})
			elif (street in counterDict[year]):
				if ("Fighting" not in counterDict[year][street]):
					counterDict[year][street]["Fighting"] = 1
				else:
					counterDict[year][street]["Fighting"] += 1			
			buildDict += row
		if ("RAPE" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Rape": 1}})
			elif (street in counterDict[year]):
				if ("Rape" not in counterDict[year][street]):
					counterDict[year][street]["Rape"] = 1
				else:
					counterDict[year][street]["Rape"] += 1			
			buildDict += row
		if ("DRUG" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Drug": 1}})
			elif (street in counterDict[year]):
				if ("Drug" not in counterDict[year][street]):
					counterDict[year][street]["Drug"] = 1
				else:
					counterDict[year][street]["Drug"] += 1			
			buildDict += row
		if ("GUNSHOTS" in row.split(",")[1]):
			streetCounter += 1
			if (street not in counterDict[year]):
				counterDict[year].update({street: {"Gunshots": 1}})
			elif (street in counterDict[year]):
				if ("Gunshots" not in counterDict[year][street]):
					counterDict[year][street]["Gunshots"] = 1
				else:
					counterDict[year][street]["Gunshots"] += 1		
			buildDict += row

print(counterDict)
buildString = "Year,Street,Crime,Quantity" + "\n"

for year in counterDict:
	for street in counterDict[year]:
		
		for crime in counterDict[year][street]:
			buildString += year + "," + street + "," + crime + "," + str(counterDict[year][street][crime]) + '\n'

with open('filteredForJSON2.csv', 'w') as f:
	f.write(buildString)
