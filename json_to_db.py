# This file takes the webscraper's json output (passed in as a filename) and
# adds it to the database (passed in as a parameter)
# For example: "python json_to_db.py out.json database.db"

import sqlite3
import json
from pprint import pprint
from sys import argv

print(argv)
if len(argv) < 3:
    print("Please pass in the JSON filepath and SQLITE3 DB path")
    print("For example: `python json_to_db.py out.json database.db`")
    exit(0)


# Read in JSON file
with open(argv[1]) as json_file:
    data = json.load(json_file)

pprint(data[0])

# Open a Database Connection
conn = sqlite3.connect(argv[2])
print("Connected to", argv[2])

# Question: Should we delete all courses before adding new ones?  Or can we
# rely on some uniqueness thing in the database to guarantee nothing goes or?

for d in data:
    # Insert this course into the DB

    # columns = "(dept, subNumber, name, description, gradeBasis, maxCreditHours, minCreditHours, maxLectureHours, minLectureHours, maxLabHours, minLabHours, departmentName, sectionsLink, restrictions, prerequisites)"
    columns = "(dept, subNumber, name, description, sectionsLink, resctrictions, maxCreditHours)"
    values = "('" + d['subj'] + "', '" + d['number'] + "', '" + d['name'] + "', '" + d['description']
    values += "', '" + d['sectionsLink'] + "', '" + d['restrictions'] + "', '" + d['creditHours'] + "')"


    sql = "insert into course " + columns + " values " + values
    print(sql)
    conn.execute(sql)

conn.commit()
conn.close()
