import csv

req_file = "/Udemy/working_With_CSV_Files/mycsvfile.csv"

fo = open(req_file, "r")
csv_reader = csv.reader(fo, delimiter="|")
# csv_reader = fo.readline()

#print(list(csv_reader))

#print(f'The Header is :\n{list(csv_reader)[0]}')

header = next(csv_reader)

print("The header is: ", header)

print("The number of rows are: ", len(list(csv_reader)))
''' 
for each in csv_reader:
    print(each)
'''
fo.close()
