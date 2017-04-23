from selenium import webdriver
from bs4 import BeautifulSoup
from time import time


class custObj:
    def __init__(self, data, numReq, dataType, title):
        # numReq is  (number >= -1) if -1 then all courses in the list are required,
        # otherwise numReq number of courses are required
        # dataType will either be "class" or "grouping" if "class", a class is
        # stored in data. If "grouping", a list of custObj are stored in data
        self.dataType = dataType
        self.data = data
        self.numReq = numReq
        self.title = title

    # def __str__(self):
    #     out = ""
    #     for item in listOfItems:
    #         if isinstance(item, requirement):

    #         else:


timer = time()
print(time() - timer)
# print((time() - time))
threads = ("devices", "information-internetworks", "intelligence", "media", "modeling-simulation", "people-0", "systems-architecture", "theorythread")
threadReqs = []
for thread in threads:
    driver = webdriver.Chrome("/Users/xiangtiangu/Downloads/chromedriver")
    driver.get("http://www.cc.gatech.edu/" + thread)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    webText = soup.getText()
    textIndexReq = webText.find("Required Courses:")
    textIndexEnd = webText.find("Academics", textIndexReq)
    coreReqText = webText[textIndexReq:textIndexEnd]
    reqCourseList = []
    elecCourseList = []

    # custObj(data, -1, dataType, title))

    required = True
    for line in coreReqText.split("\n"):
        # line = line.replace(" ", "")
        if line is not "" and line is not "Required Courses:" and "View the course prerequisites for" not in line:
            if "," in line:
                if required:
                    reqCourseList.append(line.split(",")[0])
                else:
                    elecCourseList.append(line.split(",")[0])
            else:
                if any(c.isalpha() for c in line):
                    if "Elective Courses:" in line:
                        required = False
                        continue

    print("\n########## %s ##########" % thread.upper())
    print("### Required: ###")
    for course in reqCourseList:
        print(course)
    print("### Elective: ###")
    for course in elecCourseList:
        print(course)

    driver.quit()

print(time() - timer)
