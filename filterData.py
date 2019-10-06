
import csv

buildFiltered = "Agency,incident_type_primary,Street,City,State,Forcible,"
tempString = ""
tempStringComma = ""

counterDict = {"2019": {}, "2018": {},"2016": {}, "2015": {}, "2014": {}, "2013": {}, "2012": {}, "2011": {}, "2010": {}}


with open('ACCPD.csv', mode='r') as infile:
	reader = csv.DictReader(infile)
	for row in reader:
		#print(row)
		date = ""
		if (row['incident_datetime'].split("/")[2].split(" ")[0] != ""):
			date = row['incident_datetime'].split("/")[2].split(" ")[0]
			#print(date)
		if (int(date) >= 2010):
			if ("TRESPASS" in row['incident_type_primary']):
				#print(counterDict)
				if ("Trespassing" not in counterDict[date]):
					counterDict[date].update({"Trespassing": 1})
				else:
					counterDict[date]['Trespassing'] += 1

			if ("ASSAULT" in row['incident_type_primary']):
				if ("Assault" not in counterDict[date]):
					counterDict[date].update({"Assault": 1})
				else:
					counterDict[date]['Assault'] += 1

			if ("ALCOHOL" in row['incident_type_primary']):
				if ("Alcohol" not in counterDict[date]):
					counterDict[date].update({"Alcohol": 1})
				else:
					counterDict[date]['Alcohol'] += 1

			if ("BREAKING AND" in row['incident_type_primary']):
				if ("B&E" not in counterDict[date]):
					counterDict[date].update({"B&E": 1})
				else:
					counterDict[date]['B&E'] += 1	

			if ("DRIVING" in row['incident_type_primary']):
				#print(counterDict)
				if ("DrivingImpaired" not in counterDict[date]):
					counterDict[date].update({"DrivingImpaired": 1})
				else:
					counterDict[date]['DrivingImpaired'] += 1

			if ("DRUG" in row['incident_type_primary']):
				if ("Drug" not in counterDict[date]):
					counterDict[date].update({"Drug": 1})
				else:
					counterDict[date]['Drug'] += 1				

			if ("DRUNKENNESS" in row['incident_type_primary']):
				if ("Drunk" not in counterDict[date]):
					counterDict[date].update({"Drunk": 1})
				else:
					counterDict[date]['Drunk'] += 1

			if ("FIGHTING" in row['incident_type_primary']):
				if ("Fighting" not in counterDict[date]):
					counterDict[date].update({"Fighting": 1})
				else:
					counterDict[date]['Fighting'] += 1

			if ("RAPE" in row['incident_type_primary']):
				if ("Rape" not in counterDict[date]):
					counterDict[date].update({"Rape": 1})
				else:
					counterDict[date]['Rape'] += 1	

			if ("GUNSHOTS" in row['incident_type_primary']):
				if ("Gunshots" not in counterDict[date]):
					counterDict[date].update({"Gunshots": 1})
				else:
					counterDict[date]['Gunshots'] += 1

			if ("LOUD MUSIC" in row['incident_type_primary']):
				if ("LoudMusic" not in counterDict[date]):
					counterDict[date].update({"LoudMusic": 1})
				else:
					counterDict[date]['LoudMusic'] += 1
			if ("VANDALISM" in row['incident_type_primary']):
				if ("Vandalism" not in counterDict[date]):
					counterDict[date].update({"Vandalism": 1})
				else:
					counterDict[date]['Vandalism'] += 1




buildDict = ",Assault,Trespassing,B&E,LoudMusic,DrivingImpaired,Vandalism,Alcohol,Drunk,Fighting,Rape,Drug,Gunshots" + "\n"

print(counterDict)

for key in counterDict:
		print(key)
		if ((int(key) > 2016)):
			buildDict+= key + "," + str(counterDict[key]["Assault"]) +  "," + "0" + "," + str(counterDict[key]["B&E"]) + "," + "0" + ","
			buildDict+= str(counterDict[key]["DrivingImpaired"]) + "," + str(counterDict[key]["Vandalism"]) + "," + "0" + "," + str(counterDict[key]["Drunk"])
			buildDict+=  "," + "0" + "," + "0" + "," + str(counterDict[key]["Drug"]) + "," + "0" + "\n"
		if (key == "2015" or key == "2014"):
			buildDict+= key + "," + str(counterDict[key]["Assault"]) +  "," + "0" + "," + "0" + "," + "0" + ","
			buildDict+= str(counterDict[key]["DrivingImpaired"]) + "," + "0" + "," + "0" + "," + str(counterDict[key]["Drunk"])
			buildDict+=  "," + "0" + "," + "0" + "," + str(counterDict[key]["Drug"]) + "," + "0" + "\n"
		else:
			buildDict+= key + "," + str(counterDict[key]["Assault"]) +  "," + "0" + "," + "0" + "," + "0" + ","
			buildDict+= str(counterDict[key]["DrivingImpaired"]) + "," + "0" + "," + "0" + "," + str(counterDict[key]["Drunk"])
			buildDict+=  "," + "0" + "," + "0" + "," + str(counterDict[key]["Drug"]) + "," + "0" + "\n"


print(buildDict)


with open('filtered.csv', 'w') as f:
	f.write(buildDict)



'''
counterDict = {"Trespassing": 0, "Assault": 0, "MENTAL": 0}


with open('crimeData.csv', mode='r') as infile:
	reader = csv.DictReader(infile)
	for row in reader:
		#print(counterDict)
		if ("TRESPASSING" in row['Reported As']):
			print(date)
			counterDict["Trespassing"] += 1 # = {"Trespassing": counterDict["Trespassing"] + 1}
		if ("ASSAULT" in row['Reported As']):
			counterDict["Assault"] += 1
		if ("MENTAL" in row['Reported As']):
			counterDict["MENTAL"] += 1
		if ("MENTAL" in row['Reported As']):
			counterDict["MENTAL"] += 1

print(counterDict)

'''



			#print(str(row).split(';')[1])

#print(buildFiltered)

#with open('filtered.csv', 'w') as f:
#	f.write(buildFiltered)

'''
with open('uniprot.csv', 'w') as f:
    for key in uniprotDict.keys():
        f.write("%s,%s\n"%(key,uniprotDict[key]))


		with open(csv_file, "r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
        
    for i,row in enumerate(reader):
        uniprot = str(row["Uniprot"])
        family = str(row["Family"])
        sub_family = str(row["Subfamily"])

        subfamilyID = str(row["SubfamilyID"])
        id_nums = subfamilyID.split(".")

        key1 = str(id_nums[0])
        key2 = key1 + "." + str(id_nums[1])
        key3 = key2 + "." + str(id_nums[2])
        key4 = key3 + "." + str(id_nums[3])

        keys = [key1, key2, key3, key4]
        data = [uniprot, family, sub_family]
        doSomething(json_data["children"], keys, 0, data)

        with open(json_file, 'w') as fp:
            json.dump(json_data, fp)

'''