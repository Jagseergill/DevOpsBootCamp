import csv

req_file = "/Udemy/working_With_CSV_Files/demofile.csv"

file_open = open(req_file, 'w', newline="")
csv_writer = csv.writer(file_open, delimiter=",")

csv_writer.writerow(['S_no', "Name", "Age"])
csv_writer.writerow(['1', "John", '29'])
csv_writer.writerow(['2', "Harry", '39'])
file_open.close()
