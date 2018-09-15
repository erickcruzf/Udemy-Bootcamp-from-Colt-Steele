import csv
 
def addUser(firstName, lastName):
    with open("users.csv", "a") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow([firstName, lastName])

def printUsers():
    with open("users.csv") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csv_reader: 
            print(f"{row['First Name']} {row['Last Name']}")

def findUser(firstName, lastName):
    with open ("users.csv") as csvFile:
        csvReader = csv.reader(csvFile)
        for (index, row) in enumerate(csvReader):
            firstMatch = firstName == row[0]
            lastMatch = lastName == row[1]
            if firstMatch and lastMatch:
                return index
        return "{} {} not found.".format(firstName, lastName)

def update_users(oldFirst, oldLast, newFirst, newLast):
    with open("users.csv") as csvFile:
        csvReader = list(csv.reader(csvFile))
        
    update = 0
    with open("users.csv", "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for row in csvReader:
            if row[0] == oldFirst and row[1] == oldLast:
                update += 1
                csvWriter.writerow([newFirst, newLast])
            else:
                csvWriter.writerow(row)
        return "Users updated: {}.".format(update)

def delete_users(firstName, lastName):
    with open("users.csv") as csvFile:
        csvReader = csv.reader(csvFile)
        rows = [row for row in csvReader]
    
    removed = 0
    with open("users.csv" , "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for ele in rows:
            if ele[0] == firstName and ele[1] == lastName:
                removed += 1
            else:
                csvWriter.writerow(ele)
        return "Users deleted: {}.".format(removed)