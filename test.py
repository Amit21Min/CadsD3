
import csv

buildFiltered = ""
tempString = ""
tempStringComma = ""
with open('police-incident-reports-written.csv', mode='r') as infile:
	#reader = csv.DictReader(infile)
	for row in infile:
		print(row)




			#print(str(row).split(';')[1])


'''
print(buildFiltered)

with open('suicides.csv', 'w') as f:
	f.write(buildFiltered)


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