import csv

input_file = input("Enter the name of csv file: ")

f = open(input_file)
csv_f = csv.reader(f)

content_read = ""

for row in csv_f:
    content_read += "\n" + "The content is: " + row[0] + " and " + row[1] #+ " and " + row[2]

print(content_read)