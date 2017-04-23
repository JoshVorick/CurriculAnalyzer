from selenium import webdriver
from bs4 import BeautifulSoup
import json
import urllib.request as urllib

class Course:
    """Represents a Course Object"""

    def __init__(self, subj, number, name, description, gradeBasis, creditHours, lectureHours, labHours, dept, sectionsLink, restrictions, prerequisites):
        self.subj = subj
        self.number = number
        self.name = name
        self.description = description
        self.gradeBasis = gradeBasis
        self.creditHours = creditHours
        self.lectureHours = lectureHours
        self.labHours = labHours
        self.dept = dept
        self.sectionsLink = sectionsLink
        self.prerequisites = prerequisites
        self.restrictions = restrictions

    def __str__(self):
        # return str([self.subj, self.number, self.name, self.description, self.gradeBasis, self.creditHours, self.lectureHours, self.labHours, self.dept, self.sectionsLink, self.restrictions, self.prerequisites])
        return json.dumps(self, default=lambda o: o.__dict__)

def multiselect_set_selections(driver, element_id, labels):
    el = driver.find_element_by_id(element_id)
    for option in el.find_elements_by_tag_name('option'):
        if option.text in labels:
            option.click()


driver = webdriver.Chrome()
driver.get("https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg")
multiselect_set_selections(driver, "term_input_id", ['Spring 2017'])
NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Submit"]'
button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
button.click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
multiselect_set_selections(driver, 'subj_id', ['Computer Science'])
NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Get Courses"]'
button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
button.click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
soup = BeautifulSoup(driver.page_source, "html.parser")
Coursetitles = soup.findAll("td", {"class": "nttitle"})
courses = []
for section in Coursetitles:
    courseSoup = BeautifulSoup(urllib.urlopen("https://oscar.gatech.edu" + str(section.find('a')['href'])).read(), "html.parser")
    titles = courseSoup.findAll("td", {"class": "nttitle"})
    for title in titles:
        titleBreakdown = title.text.split(" ", 3)
        courseSubj = titleBreakdown[0].strip()
        courseNumber = titleBreakdown[1].strip()
        courseName = titleBreakdown[3].strip()
        coursePrerequisites = courseRestrictions = courseDescription = ""
        courseDept = courseGradeBasis = courseCreditHours = courseLectureHours = courseLabHours = "NULL"
        infoBlock = title.parent.nextSibling.nextSibling
        linkSearch = infoBlock.find('a')
        if linkSearch is not None:
            courseSectionsLink = "https://oscar.gatech.edu/" + linkSearch['href']
        else:
            courseSectionsLink = 'NULL'
        restrictions = False
        prerequisites = False
        info = infoBlock.text.split("\n")
        for line in info:
            if line is not "":
                if "Credit hours" in line:
                    courseCreditHours = line
                elif "Lecture hours" in line:
                    courseLectureHours = line
                elif "Lab hours" in line:
                    courseLabHours = line
                elif "Grade Basis:" in line:
                    courseGradeBasis = line.split(":")[1].strip()
                elif "Dept/" in line:
                    courseDept = line.split("/")[1]
                elif "Restrictions:" == line.strip():
                    restrictions = True
                    prerequisites = False
                elif "Prerequisites:" in line.strip():
                    prerequisites = True
                    restrictions = False
                elif restrictions:
                    courseRestrictions += line.strip() + "\n"
                elif prerequisites:
                    coursePrerequisites += line.strip() + "\n"
                elif courseDescription is "":
                    courseDescription = line
        course = Course(courseSubj, courseNumber, courseName, courseDescription, courseGradeBasis, courseCreditHours, courseLectureHours, courseLabHours, courseDept, courseSectionsLink, courseRestrictions, coursePrerequisites)
        courses.append(course)  # This is slow b/c memory alloc :(
        # print(course.subj, course.number)

print(json.dumps(courses, default=lambda o: o.__dict__))
driver.quit()
