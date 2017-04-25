# Welcome to onTrack

onTrack is made of several parts inculding webscraper, a database, a web server, and a web page. The webscraper creates a JSON object of courses.

Currently our database is hosted locally. We will soon move it over to AWS.

# Install Guide onTrack 1.0

### PRE-REQUISITES:
A Windows, Mac, or Linux computer capable of running a web browser

### DEPENDENCIES:

Python 2
Python 3
Flask version 0.12
SQLite 3.18.0
Web Browser
Selenium - Python 3
Beautifulsoup - Python 3

### DOWNLOAD INSTRUCTIONS

Download our project from:
https://github.com/JoshVorick/CurriculAnalyzer.git

Save the project in folder where you would like the server to run from.

### BUILD
No build necessary for this web application. 

### INSTALLATION INSTRUCTIONS

There are no installation instructions for our project besides installing the dependencies, but they all should come with their own instructions. 

### RUN INSTRUCTIONS

#### Webserver:

Navigate to the back_end folder of our project and run application.py with python3 and the webserver will begin working and hosting the site at a port that it tells you in the console. The port should default to 5000

#### Web scraper:

Navigate to the main directory of the project and use python 3 to launch webscrape.py. The program will then output the Json of all of the scraped course data that you can save directly to a file. You can then use the file “json_to_db.py” in the same directory to upload course data  json files into the database

#### Tree Builder:

Navigate to “/back_end/threads/treeBuilder.py” and run the program with python 3. The program will then use the data stored in the named text files in the same directory to generate json files for every possible combination of the files present in the directory.


### TROUBLESHOOTING

Make sure that port number that is used by Flask is currently available. If it is not, pass Flask an available port number



# Release Notes version onTrack 1.0

### NEW FEATURES:

Added treeBuilder tool.
Added the ability for the tree to change colors.
Added light and dark theme for the web page.
The program should now run 20% faster thanks to optimization.
Added json to database tool to help load course data into the database.
Added Plan on taking and completed lists with updating tree!


### BUG FIXES:

Fixed a bug in the javascript that caused the webpage to lag out on startup.

Fixed the nodes on the tree from having inverted colors (being all green on startup).

Added class certification with courses in  the database before adding classes to the lists.


### KNOWN BUGS:

Switching to light theme causes the plan and completed buttons to become unresponsive

Web scraper will break if the structure of oscar is changed.

Overlap between textual course information and course visualization (tree structure)




