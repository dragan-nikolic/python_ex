# importing the csv module
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

def write_comma():
    # name of comma separated csv file
    filename = "university_records_comma.csv"

    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(rows)

def write_tab():
    # name of tab separated csv file
    filename = "university_records_tab.csv"

    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile, dialect='excel-tab')
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(rows)

write_comma()
write_tab()
